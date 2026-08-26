from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px
from md_lotto.data import load_csv,sync_history,save_sqlite,dataset_status,save_sync_status,load_sync_status
from md_lotto.stats import number_stats,pair_stats,triple_stats,structure_summary,randomness_audit,fdr_summary
from md_lotto.optimizer import optimize_games
from md_lotto.backtest import walk_forward,summarize_backtest,nested_walk_forward,strategy_tournament
from md_lotto.simulation import monte_carlo,theoretical_single_game
from md_lotto.ml import train_evaluate,walk_forward_ml

st.set_page_config(page_title='MD LOTTO 6/45 v3.0 FINAL',page_icon='🎯',layout='wide')
ROOT=Path(__file__).parent; path=ROOT/'data'/'lotto_history.csv'; db=ROOT/'data'/'lotto.db'; sp=ROOT/'data'/'sync_status.json'
st.title('MD LOTTO 6/45 v3.0 FINAL')
st.caption('통계·조합 최적화 연구 도구입니다. 모든 특정 6개 조합의 1등 추첨확률은 동일하며 MD Score는 당첨확률(%)이 아닙니다.')

# Exactly once per Streamlit session: every program launch attempts a fresh online sync.
if 'startup_sync_done' not in st.session_state:
    try:
        with st.spinner('시작 시 최신 당첨 데이터 자동 동기화 중...'):
            d,ss=sync_history(path,verify_official_count=3); save_sqlite(d,db); save_sync_status(ss,sp)
        st.session_state['startup_sync_status']=ss
    except Exception as e:
        st.session_state['startup_sync_status']={'ok':False,'error':str(e),'using_cached_data':path.exists()}
    st.session_state['startup_sync_done']=True

with st.sidebar:
    st.header('데이터 상태')
    ss=st.session_state.get('startup_sync_status') or load_sync_status(sp)
    if ss.get('ok'): st.success(f"자동 동기화 완료 · 최신 {ss.get('max_draw',ss.get('latest_remote'))}회")
    else: st.warning('온라인 최신 확인 실패 · 검증된 로컬 캐시 사용 중')
    if ss.get('official_verified'): st.caption(f"최근 {ss.get('official_checked')}회 공식 교차확인 통과")
    elif ss.get('ok'): st.caption('공식 JSON 교차확인은 응답 제한 등으로 생략될 수 있습니다.')
    if st.button('지금 다시 동기화'):
        try:
            with st.spinner('동기화 중...'):
                d,ss=sync_history(path,verify_official_count=3); save_sqlite(d,db); save_sync_status(ss,sp)
            st.session_state['startup_sync_status']=ss; st.success(f"{len(d)}회 저장 완료"); st.rerun()
        except Exception as e: st.error(str(e))

if not path.exists(): st.error('데이터 파일이 없습니다. 인터넷 연결 후 update_data.py를 실행하세요.'); st.stop()
df=load_csv(path); status=dataset_status(df); ns=number_stats(df); latest=df.iloc[-1]
if not status['complete_from_draw1']: st.error(f"PARTIAL DATA: {status['min_draw']}~{status['max_draw']}회만 있습니다. 전체 동기화 전 연구 결과를 실전 판단에 사용하지 마세요.")
a,b,c,d=st.columns(4); a.metric('분석 회차',f'{len(df):,}'); b.metric('최신 회차',f'{int(latest.draw_no)}회'); c.metric('최신 추첨일',latest.draw_date.strftime('%Y-%m-%d')); d.metric('1등 확률','1 / 8,145,060')

tabs=st.tabs(['대시보드','번호 Lab','FDR Pair/Triple','MD Optimizer','Monte Carlo','Backtest','Nested Tune','Strategy Tournament','ML Lab','ROI/EV','사용법'])
with tabs[0]:
    st.subheader('데이터·무작위성 진단'); st.json({**status,**structure_summary(df),**randomness_audit(df)})
    fig=px.bar(ns,x='number',y='count_all',hover_data=['count_20','count_100','current_gap','z_score']); st.plotly_chart(fig,use_container_width=True)
with tabs[1]: st.dataframe(ns,use_container_width=True,hide_index=True)
with tabs[2]:
    st.info('990개 Pair와 14,190개 Triple에 Benjamini–Hochberg FDR 보정을 적용합니다. 유의성은 예측력이 아니라 과거 데이터 감사용입니다.')
    if st.button('FDR 전체 검정 실행'):
        with st.spinner('14,190개 Triple 검정 중...'): st.json(fdr_summary(df))
    ps=pair_stats(df,with_tests=True); st.subheader('Pair 상위 관측'); st.dataframe(ps.head(100),use_container_width=True,hide_index=True)
    ts=triple_stats(df,min_count=2,with_tests=True); st.subheader('반복 Triple'); st.dataframe(ts.head(100),use_container_width=True,hide_index=True)
with tabs[3]:
    game_count=st.slider('게임 수',5,20,10,key='opt_games'); pool=st.slider('후보 Pool 크기',12,30,20)
    games=optimize_games(df,ns,games=game_count,pool_size=pool,sample_combos=20000)
    show=games.copy(); show['combo']=show.combo.apply(lambda x:' · '.join(f'{n:02d}' for n in x)); st.dataframe(show,use_container_width=True,hide_index=True)
    st.json({'coverage':games.attrs.get('coverage',{}),'candidate_pool':games.attrs.get('pool',[])})
with tabs[4]:
    games=optimize_games(df,ns,games=10,sample_combos=12000); sims=st.select_slider('시뮬레이션',[10000,50000,100000,500000],value=100000)
    if st.button('Monte Carlo 실행'):
        r=monte_carlo(games.combo.tolist(),sims); st.json(r); st.caption('Monte Carlo는 전략의 구조적 분포를 확인하는 도구이며 미래 번호를 예측하지 않습니다.')
with tabs[5]:
    tests=st.slider('최근 테스트 회차',10,150,30,10,key='bt_tests')
    if st.button('표준 Walk-forward 실행'):
        if len(df)<320: st.error('최소 320회 이상 필요')
        else:
            with st.spinner('검증 중...'): bt=walk_forward(df,start_train=300,max_tests=tests,sample_combos=2500,random_reps=100)
            st.json(summarize_backtest(bt)); st.dataframe(bt,use_container_width=True,hide_index=True)
with tabs[6]:
    st.write('각 외부 테스트 회차 직전에 과거 데이터 안에서만 가중치를 선택하는 Nested Walk-forward입니다. 가장 엄격하고 계산량이 많습니다.')
    nt=st.slider('Outer 테스트 회차',5,40,12,key='nested_tests')
    if st.button('Nested Walk-forward 실행'):
        with st.spinner('내부 튜닝 + 외부 검증 중...'):
            bt=nested_walk_forward(df,start_train=360,max_tests=nt,inner_draws=16,sample_combos=1000,random_reps=60)
        st.json(summarize_backtest(bt)); st.dataframe(bt,use_container_width=True,hide_index=True)
with tabs[7]:
    st.write('미리 선언한 전략들을 동일 회차·동일 게임 수·동일 overlap 조건으로 비교합니다.')
    if st.button('Strategy Tournament 실행'):
        with st.spinner('전략 토너먼트 중...'): tour=strategy_tournament(df,start_train=300,max_tests=30,sample_combos=1400)
        st.dataframe(tour,use_container_width=True,hide_index=True)
with tabs[8]:
    if st.button('ML 시간순 Holdout'): st.json(train_evaluate(df))
    if st.button('ML 완전 Walk-forward'):
        with st.spinner('회차별 재학습 중...'): r=walk_forward_ml(df,start_train=300,max_tests=30)
        rows=r.pop('rows',[]); st.json(r); st.dataframe(pd.DataFrame(rows),use_container_width=True,hide_index=True)
with tabs[9]:
    st.subheader('실제 과거 당첨금 기반 ROI 연구')
    if status.get('has_prize_data'):
        st.write('과거 각 회차의 실제 등위별 1게임당 당첨금으로 백테스트 지급액을 계산합니다. 세금·구매행동·미수령 등은 반영하지 않습니다.')
        if st.button('ROI 백테스트 실행'):
            with st.spinner('ROI 계산 중...'): bt=walk_forward(df,start_train=300,max_tests=50,sample_combos=1800,random_reps=80)
            st.json(summarize_backtest(bt)); cols=[c for c in ['draw_no','md_cost','md_payout','md_roi','random_div_payout_mean','random_div_roi_mean'] if c in bt]; st.dataframe(bt[cols],use_container_width=True,hide_index=True)
    else: st.warning('현재 로컬 데이터에는 등위별 당첨금 필드가 없습니다. 최신 전체 데이터 동기화 후 활성화됩니다.')
    st.subheader('이론적 단일게임 확률'); st.json(theoretical_single_game())
with tabs[10]:
    st.markdown('''### v3.0 권장 사용 순서
1. 실행 시 **자동 최신 데이터 동기화 상태** 확인
2. 데이터/무작위성/FDR 감사
3. 표준 Backtest → Strategy Tournament → Nested Walk-forward
4. ML은 반드시 Walk-forward 기준선과 비교
5. Optimizer와 Monte Carlo는 마지막에 조합 묶음을 구성·검토하는 용도로 사용

**중요:** 과거 데이터에서 우위가 보여도 미래 당첨확률 상승을 보장하지 않습니다. 네트워크 장애 시 앱은 검증된 로컬 데이터를 보존하며 최신 확인 실패를 표시합니다.''')
