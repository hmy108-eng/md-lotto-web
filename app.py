# MD LOTTO v3.9 AUTO-SYNC FIX - MOBILE WEB FINAL
# Upload only this file and requirements.txt to GitHub/Streamlit Community Cloud.
import base64 as _b64, zlib as _zlib, json as _json, tempfile as _tempfile, sys as _sys
from pathlib import Path as _Path
_EMBEDDED = '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'
_RUNTIME = _Path(_tempfile.gettempdir()) / "md_lotto_mobile_runtime_v35_fast"
_marker = _RUNTIME / ".ready"
if not _marker.exists():
    _RUNTIME.mkdir(parents=True, exist_ok=True)
    _files = _json.loads(_zlib.decompress(_b64.b64decode(_EMBEDDED)).decode("utf-8"))
    for _rel, _txt in _files.items():
        _p = _RUNTIME / _rel
        _p.parent.mkdir(parents=True, exist_ok=True)
        _p.write_text(_txt, encoding="utf-8")
    _marker.write_text("v3.1", encoding="utf-8")
_sys.path.insert(0, str(_RUNTIME))
import os as _os
_os.environ.setdefault("MD_LOTTO_DATA_DIR", str(_RUNTIME / "data"))

from pathlib import Path
import os, threading, time
import pandas as pd
import streamlit as st
import plotly.express as px
from md_lotto.data import load_csv,sync_history,save_sqlite,dataset_status,save_sync_status,load_sync_status
from md_lotto.data import ensure_latest_draw
from md_lotto.stats import number_stats,pair_stats,triple_stats,structure_summary,randomness_audit,fdr_summary
from md_lotto.optimizer import optimize_games
from md_lotto.backtest import walk_forward,summarize_backtest,nested_walk_forward,strategy_tournament
from md_lotto.simulation import monte_carlo,theoretical_single_game
from md_lotto.ml import train_evaluate,walk_forward_ml

st.set_page_config(page_title='MD LOTTO 6/45', page_icon='🎯', layout='wide', initial_sidebar_state='collapsed')
ROOT=Path(__file__).parent
DATA_DIR=Path(os.getenv('MD_LOTTO_DATA_DIR', str(ROOT/'data')))
DATA_DIR.mkdir(parents=True,exist_ok=True)
path=DATA_DIR/'lotto_history.csv'; db=DATA_DIR/'lotto.db'; sp=DATA_DIR/'sync_status.json'
bundled=ROOT/'data'/'lotto_history.csv'
if not path.exists() and bundled.exists() and bundled.resolve()!=path.resolve(): path.write_bytes(bundled.read_bytes())
_SYNC_LOCK=threading.Lock()

st.markdown(r"""
<style>
:root{--bg:#050814;--panel:#0a1020;--line:#1d2b46;--muted:#98a4b8;--blue:#1687ff;--green:#28d06f;--red:#ff4f6d;--violet:#9c5cff;--gold:#ffcc33}
html,body,[class*="css"]{font-family:Inter,Pretendard,"Noto Sans KR",system-ui,-apple-system,sans-serif}
.stApp{background:radial-gradient(circle at 15% 0%,rgba(22,135,255,.12),transparent 28%),radial-gradient(circle at 88% 15%,rgba(156,92,255,.10),transparent 26%),linear-gradient(180deg,#050814 0%,#070b15 100%);color:#f5f7fb}
.block-container{max-width:1120px;padding-top:.45rem;padding-bottom:6.2rem}[data-testid="stHeader"]{background:transparent}#MainMenu,footer{visibility:hidden}
.hero-shell{position:relative;overflow:hidden;padding:1.2rem 1.25rem 1.05rem;border-radius:24px;background:linear-gradient(135deg,rgba(29,12,28,.96),rgba(7,14,31,.96));border:1px solid #263556;box-shadow:0 18px 42px rgba(0,0,0,.35),inset 0 1px 0 rgba(255,255,255,.05);margin:.2rem 0 1rem}
.hero-shell:before{content:"";position:absolute;inset:-40% 35% 35% -20%;background:radial-gradient(circle,rgba(255,60,110,.22),transparent 60%);pointer-events:none}.brand-row{display:flex;align-items:center;gap:.75rem;position:relative;z-index:1}
.brand-target{width:56px;height:56px;border-radius:50%;display:grid;place-items:center;font-size:2rem;background:radial-gradient(circle,#fff 0 12%,#e53b49 13% 27%,#fff 28% 40%,#c80f21 41% 59%,#650713 60% 100%);box-shadow:0 7px 20px rgba(255,50,80,.32),inset 0 0 0 2px rgba(255,255,255,.55)}
.brand-title{font-size:clamp(1.8rem,5vw,2.55rem);font-weight:1000;letter-spacing:-.045em;line-height:1;background:linear-gradient(180deg,#fff,#eef1f7 56%,#b8beca);-webkit-background-clip:text;color:transparent;text-shadow:0 8px 20px rgba(0,0,0,.24)}.brand-sub{position:relative;z-index:1;color:#aeb8c9;margin:.65rem 0 0;font-size:.93rem}
.sync-ok,.sync-warn{display:flex;align-items:center;gap:.75rem;padding:.78rem .92rem;border-radius:16px;margin:.45rem 0 1rem;font-weight:750}.sync-ok{background:linear-gradient(90deg,rgba(18,82,50,.44),rgba(6,27,25,.72));border:1px solid rgba(45,214,112,.38)}.sync-warn{background:linear-gradient(90deg,rgba(104,62,11,.38),rgba(40,26,8,.70));border:1px solid rgba(255,180,55,.38)}.sync-icon{font-size:1.25rem}.sync-main{font-size:1.02rem}.sync-detail{color:#d7deea;font-weight:550}
.section-head{display:flex;align-items:center;justify-content:space-between;gap:.6rem;margin:1rem 0 .5rem}.section-title{font-size:1.27rem;font-weight:950}.date-chip{font-size:.83rem;color:#b8dcff;padding:.36rem .62rem;border-radius:10px;background:#0b2242;border:1px solid #174d87}
.lotto-row{display:flex;gap:.56rem;flex-wrap:wrap;align-items:center;margin:.55rem 0 1rem;padding:.28rem 0 .9rem;perspective:1000px}.ball{--c1:#FFF06A;--c2:#FFC400;--c3:#9A4E00;position:relative;width:70px;height:70px;flex:0 0 70px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;
background:
radial-gradient(ellipse at 25% 14%,#ffffff 0 4%,rgba(255,255,255,.98) 5% 10%,rgba(255,255,255,.40) 13%,transparent 27%),
radial-gradient(circle at 35% 30%,var(--c1) 0 16%,var(--c2) 46%,var(--c3) 100%);
border:2px solid rgba(255,255,255,.95);
box-shadow:
inset 12px 13px 18px rgba(255,255,255,.52),
inset -15px -18px 24px rgba(0,0,0,.62),
inset 0 0 0 2px rgba(255,255,255,.20),
0 11px 18px rgba(0,0,0,.60);
filter:saturate(1.65) contrast(1.14)}
.ball:before{content:"";position:absolute;left:8%;top:5%;width:52%;height:24%;border-radius:50%;
background:linear-gradient(168deg,#fff 0%,rgba(255,255,255,.98) 30%,rgba(255,255,255,.30) 68%,transparent 100%);
transform:rotate(-23deg);opacity:1;z-index:4;pointer-events:none}.ball:after{content:"";position:absolute;left:13%;right:13%;bottom:-10px;height:12px;border-radius:50%;background:radial-gradient(ellipse,rgba(0,0,0,.72) 0%,rgba(0,0,0,.36) 48%,transparent 78%);filter:blur(4px);z-index:-1;pointer-events:none}
.ball-num{position:relative;z-index:5;display:flex;align-items:center;justify-content:center;width:72%;height:72%;border-radius:50%;
font-size:2.08rem;font-weight:1000;line-height:1;letter-spacing:-.06em;color:#fff;
-webkit-text-stroke:1.6px #06080c;text-shadow:0 3px 2px rgba(0,0,0,.95),0 0 5px rgba(0,0,0,.78);
background:radial-gradient(circle at 40% 28%,rgba(255,255,255,.10),rgba(255,255,255,.01) 48%,rgba(0,0,0,.16) 100%);
box-shadow:inset 0 1px 2px rgba(255,255,255,.25),inset 0 -2px 4px rgba(0,0,0,.30)}
.b1{--c1:#FFF06A;--c2:#FFC400;--c3:#9A4E00}.b2{--c1:#61C8FF;--c2:#0066FF;--c3:#00165E}.b3{--c1:#FF7770;--c2:#F00000;--c3:#650000}.b4{--c1:#FFFFFF;--c2:#AEB4BC;--c3:#30363D}.b5{--c1:#70FF86;--c2:#00B935;--c3:#003D12}.bonus{width:76px;height:76px;flex-basis:76px;box-shadow:inset 10px 12px 18px rgba(255,255,255,.35),inset -14px -18px 23px rgba(0,0,0,.47),0 0 0 3px #ffbd28,0 0 0 6px rgba(255,220,88,.22),0 14px 22px rgba(0,0,0,.48)}.bonus .ball-num{font-size:2.12rem}.bonus-label{font-size:2rem;font-weight:1000;color:#eef2f8;margin:0 .08rem;text-shadow:0 3px 5px #000}
.legend{display:flex;gap:.9rem;flex-wrap:wrap;padding:.55rem .7rem;border-radius:14px;border:1px solid #1b2a43;background:#090f1b;margin:-.15rem 0 1rem;color:#d5dbe5;font-size:.78rem}.legend span{display:flex;align-items:center;gap:.32rem}.dot{width:11px;height:11px;border-radius:50%}
.kpi-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.65rem;margin:.55rem 0 1rem}.kpi{position:relative;overflow:hidden;border-radius:17px;padding:.82rem .85rem 1rem;border:1px solid #24334e;background:linear-gradient(145deg,#0c1423,#08101c);min-height:112px;box-shadow:0 12px 26px rgba(0,0,0,.22)}.kpi:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 10% 0%,rgba(25,132,255,.18),transparent 45%)}.kpi.purple:before{background:radial-gradient(circle at 10% 0%,rgba(158,77,255,.20),transparent 48%)}.kpi.red:before{background:radial-gradient(circle at 10% 0%,rgba(255,65,106,.20),transparent 48%)}.kpi-label{position:relative;color:#c9d2e1;font-size:.82rem;font-weight:750}.kpi-value{position:relative;font-size:1.75rem;font-weight:950;margin-top:.55rem}.kpi-value.redv{color:#ff5c7a}.kpi-sub{position:relative;font-size:.73rem;color:#7f8ba0;margin-top:.12rem}
.menu-title{font-size:1.15rem;font-weight:950;margin:.5rem 0 .55rem}.menu-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:.55rem;margin-bottom:1rem}.menu-card{border:1px solid #243450;border-radius:15px;padding:.75rem .55rem;text-align:center;background:linear-gradient(160deg,#0d1728,#08111f);box-shadow:0 10px 24px rgba(0,0,0,.22)}.menu-card.blue{border-color:#155aa4;background:linear-gradient(160deg,#0c315f,#07182d)}.menu-card.green{border-color:#2e6f31;background:linear-gradient(160deg,#153b18,#08190d)}.menu-card.orange{border-color:#8b5117;background:linear-gradient(160deg,#4b270d,#1b1006)}.menu-card.violet{border-color:#67318b;background:linear-gradient(160deg,#351449,#16091f)}.menu-icon{font-size:1.55rem}.menu-name{font-weight:900;margin-top:.25rem}.menu-desc{font-size:.68rem;color:#bac4d4;margin-top:.15rem}
[data-testid="stMetric"]{border:1px solid #24334e!important;border-radius:15px!important;background:linear-gradient(145deg,#0c1423,#08101c)!important;padding:.75rem!important;box-shadow:0 10px 22px rgba(0,0,0,.18)}[data-testid="stMetricLabel"]{color:#aeb8c8}[data-testid="stMetricValue"]{color:#f7f9fc}.stButton>button{border-radius:12px!important;font-weight:800!important;border:1px solid #2b4772!important;background:linear-gradient(180deg,#123f73,#0b284b)!important;color:#fff!important;min-height:2.7rem}.stButton>button:hover{border-color:#41a1ff!important;box-shadow:0 8px 20px rgba(15,115,220,.22)!important}
[data-baseweb="tab-list"]{gap:.25rem;background:#070d17;border:1px solid #1c2940;padding:.34rem;border-radius:14px;overflow-x:auto}button[data-baseweb="tab"]{height:2.65rem;border-radius:10px;padding:0 .8rem;color:#95a1b4;font-weight:800;white-space:nowrap}button[data-baseweb="tab"][aria-selected="true"]{color:#38a9ff;background:linear-gradient(180deg,#102f57,#0a1b34);box-shadow:inset 0 0 0 1px #235e99}
.game-card{padding:.72rem;border:1px solid #22314c;border-radius:16px;margin:.55rem 0;background:linear-gradient(145deg,#0c1423,#080f1a);box-shadow:0 10px 24px rgba(0,0,0,.19)}.game-title{font-weight:900;margin-bottom:.2rem;color:#dfe7f3}.md-score{color:#ff617f}.small-note{font-size:.78rem;color:#8490a3}.game-card .lotto-row{margin:.4rem 0 .55rem;padding-bottom:.55rem}
@media(max-width:768px){.block-container{padding-left:.66rem;padding-right:.66rem;padding-top:.3rem;padding-bottom:6.5rem}.hero-shell{padding:1rem .9rem;border-radius:21px}.brand-target{width:48px;height:48px;font-size:1.65rem}.brand-title{font-size:1.72rem}.brand-sub{font-size:.82rem}.section-title{font-size:1.12rem}.date-chip{font-size:.72rem}.lotto-row{gap:.38rem;flex-wrap:nowrap}.ball{width:53px;height:53px;flex-basis:53px}.ball-num{width:74%;height:74%;font-size:1.60rem;-webkit-text-stroke:1.15px rgba(3,6,12,.94)}.bonus{width:59px;height:59px;flex-basis:59px}.bonus .ball-num{font-size:1.72rem}.bonus-label{font-size:1.55rem}.legend{gap:.55rem;font-size:.67rem;padding:.48rem .52rem}.dot{width:9px;height:9px}.kpi-grid{gap:.45rem}.kpi{min-height:101px;padding:.72rem .62rem}.kpi-label{font-size:.72rem}.kpi-value{font-size:1.48rem}.kpi-sub{font-size:.65rem}.menu-grid{gap:.4rem}.menu-card{padding:.64rem .35rem}.menu-icon{font-size:1.35rem}.menu-name{font-size:.82rem}.menu-desc{font-size:.60rem}.game-card .ball{width:43px;height:43px;flex-basis:43px}.game-card .ball-num{font-size:1.31rem}.game-card .lotto-row{gap:.25rem;flex-wrap:nowrap}.game-title{font-size:.9rem}[data-testid="stMetric"]{padding:.6rem!important}h2{font-size:1.25rem!important}h3{font-size:1.06rem!important}div[data-testid="stDataFrame"]{font-size:.76rem}}
@media(max-width:390px){.ball{width:50px;height:50px;flex-basis:50px}.ball-num{font-size:1.52rem}.lotto-row{gap:.29rem}.bonus{width:56px;height:56px;flex-basis:56px}.bonus .ball-num{font-size:1.64rem}.kpi-value{font-size:1.36rem}.game-card .ball{width:40px;height:40px;flex-basis:40px}.game-card .ball-num{font-size:1.21rem}}
.v36-badge{display:inline-block;margin-left:.42rem;padding:.14rem .40rem;border-radius:999px;background:#FFD000;color:#111;font-size:.68rem;font-weight:1000;vertical-align:middle}

/* ===== v3.8 MOBILE ONE-ROW FIT + VIVID GLOSSBALL OVERRIDE ===== */
@media (max-width: 640px){
  .lotto-row{
    display:flex!important;
    flex-wrap:nowrap!important;
    width:100%!important;
    max-width:100%!important;
    gap:4px!important;
    justify-content:space-between!important;
    align-items:center!important;
    overflow:visible!important;
    padding:.28rem 0 .72rem!important;
    margin:.45rem 0 .75rem!important;
  }
  .lotto-row>.ball{
    width:calc((100% - 20px)/6)!important;
    height:auto!important;
    aspect-ratio:1/1!important;
    max-width:50px!important;
    min-width:0!important;
    flex:0 1 calc((100% - 20px)/6)!important;
    box-sizing:border-box!important;
    border-width:2px!important;
  }
  .lotto-row>.ball .ball-num{
    width:76%!important;
    height:76%!important;
    font-size:clamp(1.35rem,6.1vw,1.72rem)!important;
    -webkit-text-stroke:1.25px #06080c!important;
  }
  .lotto-row>.bonus{
    width:calc((100% - 24px)/7)!important;
    max-width:46px!important;
    flex-basis:calc((100% - 24px)/7)!important;
  }
  .bonus-label{
    font-size:1.2rem!important;
    margin:0!important;
  }
}
@media (max-width: 390px){
  .lotto-row{gap:3px!important}
  .lotto-row>.ball{
    width:calc((100% - 15px)/6)!important;
    max-width:47px!important;
    flex-basis:calc((100% - 15px)/6)!important;
  }
  .lotto-row>.ball .ball-num{
    font-size:clamp(1.28rem,5.8vw,1.58rem)!important;
  }
}
/* Remove muted filter effects from the balls only */
.ball.b1,.ball.b2,.ball.b3,.ball.b4,.ball.b5{
  filter:saturate(1.75) contrast(1.15)!important;
}
</style>
""",unsafe_allow_html=True)

def ball_class(n): return 'b1' if n<=10 else 'b2' if n<=20 else 'b3' if n<=30 else 'b4' if n<=40 else 'b5'
def balls_html(nums,bonus=None):
    parts=[f'<span class="ball {ball_class(int(n))}"><span class="ball-num">{int(n)}</span></span>' for n in nums]
    if bonus is not None: parts += ['<span class="bonus-label">+</span>',f'<span class="ball {ball_class(int(bonus))} bonus"><span class="ball-num">{int(bonus)}</span></span>']
    return '<div class="lotto-row">'+''.join(parts)+'</div>'
def pct(v,d=2):
    try:return f'{float(v)*100:.{d}f}%'
    except:return '-'
def render_backtest_summary(s):
    c=st.columns(4); c[0].metric('테스트 회차',f"{int(s.get('tests',0)):,}"); c[1].metric('MD 평균 최고 적중',f"{s.get('md_best_mean',0):.2f}개"); c[2].metric('랜덤 평균 최고 적중',f"{s.get('random_div_best_mean',0):.2f}개"); c[3].metric('우위 근거','있음' if s.get('evidence_of_edge') else '없음')
    st.caption(f"승 {s.get('head_to_head_wins',0)} · 패 {s.get('losses',0)} · 무 {s.get('ties',0)} · Sign test p={s.get('sign_test_p_value',1):.4f}")
    if 'md_realized_roi' in s:
        a,b,c=st.columns(3); a.metric('총 구매비',f"₩{s.get('md_total_cost',0):,.0f}"); b.metric('과거 지급액',f"₩{s.get('md_total_payout',0):,.0f}"); c.metric('과거 ROI',pct(s.get('md_realized_roi',0),1))

@st.cache_data(ttl=1800,show_spinner=False)
def cloud_sync_tick(_bucket):
    with _SYNC_LOCK:
        try:
            d,ss=sync_history(path,verify_official_count=3); save_sqlite(d,db); save_sync_status(ss,sp); return ss
        except Exception as e:return {'ok':False,'error':str(e),'using_cached_data':path.exists()}

@st.cache_data(show_spinner=False, max_entries=10)
def cached_mobile_backtest(latest_draw, tests):
    _df=load_csv(path)
    return walk_forward(_df,start_train=300,max_tests=tests,sample_combos=1500,random_reps=50)

@st.cache_data(show_spinner=False, max_entries=8)
def cached_mobile_ml_holdout(latest_draw):
    return train_evaluate(load_csv(path))

@st.cache_data(show_spinner=False, max_entries=8)
def cached_mobile_ml_walk_forward(latest_draw, tests):
    return walk_forward_ml(load_csv(path),start_train=300,max_tests=tests)

# SAFE BOOT: render immediately from embedded/validated local history.
# External sync is manual so a slow/blocked network can never leave the app blank.
if not path.exists():
    st.error('내장 데이터 파일을 준비하지 못했습니다. 앱을 다시 배포해 주세요.')
    st.stop()
df=load_csv(path)
status=dataset_status(df)
ns=number_stats(df)
latest=df.iloc[-1]
ss=load_sync_status(sp) or {'ok': True, 'using_cached_data': True, 'safe_boot': True}
st.session_state.setdefault('startup_sync_status', ss)

# v3.9: one short latest-draw check per session; failure never blocks the UI.
if not st.session_state.get('_latest_draw_checked_v39'):
    st.session_state['_latest_draw_checked_v39']=True
    try:
        _quick=ensure_latest_draw(path, timeout=4)
        st.session_state['latest_draw_quick_status']=_quick
        if _quick.get('updated'):
            st.rerun()
    except Exception as _e:
        st.session_state['latest_draw_quick_status']={'ok':False,'error':str(_e)}
nums=[int(latest[f'n{i}']) for i in range(1,7)]; bonus=int(latest.bonus)

st.markdown('<div class="hero-shell"><div class="brand-row"><div class="brand-target">🎯</div><div class="brand-title">MD LOTTO 6/45 <span class="v36-badge">v3.9 AUTO-SYNC</span></div></div><div class="brand-sub">과거 데이터·확률·조합 최적화를 연구하는 개인용 분석 도구</div></div>',unsafe_allow_html=True)
if ss.get('ok'): st.markdown(f'<div class="sync-ok"><span class="sync-icon">✅</span><span class="sync-main">데이터 정상</span><span class="sync-detail">· 1회 ~ {status.get("max_draw")}회 · 검증 데이터 즉시 로드</span></div>',unsafe_allow_html=True)
else: st.markdown('<div class="sync-warn"><span class="sync-icon">⚠️</span><span class="sync-main">온라인 최신 확인 실패</span><span class="sync-detail">· 마지막 검증 데이터를 사용 중입니다.</span></div>',unsafe_allow_html=True)
st.markdown(f'<div class="section-head"><div class="section-title">🏆 제 {int(latest.draw_no)}회 최신 당첨번호</div><div class="date-chip">추첨일 {latest.draw_date.strftime("%Y-%m-%d")}</div></div>',unsafe_allow_html=True)
st.markdown(balls_html(nums,bonus),unsafe_allow_html=True)
st.markdown('<div class="legend"><span><i class="dot" style="background:#f2b400"></i>1-10</span><span><i class="dot" style="background:#1687ff"></i>11-20</span><span><i class="dot" style="background:#ed3547"></i>21-30</span><span><i class="dot" style="background:#9da2aa"></i>31-40</span><span><i class="dot" style="background:#38b44b"></i>41-45</span><span><i class="dot" style="background:#ed3547"></i>보너스</span></div>',unsafe_allow_html=True)
st.markdown(f'<div class="kpi-grid"><div class="kpi"><div class="kpi-label">📊 분석 회차</div><div class="kpi-value">{len(df):,}</div><div class="kpi-sub">총 분석 데이터</div></div><div class="kpi purple"><div class="kpi-label">🗓️ 최신 회차</div><div class="kpi-value">{int(latest.draw_no)}회</div><div class="kpi-sub">가장 최근 회차</div></div><div class="kpi red"><div class="kpi-label">📅 최신 추첨일</div><div class="kpi-value redv" style="font-size:1.28rem">{latest.draw_date.strftime("%Y-%m-%d")}</div><div class="kpi-sub">자동 동기화 기준</div></div></div>',unsafe_allow_html=True)
st.markdown('<div class="menu-title">✨ 주요 분석 메뉴</div><div class="menu-grid"><div class="menu-card blue"><div class="menu-icon">🎲</div><div class="menu-name">번호 추천</div><div class="menu-desc">최적 번호 조합</div></div><div class="menu-card green"><div class="menu-icon">📊</div><div class="menu-name">FDR 분석</div><div class="menu-desc">패턴·확률 검증</div></div><div class="menu-card orange"><div class="menu-icon">🎯</div><div class="menu-name">백테스트</div><div class="menu-desc">과거 성과 검증</div></div><div class="menu-card violet"><div class="menu-icon">🧠</div><div class="menu-name">AI 진단</div><div class="menu-desc">종합 인사이트</div></div></div>',unsafe_allow_html=True)

with st.sidebar:
    st.header('데이터 관리'); st.success(f"최신 {status.get('max_draw')}회까지 확인") if ss.get('ok') else st.warning('온라인 최신 확인 실패'); st.caption('누락 없음' if status.get('complete_from_draw1') else '일부 회차 누락 가능')
    if st.button('🔄 지금 최신 데이터 확인',use_container_width=True):
        with st.spinner('온라인 최신 데이터를 확인하는 중입니다...'):
            _done=False
            try:
                _q=ensure_latest_draw(path, timeout=8)
                st.session_state['latest_draw_quick_status']=_q
                _done=bool(_q.get('updated') or (_q.get('ok') and _q.get('remote')==_q.get('local')))
            except Exception as _e:
                st.session_state['latest_draw_quick_status']={'ok':False,'error':str(_e)}
            if not _done:
                cloud_sync_tick.clear()
                st.session_state['startup_sync_status']=cloud_sync_tick(int(time.time()//1800))
        st.rerun()
    st.caption('동기화 실패 시 기존 검증 데이터는 보존됩니다.')
if not status['complete_from_draw1']: st.error(f"현재 데이터가 {status['min_draw']}~{status['max_draw']}회만 있습니다.")

tabs=st.tabs(['🏠 대시보드','🎲 번호 추천','📊 FDR 분석','🏆 백테스트','🧠 AI 진단'])
with tabs[0]:
    st.subheader('데이터·무작위성 진단'); audit=randomness_audit(df); struct=structure_summary(df)
    c=st.columns(4); c[0].metric('전체 회차',f"{status['draws']:,}"); c[1].metric('연속 데이터','정상' if status['contiguous'] else '점검 필요'); c[2].metric('당첨금 데이터','있음' if status.get('has_prize_data') else '없음'); c[3].metric('균등성 검정','특이점 없음' if audit.get('p_value',0)>=.05 else '검토 필요')
    st.caption(f"번호합 평균 {struct.get('sum_mean',0):.1f} · 10~90% 범위 {struct.get('sum_q10',0):.0f}~{struct.get('sum_q90',0):.0f} · 흔한 홀수 개수 {struct.get('odd_mode','-')}개")
    fig=px.bar(ns,x='number',y='count_all',hover_data=['count_20','count_100','current_gap','z_score'],labels={'number':'번호','count_all':'전체 출현'}); fig.update_layout(margin=dict(l=0,r=0,t=15,b=0),height=330,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font_color='#aeb8c8'); st.plotly_chart(fig,use_container_width=True)
with tabs[1]:
    subt=st.tabs(['추천 조합','번호 분석','시뮬레이션'])
    with subt[0]:
        c1,c2=st.columns(2); game_count=c1.slider('게임 수',5,20,5,key='opt_games'); pool=c2.slider('후보 Pool',12,30,20)
        if st.button('🎯 추천 조합 만들기',type='primary',use_container_width=True):
            with st.spinner('조합 최적화 중...'): st.session_state['md_games']=optimize_games(df,ns,games=game_count,pool_size=pool,sample_combos=20000)
        games=st.session_state.get('md_games')
        if games is not None and len(games):
            for i,row in games.iterrows(): st.markdown(f'<div class="game-card"><div class="game-title">GAME {i+1:02d} <span class="md-score">· MD Score {float(row.get("md_score",0)):.1f}</span></div>{balls_html(row.combo)}<div class="small-note">새 Pair {int(row.get("new_pairs",0))} · Triple {int(row.get("new_triples",0))} · Quad {int(row.get("new_quads",0))}</div></div>',unsafe_allow_html=True)
            cov=games.attrs.get('coverage',{}); c=st.columns(3); c[0].metric('고유 Pair',cov.get('unique_pairs',0)); c[1].metric('고유 Triple',cov.get('unique_triples',0)); c[2].metric('고유 Quad',cov.get('unique_quads',0)); st.caption('※ MD Score는 당첨확률이 아닙니다. 모든 특정 6개 조합의 1등 확률은 동일합니다.')
        else: st.info('「추천 조합 만들기」를 누르세요.')
    with subt[1]:
        view=ns[['number','count_all','count_20','count_50','count_100','count_300','current_gap','mean_gap','z_score']].copy(); view.columns=['번호','전체','최근20','최근50','최근100','최근300','현재 미출현','평균 간격','Z-score']; st.dataframe(view,use_container_width=True,hide_index=True); st.caption('Hot/Cold와 Gap은 과거 상태를 설명할 뿐 “나올 차례”를 의미하지 않습니다.')
    with subt[2]:
        sims=st.select_slider('가상 추첨 횟수',[10000,50000,100000,500000],value=100000)
        if st.button('🎲 시뮬레이션 실행',use_container_width=True):
            games=st.session_state.get('md_games'); games=games if games is not None and len(games) else optimize_games(df,ns,games=5,sample_combos=12000)
            with st.spinner(f'{sims:,}회 가상 추첨 중...'): r=monte_carlo(games.combo.tolist(),sims)
            c=st.columns(3); c[0].metric('가상 추첨',f"{r['simulations']:,}회"); c[1].metric('1회 이상 당첨',pct(r['any_prize_probability'],3)); c[2].metric('평균 당첨 티켓',f"{r['mean_winning_tickets']:.4f}")
            labels={'1st':'1등','2nd':'2등','3rd':'3등','4th':'4등','5th':'5등','none':'미당첨'}; st.dataframe(pd.DataFrame([{'최고 결과':labels[k],'확률':pct(v,4)} for k,v in r['best_rank_probability'].items()]),use_container_width=True,hide_index=True)
with tabs[2]:
    st.info('다중 비교 착시를 줄이기 위해 Benjamini–Hochberg FDR 보정을 사용합니다.')
    if st.button('🔬 전체 FDR 검정 실행',use_container_width=True):
        with st.spinner('검정 중...'): f=fdr_summary(df)
        c=st.columns(4); c[0].metric('Pair 검사',f"{f.get('pair_tests',0):,}"); c[1].metric('Pair 유의',f"{f.get('pair_fdr_significant',0):,}"); c[2].metric('Triple 검사',f"{f.get('triple_tests',0):,}"); c[3].metric('Triple 유의',f"{f.get('triple_fdr_significant',0):,}")
    ps=pair_stats(df,with_tests=True).head(50).copy(); ps['번호쌍']=ps.apply(lambda r:f"{int(r.a):02d}-{int(r.b):02d}",axis=1); st.dataframe(ps[['번호쌍','count','expected','lift','fdr_q_value']].rename(columns={'count':'출현','expected':'기대','lift':'배율','fdr_q_value':'FDR q'}),use_container_width=True,hide_index=True)
    ts=triple_stats(df,min_count=2,with_tests=True).head(50).copy(); ts['번호 3개']=ts.apply(lambda r:f"{int(r.a):02d}-{int(r.b):02d}-{int(r.c):02d}",axis=1); st.dataframe(ts[['번호 3개','count','expected','fdr_q_value']].rename(columns={'count':'출현','expected':'기대','fdr_q_value':'FDR q'}),use_container_width=True,hide_index=True)
with tabs[3]:
    btabs=st.tabs(['일반 백테스트','고급 검증','ROI'])
    with btabs[0]:
        tests=st.slider('최근 테스트 회차',10,150,30,10,key='bt_tests')
        if st.button('📈 백테스트 실행',use_container_width=True):
            with st.spinner('검증 중...'): st.session_state['last_bt']=cached_mobile_backtest(int(latest.draw_no),tests)
        bt=st.session_state.get('last_bt');
        if bt is not None and len(bt): render_backtest_summary(summarize_backtest(bt)); st.caption('우위 근거가 없으면 랜덤보다 낫다고 해석하지 않습니다.')
    with btabs[1]:
        mode=st.radio('검증 방식',['Nested Walk-forward','Strategy Tournament'],horizontal=True)
        if mode=='Nested Walk-forward':
            nt=st.slider('Outer 테스트 회차',5,40,12,key='nested_tests')
            if st.button('🧪 Nested 검증 실행',use_container_width=True):
                with st.spinner('검증 중...'): bt=nested_walk_forward(df,start_train=360,max_tests=nt,inner_draws=16,sample_combos=1000,random_reps=60)
                render_backtest_summary(summarize_backtest(bt)); st.dataframe(bt,use_container_width=True,hide_index=True)
        elif st.button('🏁 전략 토너먼트 실행',use_container_width=True):
            with st.spinner('전략 비교 중...'): tour=strategy_tournament(df,start_train=300,max_tests=30,sample_combos=1400)
            st.dataframe(tour,use_container_width=True,hide_index=True)
    with btabs[2]:
        if status.get('has_prize_data'):
            st.info('실제 과거 등위별 당첨금을 이용한 연구용 백테스트입니다. 미래 수익을 보장하지 않습니다.')
            if st.button('💰 ROI 백테스트 실행',use_container_width=True):
                with st.spinner('계산 중...'): bt=walk_forward(df,start_train=300,max_tests=50,sample_combos=1800,random_reps=80)
                render_backtest_summary(summarize_backtest(bt))
        else: st.warning('현재 데이터에 등위별 당첨금 필드가 없습니다.')
        probs=theoretical_single_game(); labels={'1st':'1등','2nd':'2등','3rd':'3등','4th':'4등','5th':'5등'}; st.dataframe(pd.DataFrame([{'등위':labels[k],'확률':pct(v,6),'약 1 / N':f"1 / {round(1/v):,}"} for k,v in probs.items()]),use_container_width=True,hide_index=True)
with tabs[4]:
    st.subheader('AI 진단 · 시간순 검증'); c1,c2=st.columns(2)
    if c1.button('시간순 Holdout',use_container_width=True):
        r=cached_mobile_ml_holdout(int(latest.draw_no))
        if r.get('available'): c=st.columns(3); c[0].metric('AUC',f"{r['roc_auc_out_of_sample']:.3f}"); c[1].metric('Model Log-loss',f"{r['log_loss_out_of_sample']:.4f}"); c[2].metric('기본보다 우수','예' if r['beats_constant_logloss'] else '아니오')
    if c2.button('완전 Walk-forward',use_container_width=True):
        ml_mode=st.radio('AI 검증 속도',['빠른 진단 (10회)','정밀 진단 (30회)'],horizontal=True,key='ml_speed_mobile')
        ml_tests=10 if ml_mode.startswith('빠른') else 30
        with st.spinner(f'회차별 재학습 중... ({ml_tests}회)'): r=cached_mobile_ml_walk_forward(int(latest.draw_no),ml_tests)
        if r.get('available'): rows=r.pop('rows',[]); c=st.columns(3); c[0].metric('테스트',r['tests']); c[1].metric('평균 AUC',f"{r['mean_auc']:.3f}"); c[2].metric('평균 Top6 적중',f"{r['mean_top6_hits']:.2f}개"); st.caption(f"평균 Log-loss {r['mean_log_loss']:.4f} · 기본 {r['mean_baseline_log_loss']:.4f}")
    st.markdown('---'); st.markdown('**사용 원칙**\n- AI가 기본 확률보다 실제로 좋아지는지 검증하는 연구 기능입니다.\n- 결과가 좋지 않으면 AI 예측 신호로 사용하지 않습니다.\n- MD Score는 당첨확률이 아닙니다.')
st.caption('MD LOTTO 6/45 · Mobile Premium Final UI · 모든 특정 6개 조합의 1등 확률은 동일합니다.')
