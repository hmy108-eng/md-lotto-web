# MD LOTTO 6/45 v3.0 FINAL

개인용 확률·통계·조합설계 연구 도구입니다. **당첨번호 예언 프로그램이 아닙니다.** 공정한 6/45에서 모든 특정 6개 조합의 1등 확률은 동일합니다.

## 가장 쉬운 실행
Windows에서 `start_md_lotto.bat`를 더블클릭합니다.

실행할 때마다 다음 순서를 자동 수행합니다.
1. Python 가상환경/패키지 확인
2. 온라인 최신 회차 및 1회~최신 전체 당첨 이력 동기화 시도
3. 과거 데이터 충돌·누락·중복·번호 오류 검사
4. CSV와 SQLite를 원자적으로 갱신
5. 회귀/무결성 테스트 실행
6. 검증 통과 후 Streamlit 웹앱 실행

인터넷/원격 데이터 소스 장애 시 기존 검증 CSV를 삭제하거나 덮어쓰지 않습니다. 앱에는 최신 동기화 실패 상태가 표시됩니다.

## v3.0 핵심
- Startup automatic full-history sync
- Historical conflict / downgrade protection
- Official recent-draw best-effort cross-check
- Atomic CSV/SQLite replacement
- Number/Gap/Structure audits
- Pair 990 + Triple 14,190 binomial tests with Benjamini-Hochberg FDR
- Genuine pair/triple/quad coverage optimizer
- Bonus-aware Monte Carlo + confidence intervals
- Walk-forward with repeated diversified-random baselines
- Nested walk-forward weight selection
- Strategy Tournament under matched constraints
- Strict walk-forward ML with constant 6/45 probability baseline
- Historical actual-prize ROI backtest when prize data are available

## 해석 규칙
MD Score, Hot/Cold, Gap, Pair/Triple 빈도는 당첨확률이 아닙니다. Backtest 결과가 좋아도 미래 성능을 보장하지 않습니다.

---

## v3.1 ONLINE 배포판 추가사항

이 패키지는 v3.0 FINAL 분석 엔진을 그대로 포함하면서 온라인 배포를 지원합니다.

- Streamlit Community Cloud: `app.py` + `requirements.txt` + `.streamlit/config.toml`
- Render/Docker: `Dockerfile` + `render.yaml`
- 모바일 반응형 UI 보정
- 서버 공용 30분 데이터 동기화 캐시
- 수동 즉시 동기화 버튼
- 클라우드 재시작/임시 파일시스템을 고려한 전체 이력 재복원

자세한 온라인 배포 절차는 `DEPLOY_ONLINE.md`를 확인하세요.
