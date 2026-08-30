# MD LOTTO v4.1 CORRELATION + REGRESSION DIAGNOSTICS - MOBILE WEB FINAL
# Upload only this file and requirements.txt to GitHub/Streamlit Community Cloud.
import base64 as _b64, zlib as _zlib, json as _json, tempfile as _tempfile, sys as _sys
from pathlib import Path as _Path
_EMBEDDED = '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'
_RUNTIME = _Path(_tempfile.gettempdir()) / "md_lotto_mobile_runtime_v40_datafix"
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
from md_lotto.data import sync_incremental_official
from md_lotto.stats import number_stats,pair_stats,triple_stats,structure_summary,randomness_audit,fdr_summary
from md_lotto.optimizer import optimize_games
from md_lotto.backtest import walk_forward,summarize_backtest,nested_walk_forward,strategy_tournament
from md_lotto.simulation import monte_carlo,theoretical_single_game
from md_lotto.ml import train_evaluate,walk_forward_ml
from md_lotto.diagnostics import recommendation_actual_diagnostics

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

@st.cache_data(show_spinner=False, max_entries=6)
def cached_recommendation_diagnostics(latest_draw, tests, games, sample_combos):
    _df=load_csv(path)
    return recommendation_actual_diagnostics(
        _df,start_train=300,max_tests=tests,games=games,
        sample_combos=sample_combos,pool_size=20,max_overlap=3
    )

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

# v4.0 DATA RECOVERY:
# 1) On a fresh runtime, restore full 1..latest history when possible.
# 2) Then check official local_max+1 for newly published draws.
if not st.session_state.get('_full_history_checked_v40'):
    st.session_state['_full_history_checked_v40']=True
    if len(df) and int(df.draw_no.min())>1:
        try:
            with st.spinner('전체 회차 데이터를 복구·동기화하는 중입니다...'):
                df,_full_status=sync_history(path,verify_official_count=2)
                st.session_state['startup_sync_status']=_full_status
        except Exception as _e:
            st.session_state['startup_sync_status']={'ok':False,'error':str(_e),'using_cached_data':True}

if not st.session_state.get('_official_incremental_checked_v40'):
    st.session_state['_official_incremental_checked_v40']=True
    try:
        df,_inc_status=sync_incremental_official(path,max_new=3,timeout=5)
        st.session_state['incremental_sync_status']=_inc_status
    except Exception as _e:
        st.session_state['incremental_sync_status']={'ok':False,'error':str(_e)}

df=load_csv(path)
status=dataset_status(df)
ns=number_stats(df)
latest=df.iloc[-1]
ss=st.session_state.get('startup_sync_status') or load_sync_status(sp) or {'ok':True,'using_cached_data':True}
nums=[int(latest[f'n{i}']) for i in range(1,7)]; bonus=int(latest.bonus)

st.markdown('<div class="hero-shell"><div class="brand-row"><div class="brand-target">🎯</div><div class="brand-title">MD LOTTO 6/45 <span class="v36-badge">v4.1 CORR+REG</span></div></div><div class="brand-sub">과거 데이터·확률·조합 최적화를 연구하는 개인용 분석 도구</div></div>',unsafe_allow_html=True)
if ss.get('ok'): st.markdown(f'<div class="sync-ok"><span class="sync-icon">✅</span><span class="sync-main">데이터 정상</span><span class="sync-detail">· 1회 ~ {status.get("max_draw")}회 · 자동 최신회차 확인</span></div>',unsafe_allow_html=True)
else: st.markdown('<div class="sync-warn"><span class="sync-icon">⚠️</span><span class="sync-main">온라인 최신 확인 실패</span><span class="sync-detail">· 마지막 검증 데이터를 사용 중입니다.</span></div>',unsafe_allow_html=True)
st.markdown(f'<div class="section-head"><div class="section-title">🏆 제 {int(latest.draw_no)}회 최신 당첨번호</div><div class="date-chip">추첨일 {latest.draw_date.strftime("%Y-%m-%d")}</div></div>',unsafe_allow_html=True)
st.markdown(balls_html(nums,bonus),unsafe_allow_html=True)
st.markdown('<div class="legend"><span><i class="dot" style="background:#f2b400"></i>1-10</span><span><i class="dot" style="background:#1687ff"></i>11-20</span><span><i class="dot" style="background:#ed3547"></i>21-30</span><span><i class="dot" style="background:#9da2aa"></i>31-40</span><span><i class="dot" style="background:#38b44b"></i>41-45</span><span><i class="dot" style="background:#ed3547"></i>보너스</span></div>',unsafe_allow_html=True)
st.markdown(f'<div class="kpi-grid"><div class="kpi"><div class="kpi-label">📊 분석 회차</div><div class="kpi-value">{len(df):,}</div><div class="kpi-sub">총 분석 데이터</div></div><div class="kpi purple"><div class="kpi-label">🗓️ 최신 회차</div><div class="kpi-value">{int(latest.draw_no)}회</div><div class="kpi-sub">가장 최근 회차</div></div><div class="kpi red"><div class="kpi-label">📅 최신 추첨일</div><div class="kpi-value redv" style="font-size:1.28rem">{latest.draw_date.strftime("%Y-%m-%d")}</div><div class="kpi-sub">자동 동기화 기준</div></div></div>',unsafe_allow_html=True)
st.markdown('<div class="menu-title">✨ 주요 분석 메뉴</div><div class="menu-grid"><div class="menu-card blue"><div class="menu-icon">🎲</div><div class="menu-name">번호 추천</div><div class="menu-desc">최적 번호 조합</div></div><div class="menu-card green"><div class="menu-icon">📊</div><div class="menu-name">FDR 분석</div><div class="menu-desc">패턴·확률 검증</div></div><div class="menu-card orange"><div class="menu-icon">🎯</div><div class="menu-name">백테스트</div><div class="menu-desc">과거 성과 검증</div></div><div class="menu-card violet"><div class="menu-icon">🧠</div><div class="menu-name">AI 진단</div><div class="menu-desc">종합 인사이트</div></div></div>',unsafe_allow_html=True)

with st.sidebar:
    st.header('데이터 관리'); st.success(f"최신 {status.get('max_draw')}회까지 확인") if ss.get('ok') else st.warning('온라인 최신 확인 실패'); st.caption('누락 없음' if status.get('complete_from_draw1') else '일부 회차 누락 가능')
    if st.button('🔄 지금 최신 데이터 확인',use_container_width=True):
        with st.spinner('전체 회차와 최신 회차를 확인하는 중입니다...'):
            try:
                _df,_st=sync_history(path,verify_official_count=2)
                st.session_state['startup_sync_status']=_st
                _df,_inc=sync_incremental_official(path,max_new=3,timeout=6)
                st.session_state['incremental_sync_status']=_inc
            except Exception as _e:
                st.session_state['startup_sync_status']={'ok':False,'error':str(_e),'using_cached_data':True}
        st.rerun()
    st.caption('동기화 실패 시 기존 검증 데이터는 보존됩니다.')
if not status['complete_from_draw1']: st.error(f"현재 데이터가 {status['min_draw']}~{status['max_draw']}회만 있습니다.")

tabs=st.tabs(['🏠 대시보드','🎲 번호 추천','📊 FDR 분석','🏆 백테스트','🧠 AI 진단','🔎 오차 진단'])
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
            with st.spinner('조합 최적화 중...'):
                st.session_state['md_games']=optimize_games(df,ns,games=game_count,pool_size=pool,sample_combos=20000)
                st.session_state['md_recommendation_record']={
                    'target_draw':int(latest.draw_no)+1,
                    'created_from_draw':int(latest.draw_no),
                    'games':[list(map(int,c)) for c in st.session_state['md_games'].combo.tolist()]
                }
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

with tabs[5]:
    st.subheader('추천번호 ↔ 실제 당첨번호 · 상관/회귀 오차 진단')
    st.info('과거 각 회차 직전 데이터만으로 추천을 다시 생성한 뒤 실제 당첨번호와 비교합니다. 상관계수와 회귀계수는 원인 진단용이며 당첨확률 자체를 의미하지 않습니다.')

    dc1,dc2=st.columns(2)
    diag_tests=dc1.select_slider('진단 회차',['빠른 10회','표준 20회','정밀 30회'],value='표준 20회')
    diag_games=dc2.select_slider('회차당 추천 게임',[5,7,10],value=5)
    _dt=10 if diag_tests.startswith('빠른') else 20 if diag_tests.startswith('표준') else 30
    _samples=500 if _dt==10 else 800 if _dt==20 else 1000

    if st.button('🔎 상관·회귀 오차 진단 실행',use_container_width=True,type='primary'):
        with st.spinner(f'{_dt}개 과거 회차를 시간순으로 재생성·비교하는 중...'):
            st.session_state['corr_reg_diag']=cached_recommendation_diagnostics(int(latest.draw_no),_dt,diag_games,_samples)

    dr=st.session_state.get('corr_reg_diag')
    if dr and dr.get('available'):
        c=st.columns(4)
        _nc=dr.get('number_exposure_vs_win_corr')
        c[0].metric('진단 회차',f"{dr.get('tests',0)}회")
        c[1].metric('추천노출↔당첨 상관','-' if pd.isna(_nc) else f"{_nc:+.3f}")
        c[2].metric('평균 최고 적중',f"{dr.get('mean_best_hits',0):.2f}개")
        c[3].metric('평균 총 적중',f"{dr.get('mean_total_hits',0):.2f}개")

        if pd.notna(_nc):
            if abs(_nc)<.10:
                st.warning('추천 노출과 실제 당첨의 상관이 매우 약합니다. 현재 자료만으로 예측 우위를 주장할 근거가 부족합니다.')
            elif _nc>0:
                st.success('양(+)의 상관이 관찰됐지만, 표본 밖 Walk-forward와 랜덤 기준을 함께 통과해야 신호로 취급할 수 있습니다.')
            else:
                st.warning('음(-)의 상관이 관찰됐습니다. 현재 추천 가중치를 강화하면 안 됩니다.')

        st.markdown('#### 원인 분석 · 실제 구조와 추천 구조의 차이')
        mc=dr.get('mismatch_correlations',{})
        _names={'abs_gap_sum':'번호합 차이','abs_gap_odd':'홀짝 차이','abs_gap_low':'저·고번호 차이','abs_gap_range':'번호범위 차이','abs_gap_buckets':'구간분산 차이'}
        mdf=pd.DataFrame([{'요인':_names.get(k,k),'적중과 상관':v} for k,v in mc.items() if pd.notna(v)])
        if len(mdf):
            mdf['적중과 상관']=mdf['적중과 상관'].map(lambda x:f"{x:+.3f}")
            st.dataframe(mdf,use_container_width=True,hide_index=True)

        mr=dr.get('mismatch_regression',{})
        pr=dr.get('pre_regression',{})
        rc=st.columns(2)
        rc[0].metric('구조차이 회귀 R²','-' if not mr.get('available') else f"{mr.get('r2',0):.3f}")
        rc[1].metric('사전점수 회귀 R²','-' if not pr.get('available') else f"{pr.get('r2',0):.3f}")
        st.caption('R²가 낮으면 현재 변수들이 적중 차이를 충분히 설명하지 못한다는 뜻입니다. 높은 R²도 미래 예측력을 자동으로 의미하지 않습니다.')

        st.markdown('#### 프로그램이 제시하는 원인과 대책')
        for x in dr.get('causes',[]):
            st.markdown(f"**• {x['factor']}** · 상관 {x['correlation']:+.3f}\n\n→ {x['action']}")
        weak=dr.get('weak_signals',[])
        if weak:
            st.markdown('**가중치 점검 필요 항목**')
            for x in weak[:4]:
                st.caption(f"• {x['factor']} ({x['correlation']:+.3f}) → {x['action']}")

        st.markdown('#### 회차별 진단 원자료')
        raw=dr.get('rows')
        if raw is not None and len(raw):
            show=raw[['draw_no','best_hits','total_hits','avg_md_score','abs_gap_sum','abs_gap_odd','abs_gap_low','abs_gap_range']].copy()
            show.columns=['회차','최고 적중','총 적중','평균 MD Score','번호합 차이','홀짝 차이','저·고 차이','범위 차이']
            st.dataframe(show.sort_values('회차',ascending=False),use_container_width=True,hide_index=True)

    rec=st.session_state.get('md_recommendation_record')
    if rec:
        td=int(rec.get('target_draw',0))
        if td<=int(latest.draw_no) and td in set(df.draw_no.astype(int)):
            rr=df[df.draw_no.astype(int)==td].iloc[-1]
            win={int(rr[f'n{i}']) for i in range(1,7)}
            hs=[len(set(g)&win) for g in rec.get('games',[])]
            st.markdown('#### 이번 세션에서 저장된 추천 ↔ 실제 결과')
            st.write(f"대상 {td}회 · 최고 적중 {max(hs) if hs else 0}개 · 전체 게임 적중 합 {sum(hs)}개")
        else:
            st.caption(f"현재 세션 추천 기록: {td}회 대상 · 실제 추첨 후 이 탭에서 바로 비교할 수 있습니다.")

    st.markdown('---')
    st.caption('해석 원칙: 상관관계는 인과관계가 아닙니다. 회귀분석은 과거 오차를 설명하는 도구이며, 가중치 변경은 반드시 Nested Walk-forward와 랜덤 기준 비교를 통과한 경우에만 적용합니다.')


st.caption('MD LOTTO 6/45 · Mobile Premium Final UI · 모든 특정 6개 조합의 1등 확률은 동일합니다.')
