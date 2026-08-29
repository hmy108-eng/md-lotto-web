# MD LOTTO v3.8 MOBILE FIT + VIVID GLOSSBALL - FINAL
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
nums=[int(latest[f'n{i}']) for i in range(1,7)]; bonus=int(latest.bonus)

st.markdown('<div class="hero-shell"><div class="brand-row"><div class="brand-target">🎯</div><div class="brand-title">MD LOTTO 6/45 <span class="v36-badge">v3.8 FIT+GLOSS</span></div></div><div class="brand-sub">과거 데이터·확률·조합 최적화를 연구하는 개인용 분석 도구</div></div>',unsafe_allow_html=True)
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
