# MD LOTTO v4.2 TOP10 FOCUS - DETERMINISTIC RANKING FINAL
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
from md_lotto.optimizer import optimize_games, deterministic_top_games
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

st.markdown('<div class="hero-shell"><div class="brand-row"><div class="brand-target">🎯</div><div class="brand-title">MD LOTTO 6/45 <span class="v36-badge">v4.2 TOP10 FOCUS</span></div></div><div class="brand-sub">과거 데이터·확률·조합 최적화를 연구하는 개인용 분석 도구</div></div>',unsafe_allow_html=True)
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
        st.info('선택과 집중 모드: 후보 Pool 20개에서 가능한 38,760개 조합을 전수 평가해 무작위 샘플링 없이 상위 10조합만 제시합니다.')
        if st.button('🎯 TOP 10 집중 추천 만들기',type='primary',use_container_width=True):
            with st.spinner('38,760개 조합을 전수 평가해 상위 10조합을 선정하는 중...'):
                st.session_state['md_games']=deterministic_top_games(df,ns,games=10,pool_size=20,max_overlap=5)
                st.session_state['md_recommendation_record']={
                    'target_draw':int(latest.draw_no)+1,
                    'created_from_draw':int(latest.draw_no),
                    'games':[list(map(int,c)) for c in st.session_state['md_games'].combo.tolist()],
                    'mode':'TOP10_FOCUS_DETERMINISTIC'
                }
        games=st.session_state.get('md_games')
        if games is not None and len(games):
            for i,row in games.iterrows():
                st.markdown(
                    f'<div class="game-card"><div class="game-title">RANK {int(row.get("rank",i+1)):02d} '
                    f'<span class="md-score">· MD Score {float(row.get("md_score",0)):.1f} · 집중지수 {float(row.get("focus_index",0)):.1f}</span></div>'
                    f'{balls_html(row.combo)}'
                    f'<div class="small-note">구조 {float(row.get("structural",0)):.1f} · 번호신호 {float(row.get("number_signal",0)):.1f} · Pair 안정성 {float(row.get("pair_stability",0)):.1f}</div></div>',
                    unsafe_allow_html=True
                )
            st.caption(f"전수평가 조합 수: {int(games.attrs.get('evaluated_combinations',0)):,}개 · 무작위 샘플링 없음")
            st.caption('※ RANK와 MD Score는 실제 당첨확률 순위가 아닙니다. 공정한 로또에서는 모든 특정 6개 조합의 1등 확률은 동일합니다.')
        else: st.info('「추천 조합 만들기」를 누르세요.')
    with subt[1]:
        view=ns[['number','count_all','count_20','count_50','count_100','count_300','current_gap','mean_gap','z_score']].copy(); view.columns=['번호','전체','최근20','최근50','최근100','최근300','현재 미출현','평균 간격','Z-score']; st.dataframe(view,use_container_width=True,hide_index=True); st.caption('Hot/Cold와 Gap은 과거 상태를 설명할 뿐 “나올 차례”를 의미하지 않습니다.')
    with subt[2]:
        sims=st.select_slider('가상 추첨 횟수',[10000,50000,100000,500000],value=100000)
        if st.button('🎲 시뮬레이션 실행',use_container_width=True):
            games=st.session_state.get('md_games'); games=games if games is not None and len(games) else deterministic_top_games(df,ns,games=10,pool_size=20,max_overlap=5)
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
