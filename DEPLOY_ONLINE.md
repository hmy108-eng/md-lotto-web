# MD LOTTO 6/45 v3.1 ONLINE 배포 가이드

## 가장 쉬운 방법: Streamlit Community Cloud
1. 이 폴더 전체를 GitHub 저장소(repository)의 루트에 업로드합니다.
2. Streamlit Community Cloud에 GitHub 계정으로 로그인합니다.
3. **Create app** → 해당 저장소와 branch를 선택합니다.
4. Main file path는 `app.py`로 지정합니다.
5. Deploy를 누릅니다.
6. 배포가 끝나면 `https://원하는이름.streamlit.app` 형태의 URL로 PC/Android/iPhone에서 접속합니다.

`requirements.txt`와 `.streamlit/config.toml`은 이미 포함되어 있습니다.

## Render 배포
이 저장소에는 `Dockerfile`과 `render.yaml`도 포함되어 있습니다.
Render에서 새 Blueprint/Web Service를 만들고 GitHub 저장소를 연결하면 Docker 방식으로 실행할 수 있습니다.

## 온라인 데이터 동기화
- 서버 프로세스가 시작되면 첫 접속에서 최신 전체 회차를 확인합니다.
- 이후 30분 TTL 동안 모든 방문자가 같은 동기화 결과를 공유합니다.
- TTL 경과 뒤 첫 페이지 실행이 최신 회차를 다시 검사합니다.
- 사이드바의 **지금 다시 동기화** 버튼으로 즉시 강제 갱신할 수 있습니다.
- 새 데이터는 전체 회차 연속성, 과거 번호 불변성, 최신 endpoint 일치 등을 통과해야 적용됩니다.
- 네트워크/원격 서버 장애 시 현재 검증 캐시를 유지하며 최신 확인 실패 경고를 표시합니다.

## 클라우드 파일 저장에 관한 주의
무료 클라우드의 로컬 파일시스템은 영구 저장소가 아닐 수 있습니다. 이 앱은 이를 전제로 설계되어, 재시작 시에도 원격 전체 이력을 다시 동기화합니다. 즉 CSV/SQLite는 실행 캐시이며 원본 진실(source of truth)로 간주하지 않습니다.

## 모바일 사용
스마트폰에는 Python이나 `.bat` 파일을 설치할 필요가 없습니다. 배포 URL을 Chrome/Safari에서 열면 됩니다. 브라우저 메뉴의 **홈 화면에 추가**를 사용하면 앱 아이콘처럼 실행할 수 있습니다.
