from __future__ import annotations
import json, os, re, sqlite3, tempfile, time
from pathlib import Path
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_COLUMNS = ['draw_no','draw_date','n1','n2','n3','n4','n5','n6','bonus']
PRIZE_COLUMNS = [x for i in range(1,6) for x in (f'prize_{i}', f'winners_{i}')]
EXTRA_COLUMNS = ['total_sales_amount','auto_winners','semi_auto_winners','manual_winners']
COLUMNS = BASE_COLUMNS
OFFICIAL_JSON_URLS = (
    'https://www.dhlottery.co.kr/lt645/selectPstLt645Info.do?srchLtEpsd={draw_no}',
    'https://www.dhlottery.co.kr/lt645/selectPstLt645InfoNew.do?srchLtEpsd={draw_no}',
)
MIRROR_ALL_URL = 'https://smok95.github.io/lotto/results/all.json'
MIRROR_LATEST_URL = 'https://smok95.github.io/lotto/results/latest.json'
OFFICIAL_RESULT_URL = 'https://m.dhlottery.co.kr/lt645/result'


def _session() -> requests.Session:
    s=requests.Session()
    retry=Retry(total=3, connect=3, read=3, backoff_factor=.7,
                status_forcelist=(429,500,502,503,504), allowed_methods=frozenset(['GET']))
    s.mount('https://', HTTPAdapter(max_retries=retry)); s.mount('http://', HTTPAdapter(max_retries=retry))
    s.headers.update({'User-Agent':'Mozilla/5.0 (MD-Lotto v3 research; personal use)',
                      'Accept':'application/json,text/plain,*/*'})
    return s


def validate(df: pd.DataFrame, require_contiguous: bool=False) -> pd.DataFrame:
    missing=[c for c in BASE_COLUMNS if c not in df.columns]
    if missing: raise ValueError(f'Missing columns: {missing}')
    keep=BASE_COLUMNS+[c for c in PRIZE_COLUMNS+EXTRA_COLUMNS if c in df.columns]
    out=df[keep].copy()
    for c in ['draw_no','n1','n2','n3','n4','n5','n6','bonus']:
        out[c]=pd.to_numeric(out[c],errors='raise').astype(int)
    for c in PRIZE_COLUMNS+EXTRA_COLUMNS:
        if c in out.columns: out[c]=pd.to_numeric(out[c],errors='coerce')
    out['draw_date']=pd.to_datetime(out['draw_date'],errors='coerce')
    if out['draw_date'].isna().any(): raise ValueError('Invalid draw_date detected')
    if out['draw_no'].duplicated().any(): raise ValueError('Duplicate draw_no detected')
    for idx,r in out.iterrows():
        nums=[int(r[f'n{i}']) for i in range(1,7)]; sn=sorted(nums)
        if len(set(sn))!=6 or not all(1<=x<=45 for x in sn):
            raise ValueError(f'Invalid winning numbers at draw {int(r.draw_no)}: {nums}')
        for i,n in enumerate(sn,1): out.at[idx,f'n{i}']=n
        bonus=int(r.bonus)
        if not 1<=bonus<=45 or bonus in sn: raise ValueError(f'Invalid bonus at draw {int(r.draw_no)}')
    out=out.sort_values('draw_no').reset_index(drop=True)
    if require_contiguous and len(out):
        expected=list(range(int(out.draw_no.min()),int(out.draw_no.max())+1))
        if out.draw_no.tolist()!=expected:
            missing_draws=sorted(set(expected)-set(out.draw_no))
            raise ValueError(f'Missing draw numbers: {missing_draws[:30]}')
    return out


def dataset_status(df: pd.DataFrame) -> dict:
    d=validate(df); contiguous=True
    if len(d):
        expected=list(range(int(d.draw_no.min()),int(d.draw_no.max())+1)); contiguous=d.draw_no.tolist()==expected
    return {'draws':int(len(d)), 'min_draw':int(d.draw_no.min()) if len(d) else None,
            'max_draw':int(d.draw_no.max()) if len(d) else None, 'contiguous':bool(contiguous),
            'complete_from_draw1':bool(len(d) and int(d.draw_no.min())==1 and contiguous),
            'latest_date':str(d.draw_date.max().date()) if len(d) else None,
            'has_prize_data':all(c in d.columns for c in PRIZE_COLUMNS)}


def _dig(obj,keys):
    if isinstance(obj,dict):
        for k,v in obj.items():
            if k in keys:return v
            f=_dig(v,keys)
            if f is not None:return f
    elif isinstance(obj,list):
        for v in obj:
            f=_dig(v,keys)
            if f is not None:return f
    return None


def _parse_official_json(payload:dict, requested_draw:int|None=None)->dict:
    draw=_dig(payload,{'ltEpsd','drwNo','drawNo','round','lottoEpsd'})
    date=_dig(payload,{'ltRflYmd','drwNoDate','drawDate','lottoDate','epsdRflYmd'})
    bonus=_dig(payload,{'bnusNo','bonusNo','ltBnusNo','bonus'})
    nums=[]
    for i in range(1,7):
        v=_dig(payload,{f'drwtNo{i}',f'lottoNo{i}',f'ltWinNo{i}',f'winNo{i}'})
        if v is not None: nums.append(int(v))
    if len(nums)!=6:
        seq=_dig(payload,{'lotto645WinNo','winNoList','winningNumbers','lottoNos','numbers'})
        if isinstance(seq,str): nums=[int(x) for x in re.findall(r'\d+',seq) if 1<=int(x)<=45][:6]
        elif isinstance(seq,list): nums=[int(x) for x in seq][:6]
    if draw is None: draw=requested_draw
    if draw is None or date is None or bonus is None or len(nums)!=6:
        raise ValueError('Unsupported official JSON response shape')
    nums=sorted(nums)
    return {'draw_no':int(draw),'draw_date':str(date)[:10],**{f'n{i}':n for i,n in enumerate(nums,1)},'bonus':int(bonus)}


def fetch_official_draw(draw_no:int,timeout:int=12)->dict:
    errors=[]; s=_session(); s.headers['Referer']='https://www.dhlottery.co.kr/lt645/result'
    for template in OFFICIAL_JSON_URLS:
        try:
            r=s.get(template.format(draw_no=draw_no),timeout=timeout); r.raise_for_status()
            return _parse_official_json(r.json(),draw_no)
        except Exception as e: errors.append(f'{template}: {e}')
    raise RuntimeError('Official draw fetch failed: '+' | '.join(errors))


def _mirror_row(x:dict)->dict:
    nums=sorted(int(n) for n in x['numbers'])
    row={'draw_no':int(x['draw_no']),'draw_date':str(x['date'])[:10],
         **{f'n{i}':n for i,n in enumerate(nums,1)},'bonus':int(x['bonus_no'])}
    divisions=x.get('divisions') or []
    for i in range(1,6):
        if i<=len(divisions):
            row[f'prize_{i}']=divisions[i-1].get('prize'); row[f'winners_{i}']=divisions[i-1].get('winners')
    if 'total_sales_amount' in x: row['total_sales_amount']=x.get('total_sales_amount')
    wc=x.get('winners_combination') or {}
    row['auto_winners']=wc.get('auto'); row['semi_auto_winners']=wc.get('semi_auto'); row['manual_winners']=wc.get('manual')
    return row




def discover_official_latest(timeout:int=12)->int|None:
    """Best-effort latest draw discovery from the official result page."""
    try:
        r=_session().get(OFFICIAL_RESULT_URL,timeout=timeout); r.raise_for_status()
        nums=[int(x) for x in re.findall(r'(\d{1,5})\s*회',r.text)]
        return max(nums) if nums else None
    except Exception:
        return None

def fetch_mirror_latest(timeout:int=15)->dict:
    r=_session().get(MIRROR_LATEST_URL,timeout=timeout); r.raise_for_status(); return _mirror_row(r.json())


def fetch_mirror_all(timeout:int=30)->pd.DataFrame:
    r=_session().get(MIRROR_ALL_URL,timeout=timeout); r.raise_for_status(); payload=r.json()
    return validate(pd.DataFrame([_mirror_row(x) for x in payload]),require_contiguous=True)


def _row_signature(r)->tuple:
    return (str(pd.Timestamp(r.draw_date).date()),)+tuple(int(r[f'n{i}']) for i in range(1,7))+(int(r.bonus),)


def reconcile(existing:pd.DataFrame,remote:pd.DataFrame)->None:
    if not len(existing) or not len(remote):return
    e=validate(existing).set_index('draw_no'); r=validate(remote).set_index('draw_no'); common=e.index.intersection(r.index)
    bad=[int(n) for n in common if _row_signature(e.loc[n])!=_row_signature(r.loc[n])]
    if bad: raise ValueError(f'Data source mismatch on historical draws: {bad[:20]}')
    if int(r.index.max())<int(e.index.max()): raise ValueError('Remote source is older than local history; refusing downgrade.')


def verify_tail_with_official(df:pd.DataFrame,count:int=3)->dict:
    d=validate(df); checked=0; failures=[]; errors=[]
    for n in d.draw_no.tail(min(count,len(d))).tolist():
        try:
            off=fetch_official_draw(int(n)); row=d[d.draw_no==int(n)].iloc[0]
            if _row_signature(row)!=_row_signature(pd.Series(off)): failures.append(int(n))
            checked+=1
        except Exception as e: errors.append(f'{n}: {e}')
    return {'official_checked':checked,'official_mismatches':failures,
            'official_verified':bool(checked and not failures),'official_errors':errors[:3]}


def _atomic_write_csv(df:pd.DataFrame,path:Path)->None:
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix=path.stem+'_',suffix='.tmp',dir=str(path.parent)); os.close(fd)
    try:
        validate(df).to_csv(tmp,index=False,date_format='%Y-%m-%d'); os.replace(tmp,path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)


def save_csv(df:pd.DataFrame,path:str|Path)->None:_atomic_write_csv(df,Path(path))

def load_csv(path:str|Path)->pd.DataFrame:return validate(pd.read_csv(path))


def save_sqlite(df:pd.DataFrame,path:str|Path)->None:
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); feat=add_derived_features(df)
    tmp=p.with_suffix('.tmp.db')
    if tmp.exists(): tmp.unlink()
    with sqlite3.connect(tmp) as conn:
        feat.to_sql('draws',conn,if_exists='replace',index=False)
        conn.execute('CREATE UNIQUE INDEX idx_draw_no ON draws(draw_no)')
    os.replace(tmp,p)


def save_sync_status(status:dict,path:str|Path)->None:
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); tmp=p.with_suffix('.tmp')
    tmp.write_text(json.dumps(status,ensure_ascii=False,indent=2,default=str),encoding='utf-8'); os.replace(tmp,p)


def load_sync_status(path:str|Path)->dict:
    p=Path(path)
    if not p.exists(): return {}
    try:return json.loads(p.read_text(encoding='utf-8'))
    except Exception:return {}


def sync_history(path:str|Path, latest:int|None=None, verify_official_count:int=3)->tuple[pd.DataFrame,dict]:
    """Refresh full history safely.

    v5.6 recovery logic:
    - The public bulk mirror can lag behind the newest locally verified draws.
    - Never downgrade a newer local tail just because the mirror's latest.json is stale.
    - Rebuild the historical body from the bulk mirror, reuse matching local tail
      rows first, and call the official endpoint only for genuinely missing draws.
    """
    p=Path(path); started=pd.Timestamp.now(tz='Asia/Seoul')
    existing=load_csv(p) if p.exists() else pd.DataFrame(columns=BASE_COLUMNS)
    try:
        try:
            latest_meta=fetch_mirror_latest()
            mirror_latest=int(latest_meta['draw_no'])
        except Exception:
            mirror_latest=None

        official_latest=discover_official_latest()
        local_latest=int(existing.draw_no.max()) if len(existing) else None
        discovered=[x for x in (mirror_latest,official_latest,local_latest) if x is not None]
        if not discovered:
            raise RuntimeError('Could not discover latest draw')

        discovered_max=max(discovered)
        target=discovered_max if latest is None else min(int(latest),discovered_max)

        remote=fetch_mirror_all()
        remote=remote[remote.draw_no<=target].copy()
        remote=validate(remote,require_contiguous=True)

        # Reuse already validated local draws beyond the bulk mirror before
        # attempting network calls. This is essential when the mirror lags.
        current_max=int(remote.draw_no.max()) if len(remote) else 0
        if len(existing) and current_max < target:
            local_tail=existing[(existing.draw_no>current_max)&(existing.draw_no<=target)].copy()
            if len(local_tail):
                expected_start=current_max+1
                local_tail=local_tail.sort_values('draw_no')
                contiguous_local=local_tail.draw_no.astype(int).tolist()
                expected_local=list(range(expected_start, int(local_tail.draw_no.max())+1))
                if contiguous_local==expected_local:
                    remote=pd.concat([remote,local_tail],ignore_index=True)
                    remote=validate(remote,require_contiguous=True)
                    current_max=int(remote.draw_no.max())

        # Fetch only draws still missing after mirror + local-tail recovery.
        if current_max < target:
            rows=[]
            for draw_no in range(current_max+1,target+1):
                rows.append(fetch_official_draw(draw_no))
            if rows:
                remote=pd.concat([remote,pd.DataFrame(rows)],ignore_index=True)
            remote=validate(remote,require_contiguous=True)

        if not len(remote) or int(remote.draw_no.min())!=1 or int(remote.draw_no.max())!=target:
            got_min=int(remote.draw_no.min()) if len(remote) else None
            got_max=int(remote.draw_no.max()) if len(remote) else None
            raise ValueError(
                f'Remote history incomplete: 1..{target} expected, '
                f'got {got_min}..{got_max}'
            )

        reconcile(existing,remote)
        official=verify_tail_with_official(remote,count=verify_official_count)
        if official['official_mismatches']:
            raise ValueError(f'Official verification mismatch: {official["official_mismatches"]}')

        save_csv(remote,p)
        status={
            'ok':True,'synced_at':str(started),
            'source':'mirror_full + local_tail + official_missing_bridge',
            'local_before':local_latest,
            'latest_remote':target,
            'mirror_latest':mirror_latest,
            'official_latest_discovered':official_latest,
            **dataset_status(remote),**official
        }
        return remote,status
    except Exception as ex:
        if len(existing):
            status={
                'ok':False,'synced_at':str(started),'error':str(ex),
                'using_cached_data':True,**dataset_status(existing)
            }
            return validate(existing),status
        raise

def add_derived_features(df:pd.DataFrame)->pd.DataFrame:
    from itertools import combinations
    out=validate(df); feats=[]
    for _,r in out.iterrows():
        nums=[int(r[f'n{i}']) for i in range(1,7)]; gaps=[b-a for a,b in zip(nums,nums[1:])]
        buckets=[sum(lo<=n<=hi for n in nums) for lo,hi in [(1,10),(11,20),(21,30),(31,40),(41,45)]]
        endings=[n%10 for n in nums]; same=sum(1 for a,b in combinations(endings,2) if a==b)
        ac=len({abs(a-b) for a,b in combinations(nums,2)})-5
        feats.append({'sum':sum(nums),'odd_count':sum(n%2 for n in nums),'even_count':sum(n%2==0 for n in nums),
                      'low_count':sum(n<=22 for n in nums),'high_count':sum(n>=23 for n in nums),'range':max(nums)-min(nums),
                      'consecutive_pairs':sum(b-a==1 for a,b in zip(nums,nums[1:])), 'mean_gap':sum(gaps)/5,
                      'max_gap':max(gaps),'same_ending_pairs':same,'ac_value':ac,
                      **{f'bucket_{i+1}':v for i,v in enumerate(buckets)}})
    return pd.concat([out.reset_index(drop=True),pd.DataFrame(feats)],axis=1)


def sync_incremental_official(path:str|Path, max_new:int=3, timeout:int=5)->tuple[pd.DataFrame,dict]:
    """Best-effort incremental update from the official endpoint.

    Checks local_max+1, then continues while valid new draws exist.
    Any network/unavailable-next-draw condition is non-fatal.
    """
    p=Path(path)
    df=load_csv(p)
    before=int(df.draw_no.max()) if len(df) else 0
    added=[]
    error=None
    for _ in range(max_new):
        nxt=int(df.draw_no.max())+1 if len(df) else 1
        try:
            row=fetch_official_draw(nxt,timeout=timeout)
            one=validate(pd.DataFrame([row]))
            if int(one.iloc[0].draw_no)!=nxt:
                break
            df=pd.concat([df,one],ignore_index=True)
            df=validate(df)
            added.append(nxt)
        except Exception as e:
            error=str(e)
            break
    if added:
        save_csv(df,p)
    return df,{
        'ok':True,'local_before':before,'local_after':int(df.draw_no.max()) if len(df) else 0,
        'added_draws':added,'incremental_error':error
    }
