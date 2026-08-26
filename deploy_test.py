from pathlib import Path
import ast
root=Path(__file__).resolve().parents[1]
required=['app.py','requirements.txt','Dockerfile','render.yaml','.streamlit/config.toml','DEPLOY_ONLINE.md']
missing=[x for x in required if not (root/x).exists()]
assert not missing, missing
ast.parse((root/'app.py').read_text(encoding='utf-8'))
app=(root/'app.py').read_text(encoding='utf-8')
assert 'cloud_sync_tick' in app
assert 'ttl=1800' in app
assert '지금 다시 동기화' in app
assert 'MD_LOTTO_DATA_DIR' in app
docker=(root/'Dockerfile').read_text(encoding='utf-8')
assert '${PORT:-10000}' in docker and '/_stcore/health' in docker
print('DEPLOY TEST OK')
