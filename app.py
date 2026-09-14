# MD LOTTO v8.3 GITHUB DEPLOY - SPLIT FILE STRUCTURE
# Upload only this file and requirements.txt to GitHub/Streamlit Community Cloud.
import base64 as _b64, zlib as _zlib, json as _json, tempfile as _tempfile, sys as _sys
from pathlib import Path as _Path
import base64 as _b64, zlib as _zlib, json as _json, tempfile as _tempfile, sys as _sys
from pathlib import Path as _Path
_ROOT = _Path(__file__).resolve().parent
_RUNTIME = _ROOT
if str(_ROOT) not in _sys.path:
    _sys.path.insert(0, str(_ROOT))
import streamlit as st
MD_BUILD_ID = 'MD-LOTTO-v8.0-20260913-2135-KST'
import plotly.express as px
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from md_lotto.data import load_csv,sync_history,save_sqlite,dataset_status,save_sync_status,load_sync_status
from md_lotto.data import sync_incremental_official
from md_lotto.stats import number_stats,pair_stats,triple_stats,structure_summary,randomness_audit,fdr_summary
from md_lotto.optimizer import optimize_games, deterministic_top_games
from md_lotto.backtest import walk_forward,summarize_backtest,nested_walk_forward,strategy_tournament
from md_lotto.simulation import monte_carlo,theoretical_single_game,optimize_five_portfolio,converge_min_miss_portfolio
from md_lotto.ml import train_evaluate,walk_forward_ml
from md_lotto.diagnostics import recommendation_actual_diagnostics
from md_lotto.transitions import latest_transition_report, next_draw_adjustment_report, adaptive_priority_five, corrected_candidate_games
from md_lotto.learning import record_recommendation,evaluate_pending,learning_summary,learning_profile,rerank_with_learning,load_learning_log
from md_lotto.evolution import evolutionary_weekly_plan
from md_lotto.evolution_report import evolution_report

st.set_page_config(page_title='MD LOTTO 6/45', page_icon='🎯', layout='wide', initial_sidebar_state='collapsed')
ROOT=Path(__file__).parent
DATA_DIR=Path(os.getenv('MD_LOTTO_DATA_DIR', str(ROOT/'data')))
DATA_DIR.mkdir(parents=True,exist_ok=True)
path=DATA_DIR/'lotto_history.csv'; db=DATA_DIR/'lotto.db'; sp=DATA_DIR/'sync_status.json'
learning_path=DATA_DIR/'md_lotto_learning_log.json'
bundled=ROOT/'data'/'lotto_history.csv'
embedded_bundled=_RUNTIME/'data'/'lotto_history.csv'
if not path.exists():
    _seed_source=None
    if bundled.exists() and bundled.resolve()!=path.resolve():
        _seed_source=bundled
    elif embedded_bundled.exists() and embedded_bundled.resolve()!=path.resolve():
        _seed_source=embedded_bundled
    if _seed_source is not None:
        path.write_bytes(_seed_source.read_bytes())
# v8.1 migration: an existing v8.0 installation may still contain only
# draws 1219~1241. Merge the embedded full history into that cache while
# preserving any newer locally synced draws and all separate learning logs.
if path.exists() and embedded_bundled.exists() and path.resolve()!=embedded_bundled.resolve():
    try:
        _local_history=load_csv(path)
        _embedded_history=load_csv(embedded_bundled)
        _local_status=dataset_status(_local_history)
        if (not _local_status.get('complete_from_draw1')) or len(_local_history)<len(_embedded_history):
            _merged_history=pd.concat([_embedded_history,_local_history],ignore_index=True)
            _merged_history=_merged_history.sort_values('draw_no').drop_duplicates('draw_no',keep='last')
            _merged_history.to_csv(path,index=False,date_format='%Y-%m-%d')
            load_csv(path)  # fail fast if the migrated cache is invalid
    except Exception:
        # The UI below will show DATA CHECK instead of hiding a migration error.
        pass
_SYNC_LOCK=threading.Lock()

st.markdown(r"""
<style>
:root{--navy:#020d20;--navy2:#061a34;--gold:#d9ae4a;--gold2:#f1d178;--text:#f8fafc;--muted:#9caec3;--line:rgba(220,177,73,.36)}
html,body,[class*="css"]{font-family:"Noto Sans KR","Malgun Gothic","Apple SD Gothic Neo",sans-serif}
.stApp{color:var(--text);background:radial-gradient(circle at 50% -12%,rgba(34,91,161,.22),transparent 32%),linear-gradient(180deg,#010815 0%,#06162c 52%,#010815 100%)!important}
.block-container{max-width:1220px!important;padding:.55rem .9rem 3.6rem!important}
#MainMenu,footer,[data-testid="stHeader"]{visibility:hidden!important}
.signature-banner{overflow:hidden;border:3px solid var(--gold);border-radius:22px;margin:.1rem 0 .7rem;background:#021026;box-shadow:0 18px 48px rgba(0,0,0,.40),inset 0 0 0 1px rgba(255,236,172,.17)}
.signature-banner img{display:block;width:100%;height:auto}
.cmd-status{display:grid;grid-template-columns:1.35fr 1fr 1fr 1fr;gap:.55rem;padding:.55rem;border:1px solid var(--line);border-radius:18px;background:linear-gradient(180deg,#04142b,#020d1f);box-shadow:0 12px 30px rgba(0,0,0,.24)}
.cmd-stat{padding:.72rem .78rem;border:1px solid rgba(220,177,73,.20);border-radius:14px;background:linear-gradient(145deg,#08213f,#031128)}
.cmd-stat .lab{font-size:.65rem;font-weight:900;letter-spacing:.06em;color:#d7b55c}.cmd-stat .val{margin-top:.18rem;font-size:1rem;font-weight:1000;color:#fff}.cmd-stat.live{border-color:rgba(82,226,153,.32)}.cmd-stat.live .val{color:#66e5a5}
.draw-stage{margin:.78rem 0 1rem;padding:1rem 1.05rem 1.15rem;border:2px solid rgba(220,177,73,.64);border-radius:24px;background:linear-gradient(145deg,#071c36,#021025);box-shadow:0 18px 42px rgba(0,0,0,.28)}
.draw-stage-head{display:flex;align-items:flex-end;justify-content:space-between;gap:.8rem;margin-bottom:.35rem}.draw-stage-kicker{font-size:.67rem;font-weight:950;letter-spacing:.14em;color:#e3bd61}.draw-stage-title{font-size:1.42rem;font-weight:1000;letter-spacing:-.035em}.draw-stage-date{padding:.42rem .7rem;border:1px solid #b68d3d;border-radius:999px;background:#071a34;color:#ffe6a4;font-size:.82rem;font-weight:900}
.lotto-row{display:flex;align-items:center;gap:.62rem;flex-wrap:wrap;margin:.55rem 0 .7rem;padding:.25rem 0 .5rem}
.ball{--c1:#fff17e;--c2:#ffd400;--c3:#a36900;position:relative;width:72px;height:72px;flex:0 0 72px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;background:radial-gradient(ellipse at 28% 14%,#fff 0 5%,rgba(255,255,255,.72) 7% 12%,rgba(255,255,255,.12) 17%,transparent 29%),radial-gradient(circle at 34% 29%,var(--c1) 0 17%,var(--c2) 48%,var(--c3) 100%);border:2px solid rgba(255,255,255,.94);box-shadow:inset 10px 12px 16px rgba(255,255,255,.34),inset -15px -18px 22px rgba(0,0,0,.46),0 12px 19px rgba(0,0,0,.52);filter:saturate(1.22) contrast(1.06)}
.ball:before{content:"";position:absolute;left:9%;top:6%;width:48%;height:22%;border-radius:50%;background:linear-gradient(165deg,#fff,rgba(255,255,255,.78) 38%,rgba(255,255,255,.12) 75%,transparent);transform:rotate(-22deg);z-index:4;pointer-events:none}.ball:after{content:"";position:absolute;left:14%;right:14%;bottom:-10px;height:12px;border-radius:50%;background:radial-gradient(ellipse,rgba(0,0,0,.66),rgba(0,0,0,.22) 55%,transparent 78%);filter:blur(4px);z-index:-1}
.ball-num{position:relative;z-index:6;display:flex;align-items:center;justify-content:center;width:64%;height:64%;border-radius:50%;background:radial-gradient(circle at 35% 28%,#fff 0 28%,#fafaf8 58%,#e6e8e9 100%)!important;border:1px solid rgba(220,222,224,.97)!important;box-shadow:inset 3px 4px 6px rgba(255,255,255,.96),inset -4px -5px 7px rgba(0,0,0,.10),0 1px 4px rgba(0,0,0,.18)!important;color:#050505!important;font-size:2rem;font-weight:1000!important;line-height:1;letter-spacing:-.06em;text-shadow:none!important}
.b1{--c1:#fff17e;--c2:#ffd400;--c3:#a36900}.b2{--c1:#70d1ff;--c2:#0f8df5;--c3:#0048a8}.b3{--c1:#ff8b8b;--c2:#f5232c;--c3:#990007}.b4{--c1:#b9bec5;--c2:#484e55;--c3:#15191e}.b5{--c1:#82f59a;--c2:#18b956;--c3:#08702a}.bonus{width:78px;height:78px;flex-basis:78px;box-shadow:inset 10px 12px 16px rgba(255,255,255,.34),inset -15px -18px 22px rgba(0,0,0,.46),0 0 0 3px #e4bd57,0 0 0 6px rgba(228,189,87,.16),0 14px 23px rgba(0,0,0,.48)}.bonus-label{font-size:2rem;font-weight:1000;color:#fff}
.command-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.62rem;margin:.7rem 0 1rem}.command-card{padding:.9rem;border:1px solid rgba(220,177,73,.30);border-radius:19px;background:linear-gradient(145deg,#081b34,#031027);box-shadow:0 13px 30px rgba(0,0,0,.20)}.command-card.hot{border-color:#d5a842;background:linear-gradient(145deg,#102a4e,#07152b)}.command-card .no{font-size:.65rem;font-weight:950;letter-spacing:.11em;color:#e5bf63}.command-card .ttl{margin-top:.2rem;font-size:1.04rem;font-weight:1000}.command-card .txt{margin-top:.18rem;color:#93a6bd;font-size:.75rem;line-height:1.4}
[data-testid="stTabs"] [data-baseweb="tab-list"]{gap:.32rem;padding:.33rem;border:1px solid rgba(220,177,73,.38);border-radius:17px;background:#020d1f!important}[data-testid="stTabs"] button[role="tab"]{min-height:50px!important;padding:.55rem .78rem!important;border-radius:12px!important;font-size:.93rem!important;font-weight:900!important}[data-testid="stTabs"] button[aria-selected="true"]{background:linear-gradient(135deg,#173665,#0c2144)!important;box-shadow:inset 0 -3px 0 #ddb34d!important}
div.stButton>button,div.stDownloadButton>button{min-height:58px!important;border:1px solid #d6ad4b!important;border-radius:16px!important;background:linear-gradient(180deg,#17477f 0%,#0c2e5b 56%,#071f42 100%)!important;color:#fff!important;font-size:1rem!important;font-weight:1000!important;box-shadow:0 12px 28px rgba(0,0,0,.30),inset 0 1px rgba(255,255,255,.15)!important}div.stButton>button:hover,div.stDownloadButton>button:hover{border-color:#f0cf74!important;transform:translateY(-1px);box-shadow:0 15px 34px rgba(0,0,0,.38),0 0 0 2px rgba(224,181,73,.14)!important}
.compact-audit-row{display:grid;grid-template-columns:repeat(3,1fr);gap:.55rem}.compact-audit,.game-card,[data-testid="stMetric"]{padding:.65rem!important;border:1px solid rgba(220,177,73,.20)!important;border-radius:16px!important;background:linear-gradient(145deg,#071a34,#031025)!important;box-shadow:0 11px 26px rgba(0,0,0,.18)!important}.compact-audit span{display:block;color:#9babc0;font-size:.75rem}.compact-audit b{display:block;margin-top:.18rem;color:#fff;font-size:1.25rem}
.final-board{margin:.75rem 0 .9rem;padding:1.15rem;border:1px solid #d5aa45;border-radius:25px;background:linear-gradient(145deg,#071a33,#031025);box-shadow:0 20px 50px rgba(0,0,0,.30)}.final-head{display:flex;align-items:flex-end;justify-content:space-between;gap:.8rem;margin-bottom:.85rem}.final-kicker{color:#e2bb5d;font-size:.68rem;font-weight:950;letter-spacing:.15em}.final-title{font-size:1.5rem;font-weight:1000}.final-draw{padding:.4rem .65rem;border:1px solid #b68d3d;border-radius:999px;color:#ffe39a;font-size:.82rem;font-weight:900}.final-grid{display:grid;grid-template-columns:1fr;gap:.55rem}.final-line{display:grid;grid-template-columns:70px 1fr;align-items:center;padding:.65rem .75rem;border:1px solid rgba(222,181,75,.28);border-radius:17px;background:linear-gradient(90deg,#0b2141,#06152b)}.final-rank{color:#e2bb5d;font-size:.9rem;font-weight:1000}.final-line .lotto-row{margin:0;padding:0;gap:.62rem;flex-wrap:nowrap}.final-line .ball{width:58px;height:58px;min-width:58px}.final-line .ball-num{font-size:1.35rem}
.legend{display:flex;gap:.75rem;flex-wrap:wrap;padding:.58rem .7rem;border:1px solid rgba(220,177,73,.28);border-radius:14px;background:#031026;color:#d9e1ec;font-size:.76rem}.legend span{display:flex;align-items:center;gap:.3rem}.dot{width:11px;height:11px;border-radius:50%}.ops-title{font-size:1rem;font-weight:1000}[data-testid="stExpander"]{border-color:rgba(220,177,73,.22)!important;border-radius:15px!important;background:rgba(4,15,32,.60)!important}
@media(max-width:780px){.block-container{padding:.45rem .65rem 3rem!important}.signature-banner{border-radius:16px}.cmd-status{grid-template-columns:repeat(2,1fr)}.draw-stage-head{align-items:flex-start}.command-grid{grid-template-columns:1fr}.compact-audit-row{grid-template-columns:1fr}.final-line{grid-template-columns:42px 1fr;padding:.56rem .5rem}.final-line .lotto-row{gap:.28rem}.final-line .ball{width:42px;height:42px;min-width:42px}.final-line .ball-num{font-size:.98rem}.ball{width:58px;height:58px;flex-basis:58px}.ball-num{font-size:1.58rem}}
</style>
""",unsafe_allow_html=True)

def ball_class(n): return 'b1' if n<=10 else 'b2' if n<=20 else 'b3' if n<=30 else 'b4' if n<=40 else 'b5'
def balls_html(nums,bonus=None):
    parts=[f'<span class="ball {ball_class(int(n))}"><span class="ball-num">{int(n)}</span></span>' for n in nums]
    if bonus is not None: parts += ['<span class="bonus-label">+</span>',f'<span class="ball {ball_class(int(bonus))} bonus"><span class="ball-num">{int(bonus)}</span></span>']
    return '<div class="lotto-row">'+''.join(parts)+'</div>'

def premium_brand_banner_html():
    return f'<div class="signature-banner"><img src="data:image/png;base64,{_BRAND_BANNER_B64}" alt="MD LOTTO Premium Banner"></div>'

def final_five_board_html(games,target_draw,title='MD LOTTO FINAL 5'):
    rows=[]
    for i,g in enumerate(games,1):
        rows.append(
            f'<div class="final-line"><div class="final-rank">{i}순위</div>{balls_html(g)}</div>'
        )
    return (
        '<div class="final-board">'
        '<div class="final-head"><div><div class="final-kicker">ADAPTIVE CORRECTION · FINAL SELECTION</div>'
        f'<div class="final-title">{title}</div></div>'
        f'<div class="final-draw">제 {int(target_draw)}회</div></div>'
        f'<div class="final-grid">{"".join(rows)}</div></div>'
    )

def _pick_font(size,bold=False):
    # Cloud-safe font resolver.  The old fallback ImageFont.load_default()
    # ignored the requested size on some Pillow/Streamlit environments,
    # which made lotto numbers appear tiny even when the code requested
    # a large font.  Try Korean/system fonts, then font-name lookup, then
    # Pillow's scalable default where supported.
    candidates=[
        '/usr/share/fonts/truetype/nanum/NanumSquareB.ttf' if bold else '/usr/share/fonts/truetype/nanum/NanumSquareR.ttf',
        '/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf' if bold else '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf',
        '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc' if bold else '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
        '/usr/share/fonts/truetype/unfonts-core/UnDotumBold.ttf' if bold else '/usr/share/fonts/truetype/unfonts-core/UnDotum.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
        'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf',
        'LiberationSans-Bold.ttf' if bold else 'LiberationSans-Regular.ttf'
    ]
    for fp in candidates:
        try:
            return ImageFont.truetype(fp,size=int(size))
        except Exception:
            pass
    try:
        return ImageFont.load_default(size=int(size))
    except TypeError:
        return ImageFont.load_default()

def _ball_rgb(n):
    n=int(n)
    if n<=10:return (255,208,0)
    if n<=20:return (22,135,248)
    if n<=30:return (243,38,46)
    if n<=40:return (49,54,60)
    return (32,185,86)

def _draw_signature_ball(d,cx,cy,n,font):
    n=int(n); rgb=_ball_rgb(n); R=56
    # soft oval shadow like the approved reference
    d.ellipse((cx-43,cy+47,cx+43,cy+69),fill=(125,128,132))
    # multi-layer glossy sphere
    dark=tuple(max(0,int(c*.42)) for c in rgb)
    mid=tuple(max(0,min(255,int(c*.78))) for c in rgb)
    light=tuple(max(0,min(255,int(c*1.13+14))) for c in rgb)
    d.ellipse((cx-R,cy-R,cx+R,cy+R),fill=dark,outline=(255,255,255),width=2)
    d.ellipse((cx-R+5,cy-R+4,cx+R-4,cy+R-5),fill=mid)
    d.ellipse((cx-R+11,cy-R+8,cx+R-10,cy+R-11),fill=rgb)
    # large upper-left highlight
    d.ellipse((cx-R+15,cy-R+10,cx-2,cy-13),fill=light)
    d.ellipse((cx-R+22,cy-R+12,cx-17,cy-R+31),fill=(255,255,255))
    # dark lower-right contour
    d.arc((cx-R+4,cy-R+4,cx+R-4,cy+R-4),182,342,fill=dark,width=8)
    # white center disk -- exact approved look
    ir=33
    d.ellipse((cx-ir,cy-ir,cx+ir,cy+ir),fill=(250,250,248),outline=(221,223,225),width=2)
    d.ellipse((cx-ir+6,cy-ir+5,cx+ir-12,cy-ir+18),fill=(255,255,255))
    # Fit the number to the white center disk. Pillow's text bbox includes font
    # bearings, so center using the bbox itself rather than width/height alone.
    s=str(n)
    max_w=int(ir*2*0.94); max_h=int(ir*2*0.90)
    chosen=font; bb=d.textbbox((0,0),s,font=chosen,stroke_width=1)
    # Start from a large font and select the largest size that fits the disk.
    for fs in range(92,23,-1):
        cand=_pick_font(fs,True)
        cb=d.textbbox((0,0),s,font=cand,stroke_width=1)
        if (cb[2]-cb[0])<=max_w and (cb[3]-cb[1])<=max_h:
            chosen,bb=cand,cb
            break
    x=cx-(bb[0]+bb[2])/2
    y=cy-(bb[1]+bb[3])/2
    d.text((x,y),s,font=chosen,fill=(0,0,0),stroke_width=1,stroke_fill=(0,0,0))



# Embedded bold Korean banner glyphs. These are raster glyph images only,
# so mobile/cloud rendering does not depend on server-installed Korean fonts.
_MD_KO_GLYPHS = {'년': 'iVBORw0KGgoAAAANSUhEUgAAAEYAAABICAYAAABLJIP0AAACNElEQVR42u2asWsUQRTGf58XI8FT8cCgKEkKxcYylYWd2NiYTi208C+wTCHY2NjYW4n4JygIggasbSJYWAhqYRRiNJpI4uVZOEJCdt0cd7nb2/0+eEwxy+7Ob+a9N292wbIsy+q7VKXBREQzp2tVUruWMxwRzyNfHyPiYF3BFGm6k/vtcTTJ1kiHs3INOJXT/ULSszou1dMFS3W5rq50oKC/WaWF4BjTixizi24wA9wG9hrMVl0HztiVhsClHWMMxmAqBeaz03W2bgJPu0zXDwe115gu2nO7uvbOt2+zPQVc9c53u+4Al52Vtqt0x46OMQZjMJUCs+50na176V26SdcXKgdG0hww1+3Ot7YxJiJUK1eKiP1AK9lh4AhwAjie2klgAhiPiLuSZocKTEQ84u+PAgIa6f6NFDtGgX3JxpI1E4jRDh4zA8wO24q50ocFNuF9TLbGImLcYLI1aTDZmjKYbC2VKfhu9Hnw34APyd4D75LNS3pTJjCvgcfAyX/ZOcM2gPamdh1Y22S/gBXgZ2qX0+wvAV+BL8ACsCBpZShqJUlrwEVX1z52sAxmgLVSC3gAHMu55ImkW7WjHBGXCr4Gtnfx2aX+EtmoiutWKca8/E/fJ+DtII8dBqlzwKGcvh+SftcSjKToZQ3ldG0wBmMwBmMwBlOvInKnNc2AxroInJf0yitmq1rAWbuSY4zBGEwVwXwv+Xh3/H49/UMpIkaAG8DREkJZBO5LWrU/WJZllVR/ANxvh0OVqsswAAAAAElFTkSuQmCC', '월': 'iVBORw0KGgoAAAANSUhEUgAAAEYAAABICAYAAABLJIP0AAADxElEQVR42u2aT4iVZRTGf+d6c2Rmcq7jvyzEtD8kahAkIrRoIZQRtBARqW1qBIEUtCl3upGgNmmboNDZiAtFKd1YIrQYw0oFy0AqgxRNZpyRRu/wtJg3HIe593vvN9+f997eB87ict97zvc9933Pc875PoiIiIiIKByWl2NJS4BVwOPAw866gVFgGBgCrgAXzezGDGMZcBp4ocGSX4HnzGykcIYl9Ul6XdIhSX+rNVyTNCBpi6S5KWLXPGI8XzQh/ZL2SBpRNrgtabek/rYlRtKrKXaHL25J2loWMZUZkPI+cBSYlxPvNWBA0q62ydiSNqtYvBn8jpG0GPi84P/iY0mPFBkwzVF6G+htYX0duAr8DJwHfnGf6y346AbeCv0YnfPYtt9L2ibpKUmVBn4qkp6WtEPSDx4+B4NWJQ9Z/qgRGU18ViR9kiTjoROThO6UfnuTHLeFXDfBeMrf1UNKGWmIuZPw/c6U1/LeDOOWnnzPe2zb45JeSjpWknokbZT0lYfPH4s8StUU3JwEViesecVZXdLvwJ+uq74LzAZ6gMeAZcAsz7hfh75jlksaK7jyHZO0LOjka2ZXgA8L/j8+MLPf2qVf2lfQbvm0HccO7+Z4rP6RtNPzOoIcVD0h6UtJ9YwIqUv6QtLyMgdVliFBK4BNwGvA+hbz1zjwHXAEOOzy2FT/VWAhsMjZPOC0mf0lqQbcSoix1szOZkqMpK4pa22SVZyZk96K675XA88CK9xN9Lvhk1yVew+4Afwn51VgLtDnrOZ+N99Z3zSXdsLMXs6DmKoHKfuB7YFqwMoyW4INAYvjEvfoJIheKSQ85PJOJGYaPBqJmR5deTittsnNy6nOtSn2EzDo1CxTJCYuSZ8B21q8iTFgjsfaA67rHgVGuP9Mew3wzqR11528N7uPpCPVklz7Fm9dkuY0sS5J1cmzXkkbZjCq3JtDi5H9PMbMxgo+Olb22e2E5BuJicREYhriG0p+KpBnHaPUmdfsGBMDc+95jEd3HQwxg8AZYGmD749nGGvIxWr2Dt6lwmVR0krg27waugzQ8suJWeWYdQGTAvAk8ExUpSjXkZhITKcRc4GJB/Ydg0zqGDM7K2khOQyMWsAfQRZ4ZjbMxKCpFDQZ75RLjKRTwIsxxzxISm8nkRJVKRITiYnEpEmFpaiSB26WSMpl4GKIxIya2YL/XeXrgR5lXYGlw0Eze8OrYM2wjrndBhthyMxqMflGVYrERGI6hZg7rlYIHed8F2b5AvRscnofLsPK96qZjcfzEBEREREo/gUAgYCdnAoTbgAAAABJRU5ErkJggg==', '일': 'iVBORw0KGgoAAAANSUhEUgAAAEYAAABJCAYAAACAeFBRAAADcklEQVR42u2by4sdRRSHvzNzx/gYUJgsNEEUFIVxXAQMgYDCaMRHfCEKbhQiQpTgH6BbwUXARXATyMKl4kYUZyUhYdwkIZCAMaAG89TBxIWKYjIZ87mYXsSYpLvv7Xu77p36batuneqvz6k6daovZGVlZWUNXDEqD6KOAzdd9SEj/kwCjDoGrAFuKyZ7Hvgd+Dkilvpg73bgG2D1NbrsjYjZNt7WmDqrfqgeUhe9ui6qR9Sd6pNqpyH7myzRwN1XfVX9zu50Qt2q3jAyYNT1PQC5UifV2aEHo76tXrBZLanvqDGUYNR37a+2Dx0Y9RX1kv3XW22DGau5Je4aUO6zQ723zbyoznb5HjBZhSEwD+wGjhf5y63A3cDjwMMV4E4A24EXU88q71D/qRAC8+p0yVgz6p6KITWdeii9UKHvJ8BsRBy9bqodcQR4DPiogt3kPWau5IX8qN5Yc8yO+m3JuPtT95iyhfCDiDhf65C2fGZ6v6TbPW05Q1Uwa0va93Rpf3dJ+1RdTxw0mFtK2s91af+XCn0mUwZTZYuuXwyKkERVFcylkvabu1zUq/xuKWUwZS7/QJf2Z0raL0TEbymD+amkfUuX9l8vaV9IPZTK8omX1adqhtFG4I2SbvtSB/NZhT6fqs9XhPIo8AUw3oDdVjPfjnq84vnm8yITXXXFGBPqI+rHFc9d59TJivNrrx5T1GLq6G/1mHpQ/V79q+bvtw1ToWqvg9HhOjcIrRaqCr0EHOtz5C4Az/bj/qlvYCLiV+Bp4FSf5nMW2BwRp4cl870czg/AOmCu4bnMA+si4hDDLDXULcUC24vOFNcx4z3MJa2byMu28tfUrytuwxY3DfvVN3u9hewXmGgY0hSwAZgG7mK5CL4KWAT+AE4DR4F9EXG2QbubgK9KloCR+bKjDpiZEodZaNVjWoazAbjzGs0HI+JEnfE6DU5sLXCA5e9iUtMc8EwbFTyKLXxNog61ue95zEpRBpPBZDDJgTk1SmCaznzva2lnuh/YmTPf/7+Qh9ouVOU1ZqWr07BLf9lNlrkSFt9kL+nrLr45lDKYDCaDyWB61+FWt+sKeo7lf6INWmdSB7NQt/aaQymDyZlvaroIbIuIXdlj/qsJ4IkcSnmNyWAymFEEk/pNwcm2tusp4MFEoSwCB9r+6DErKysr6zr6Fxj7Gn4FkikqAAAAAElFTkSuQmCC', '토': 'iVBORw0KGgoAAAANSUhEUgAAAEYAAAA8CAYAAADbl8wjAAABV0lEQVR42u2YsUoDQRRF7w0pBBvBqEj0B2xEsPEDxMKf8Af8EHs/wMrOzkobO4t0FqIigiEiWIilqOyzSRcky8bNToZzYKrdYXln5t1hVgIAgNkhIg4j4jvSpR8RS1Xra03gZk9SO+G1W5e02YSYrEEMYhCDmBK8VZ1Y56lyKem0QSl92zcpirm1fUIrkTGIQQz87yXyPOELZBERR+yYUSxpHzFkDGIQg5jp8zzJ5DrvSmeSjhuSUkjqpSpmYPuKViJjEIMYmG74bkTEQcP13du+Tk3M7nA0SRERa7ZfaaXR+hbJGMIXMYjJScyFpJ/E67uT9DhTKxIRCyV+am/TSmQMYhCDGMRAe8yRuiJpq6Zvz5d4ZyciOjV9/8H2018PPUbMQFI3003xKWnV9keVVupm3C1zkjpkDOGLGMSkKKaXce0vw1HpuG5JWs5UzLvtL3oDACAhfgEdiZ8y/SpZ3AAAAABJRU5ErkJggg==', '화': 'iVBORw0KGgoAAAANSUhEUgAAAEYAAABICAYAAABLJIP0AAAD30lEQVR42u2aTYiVVRjHf894w5zJj3E0GcusKdCByFUgkuJCXBglE4gbNy7CTYsSKWxZtDCwWpsg6KJAiIISNOiDoqKNklRSLqT8mutHzpjaNHb/LeYUl8v4nvfjvvee1zl/eODC855znvmdr+d93oGoqKioqI7LyupY0kpgCzBrGvc4sN/MxmcccUnHlKydbRhjsaTfEsb4OG/fPSWymVfQn0argGUJ/qdDBFNpRTARTATTFtVSnPzLgadyXO2LPP4nJG3L2Of3ZvZLEHmMpJ+A4UAmsm5mS5pi2wB8mvgHmllZW+n+gFZ4x2KJZ0wEE8FEMN0G821A8XYsFm8eY2bPSBrIkcc8BqwA+p31AtecXQFOAJcz9nklGDAOjjcgSb3AVuA5YHWKBA/gNPA1cAj43Mx01+xFSQskvSNpTMV0WtIOST0Zxt7g67RbULZKuqj26jtJj1cWjKRXVZ7GJK3tJpievFCAN0rkPg84KmlNZfIYF+xrHYhtDnBI0n1Blh1aoMwCDjB95X863QZ+Bi4Bt4C5wMPAQynbDwGvAy+FfgONZDhARyTde4d+BiXtlFRP0ddNSfM7fcbUMj4/kuKZvcDLZtZIyIsuAG9JOggcAZ70bKlNwHs5J/OFBHcDOGJmZ4qumJOeCTqao8+lKXKgN/OumBT6sh2H70KPf19WMGZ2HvjA89hAiSfEQDvA+A7d0ZzBnSs4bvBlh3tKaqfQwYx5/KtzxuFrNx46mN89/lckrch4+G4D1hUct+tgvvD45wNfSdqUAkhN0i6XMPr0WYkMvpn2Usg4u48Cv6Zsdxz40BWk6k2Z7zKXt2wBHkzRzykzG77TdY3nuxKwOCmPMbOr7cp+96mz2lyVt+vdHdzz75vZR5V4u3Zlzo1kr9fm2fvbK1N2cHBOAWuBH0uK6zCw0cz+ooqS1OfqvRNtOk8uSHo+w/hh1nybAnxE0ruSruUEckLSi5L6Mo4bNpimQGdLelbSnpRAdkgaLjBeNcC0BL3Lt0raMEZYxfCZoFrIwUma4zLXVrtsZge7BkbSXOCBlCvvP6sBs4H1njarJO1l6pt2L1OfTPqBBc4WAX0JsZ3sChh3Q5zBX7UroiL/Nj+UogxSSoI3WDKUohoMLvMNREsjmLhiMql/xl7XLfrHvdFfBM4Db5O/+F4IzChwI+nKzKgGMAHcdPYncJ2pQve4u2H+cHbVQbjkrO5yl0Zr5ttxMGZ2XdKQuxb/j8VZw1nz79tuVifd70ngb2cTZjZ512S+ZlZ3szXjFN+VIpgIJoKJYCKYCCaCiWC6ox+Aswn+T+IUR0VFRVVI/wLukr8rX0aefgAAAABJRU5ErkJggg==', '회': 'iVBORw0KGgoAAAANSUhEUgAAAEYAAABICAYAAABLJIP0AAADtUlEQVR42u2aT4hVVRzHP7/XG2tKHaf824CzMHQh5hRkQYEuXEiCOYsIVGzZMFAwOJu2boKK2rSokAiyaBNEJFoEJpm08j+4sTQapXlNzuSoMzSj3xbviI/H9O69775737nO+cIPHpx3f79zP+++3/md3z0QFBQUFJS7LOsAkvqAHUBpjuG/gQNmNjXvyEs6qcba26I4KyWNNIjzbRJ/pRzYLE45Hld9QE+D8e2+gSmkApgAJoBpicoJsv5aYFMTMRZGjD8jaU9Cn+fN7LQXdYykCrDMkx90GlhuZpM189sGHG54s2aWxV9pmUdP+kNAV8gxIfkGMAHMfADzi0fz/hUY9aKOAZ4HHm2iHFgHPAEsAbqBh4F/gHHgGnC2iZucMLNZL8CY2R1gLEa9sxjYBex0BWF3DPeXgBPA58B3Ltb9IdcP+VjSTaXT75KGJJUTxt8W5bgdUAYlTai1OiNpUyHBSCpJ+lDZaUrSjnaASbtcfwK8lnHp/5WklwpTx0jaDbyaUwfggKQVXrYd6qB0AR8kuGQGuOBWtSlgEdDrLI6WAu+71c7rFeiNmDniuKR+SQ82WMn2SRqN4WtWUo/XyVfSDzFuZDiBv25JP8bwOeB78t0YlZTN7N0ExeM40B+jAn7S9+QbtTX4NKlDB+fLiK895juYqOv+atLvnxHjDxS97dCR0Sop38Fcjxh/tkm/T6eM23Ywf0SM75f0eNJNIBBV4Y74DuZYxPgq4ISkrTGAdEjaB3wdYz5H8wLT1PkYSS8AP8X8+ingG+AkUKmrfJ8DXgbilPsjQO//9Wpa/V4pTZF3WPlqb1F216/nmAyPAJ8VYndtZhepHiGbzniO54BXzEyFAOPgHAO2ZrhafA9sNrPr5KzUBZ6Z/Qw8BRwEWtXEHgeGgRfdVqHYkrRB0kFJk00m2AuS3pS0pInY/jXD55hkp+vDvB0TyKCkjSlj+g+mbsIDEfO92KI4XjXD71uVC5K7SlT7vstdlbyi5vNlM/uoLWAk9QKdMZ/Au9YBLAC2RFyzRtI7VN9pdwKPUH3P3cW9991LGz3dko7mDkbSEPBexg/FcMrrV7ejjllfgH/bSu8KPE+0KoAJT0witfyobbnAMOT2VFeBL9oB5reMbuw21W7eLeAmcMPZpLMJqkfS7h5LG6uxClAxs5nayjdvMG8Bh+rqGM1hd+rstrNZZzPAv86msz5DlzkY1yA6M9+2BGGvFMAEMAFMABPABDABTADTfp0GrjQYPxR+7qCgoCDP9R/h1CFJckdb7QAAAABJRU5ErkJggg==', '추첨일': 'iVBORw0KGgoAAAANSUhEUgAAALsAAABJCAYAAABlyld4AAAJCklEQVR42u2da6xdRRmGn6/3AoXai0JLL1ZoDS0KSK1ctGJBQFAsCiKBxoIBSgsJiSSKREOoGFolXEwgKQStthAvaQ2NQSuChXCpVRFIoS3k9GqDrWKxVdoe+vpjT5OTw9l7zVp7rbXXPv2eZP84WbO+mW/mXXOfOeA4juM4juM4juM4FcBaGbmkrwKT6jx+2cx+VfUMlDQYuBsYXSfIC2Z2u0stdb72BQb3KFqz3e3mzAQ15oCkD7SBH+cqmeE5xWWSnm4QzwZJRxTgYx9Jx0qaImmqpBMljZXUr6A8PVrSjgZ+PpnFbr8W6uTIiFZnCPBmxfXeP6cwMRwFnNng+XHAh4E1zYobmA5cHOKbXMeHTknrgGeA5cDvzawzBz+nACMaPP90u4ndqWbX4XLgVmBipH4mh9+1wCZJ3wceNrN9VfOvjxexE4Q+FVgLLI4Uek+MAx4ANkg6y8XuVFHoN4SuyMScTI4FVkr6liRzsTtVEfotwL3AgJxN9wXuAO6siq/9MmbQkcBfgQkFp2+DpGbe3wicbGb/TuHbcuDCFHHE1FxbU/ix0szOL0nolwHzC47mZkkdZnZ/u9bsJ5Qg9DwYH0b2abgo1Eqxv5g8TGPvPEkDSxD60cAiyllruUfScW1ZszuFU4YAbwdi5uQFrAKeADqAXdSmQMcD5wCfjEhvf2ABtalMF7tTaj/9GOCqiKBPA9eZ2do6z+dLmgLcR/Lc90xJJzSw5QNUpxC+GFH2jwJnJYnTzF4BZgAPR8Tb0prdxX5okjQA7wBmm9m7UX0uswPANdTm6Rvx+XYU+442KtidKcPvanF69wD7C44jabD4QzN7J9Ugo7ZN4I6EYB9quz67mb0haTrNzch8DrgkIcwiYHUTcXSY2Wsp3zkfOCNllyAp/N3Atkh7z8fWqE0wOuH5kxntPpHwfLikQWk/pN4wSPp2xG7BK9rAj8sj/JiYU1xDI+I6NcJOEiMzps8ibI+IsHN2kpG2mY2RNITaxqEk5khaYmaqsN5HR4QZBaxvkB/DQj86aRVzcFlFlLHFV5OLgNXrxjQp9IHAz4ExEcFPB+6VdGOFBX9KRJiPA081eL4AuLrENB9IGK8dlrFsY97rbFVB9SlZ6OOBPwDnpXhtHvBYWPGrWhemD/DZiKBJYUaUnPSkMwKTM9pNWq3em2brRluKXdIQSbcCL4faOi0XAGsl3VTGUnoKZgDDYsJJOqNC6U4aLM/OaDdpoWp7bx6EflDSQkn/Un5sCVtHh7fYt76SVqdI90v1mnlJy3PMn5gB6o8i7JyfMj9Ol9SZYPORSFuFDFCLEsKMUIDvqjj+J+khSR9tkY/zM6T5d+GAdqvFPiPCzn8kXRSZF5+RtDPC5qW9QuySjpB0raRXVD5/lPTlog4A9+DrFU2kdY2k0S0Wez9JHZH2fh3EN7Cbjf6SPiXpkchKbUfsYfDKij00Xw+GmqAZbpM0V9K+Jmxsl3SnpEkF+nuJpP1N+rpd0rQuNm8OtymUIvYQ52UZWtLXw8e6XtKelO/PTZHH1RG7pHGSbpH0Wg6Fs7Fr/1DSJyStzcHus5LmhDnsvPy+Pseu2TuSruzWMg5N+I3LS+whzqdKanlfTNPqVkLskiaHDMqjFtoRarTBdZrZOWEw2ix7Jf1S0vubHIwuLEgIC8Op/ph0DM1Z7CPCXTNF8ndJY1LmdyXEflcOzm8OU4iHR8Q3QNI1odlslq9l9Pl9kn6bIp7lks5J2cw/G9YgShV7sHm8pE0FCf1NSSdnyPNKiP3MJhxfJenSLIPIsOfiAkmPZ2xV9ma5XUzSKZLeSDn4HNJlLLMzxbu7kvYCFSH2YHeYpBUFTBqMyqizavTZQy0Uy9uS7pf0kRzjnxhamDRz9z/NEM91oV+dZh59ZA+1ZtpWaVm9D7MosXepUGaHQWgzbJV0Q2zXrOpinxnh8HOSvh7TVWkiHYMkzUq4+/AgU1PYPUrSoykL+GlJQxsI9Dcp7e2UdFKZYu82XjqYr7GD8QOSXggVxIAcyrYQsVuGhPQBXuW9F+psA35G7eqzdSVPf04KS9VXAsd0e/y8mZ0WO40KLKF2mDiWpcBVZrY3Ic++B3wzhd0bzey+7mIH3kp4b6qZrckpX4cD06jdJjGO2kHrgcA+4G1gC7XTSc+b2T9yLM+zgZUNhWtmZYlrVvjAdktaHAZkLT/iF2ZNzpO0VNJ/QxpnRr77pYjl7u612XczzNHvjrD9Z0mDWlGzV2QFfkrSOkUpNXvXBFE7CbSnohk2BDjWzF6NDH8b8J1I87uBWWa2LEO6TgR+Qf176XcCp5rZpp7EXmbN3uLym0b9beBrzGwjTubMPUzSXyJqznWSJjcZ1+GSftKD7U5JM8qejakT12hJ21RNVrhimy/gMWFuuB6LleNl/+FI31td7H+jFVOPdeK6UBUmi0/9EhxeQW0veW/kpdBd2N9l0LNF0sXUDph0nVXYA8wzsx/nmQAzWyrpGWonlTab2Q+SNBijU6+2MvTZK7VvuBiON7PXe/D7auDB8OffgK+UPcPUoEyWUbtyric2ULvY6J0c4rkQeKyyws0wG+PX3/WckQ9J6g+MBBZ0n1ZU7c7xjxF3V2Le3BN+PdFxyF1T4WLPRfAPNHg8j9qd5lWjU9JYM9vuJfhe/Pq7bIyrcOU1Oidbm71mdw6Vlu2lsDI9qgXRT6L2v5lKFftOyr/mobQmn+QFmkNd8OtpcLlTgYPwQv6pb5LYp1O74KcIRgALE8LcRe36jSJYa2b/dEn7APXgl72W5GuIs3694yPEvtLMHvdicrzP7hTdnehVi4ou9mJYDtxUkO2OEv3oVavnLvZi2FPUrrzev6hdHD7P7rjYHcfF7jgudscpjRd9gOqUzRcobtGvEVtd7E7ZbG+ns6DejXEOGbxmL4YJWe+WdFzs7cZp4dfb+VMLF7n2A3PNbJF3Y5zeTn/gXO+zO46L3XGxO46LvVAO5BTGcaJo2WyMmW2WtAQ4qU6QrcBzFc23VcD1wOCKpasDyPMyp83A2Arrd1Mqzfn3no1wRXeluoFm1pmzj8OBEytaBPuA1Xn77DiO4ziO4ziO4ziF83/kyt+esc8EPAAAAABJRU5ErkJggg==', '수': 'iVBORw0KGgoAAAANSUhEUgAAAEYAAABGCAYAAABxLuKEAAACjElEQVR42u2aMWsUQRSA38SExGgM3iWERAUPLiCxsRALEYISKy38CWKhgoXYCIcGBSUgAQtRtLAUVARBERsrBdFOsUhAxEIQUWNOghqPy/nZTBVyt3u7O7t7u+9r9+3Mm29n5s3unYiiKIoSOybJzoGyiOxocvmjMWYud08E2AQs05wGsCWp/LoSdFMQkT6P3EbzKCbVqBgVo2I6Xkyvj5iePIoZjCgmc2LGfcSU8yjmgI+Y/Xk79Q4DS3jzF9iWJzEP8M9jwGRdyDrgFu1zE+jKqpQy8JLgPAdKWXuLvmz3i7As27YGO1nIBqACLBI9i8A5YGMnCSkA54FvuOc7MA0U0iykBFwDfgUc5BvgRcB7f9u+S2kSMgU8sl/cgvIQGAB6bAUKSsOW94OJlHi7XE4D8yGXwk/g+BrtHwE+h2x7HjgDFOMQshe4G0GFaQC3gZEWfQ0AMx7fhf1QA+4D+1xJGQXqIZP8Z0+9E230OwbcsAMMwwqw1YWYvhCVpg7cAXaG6H8MuBpic18A+l3NmkqbyfwBrkdZLYAicMGW6naYdn2KrfpI4itwERhymEs/cAp47yOfJWCz6w34UosE3gLHgN4YK6QBDgPPWuR1JY5EiqvWeQ24B0ym4Ew1YQ961VXvVyNxJXASeA2cBYZTeApfDxwFngInRFGUpDAea/WJiBzK6NjfichuY0w9iBgyPjHGjTEf1rqgv103QcWoGBUTi5iFDI99RUSqzS52e9w8KSJ7HCU2JCKzHjGzIuLqL61zxpgfqXtcwHYfnwumdI/RzVfFqBgVo2IUFaNiVIyKUTEqRsWoGBWjYlSMikmIWkQxTuhOqmNjzBegIiK7moR8EpFXOncVRVFyxH/U+mpWV1r3XgAAAABJRU5ErkJggg==', '(': 'iVBORw0KGgoAAAANSUhEUgAAACIAAABICAYAAACTKCf+AAACC0lEQVR42u3av2sTYRgH8OcJ/ohmCOigtQHHaAnolKiR6lC3UiGLFEf/Cv+DZi7iroujOhh0UlE3h7QqWih20BLEgA5pTGLu62I3yffukvsayD3r9+X48Lx53/cud2ZppTVrBcAB3AMQ4N/1RgW5jdH1XoG4BGAwAjEEcDFpRA7ADulGXdGNOpsSAIeTRhQB9AnkmqIbTwmioUBcIIjfAEoKyGMCeaBAlEZsXPtVVkDuEsQrBeIQgDaBrCogNYLYA5CLet1MDMtNkj9x907S3TgA4CfpyA3FtFQJIgBwPM61o07NEsk33b2tgFwh+Yu43Y4KOUfy14lDABTM7BgZ9k7REdaNgZltKSBnSP7J3QcKSIHkn8fZGqJA5km+O3OQEyRvqSBHSd5RQbIk76ogR0j+SwVhD0l9FcSTvMXI2JRUFEgwLZDemL+hiUG6Y66qiUHY8syqIGznzKsg7Cw5pYJ8JfnctEBkHflC8qIK8oHkp+M8fMeBbIQ4i84mDnH3lpl9I8POqw69JsmrKshzkl+WHNUAyuB1UtGRt2b2g4xZThzi7kMze0aG1VTTs0Kmpgcgr4AcBPCdYG6punKHQJoqyEKIv8CvqjAPCeSRClIJsadUVJgGgbxUQYp/l+uouq7CrBHI9jj3KVEgYV63rqu6wl5ABwAWVRj2Sv6jCuIA7v/3jxTSSivp+gMAcWGq+cTtjAAAAABJRU5ErkJggg==', '제': 'iVBORw0KGgoAAAANSUhEUgAAAEYAAABHCAYAAAC6cjEhAAAC+0lEQVR42u2aS0hUURjH/2ecjEh7UcJEYRYYQkGQPRctAoMyjCKiVVQQbkKKtkFgi8DIoGVFZYtc5EZKcVVto02EG4vCINoURIbQw/y1ucEwODPnOjrex/ffDfc73znnx/0eZ+6RTCaTyWSqVEAd8I7ieurjx8Vgo4skPZC0qYjJsHOuO8++VdKrkpt2ziXhDdhBaf0tsG8tY4/PvJkYsKlZiD1kLCvNrKzn67xe0vYqrOePpBfOuclYgJH0UlKuSmu6L+nsQoPxDaVcFde0NgqhZDnGwBgYAxMFMMNVWs+UpJHY9DHOuXbPfmdcUmMJk4POuRELJcsxBsbAGBhTRYfIeRNwVVJLCZNVSQCTCfMcaJZ0OQ2htKzM8xUFv2sTn2MAJ6m+jNnKNCbfRg9/m9MIZpuHzZ40gtnlAw/IrzLTiS7XQX457jnfaUm9we8xSQNlyvUSSRtj2QwBR/DXZ2BpCN+7w3xAi8wHN6BWUk+IITlJV9KQY65Jag455hKwL7FggGOSLs5y3sdAY+LAAFsk9Wn2NyYaJD0B6hMDBlgtaVBSXYXzb5XUD2RiDyaoKEMeJRRJEx4u2yXdiDWY4BLPgKSdHuY9QX/y1cP2AtAZ116lBuj37FWeATXBuDZgymPMFHAiKn2ML5QM0OcJ5QPQUDC+y3Psb6AjFmAAB9z13Ng3oKWIn+uePn4ChyINJnhT7nlu6Bewvwzg/hC+DkcSTJBTHnpuZBo46XN8AJ6HgNMRRTB3QhwMu0L4XQ688fQ7GsVD5AHPvXY75275gnHOfZfUJumtRx90M4rleS8wUQZ+bwX+1wUVrFhonoty8i0F5/Yc+N8AjBdeaAbOxKFczwTn0Vydb4Am4GMelFNxavDy4QwC2TkO26aglB+NVef7/28G4DywuMq5bkHAZENUk1FJo0qJ7LaDgTEwBsbAGBgDY2AMjIGput5L+lHi+ev5mDQbdSrOuS9ATtKaIiafUgkmgDMpadJCqTKNBeFXTEOWQU0mkymi+gdipW1N0ou7fAAAAABJRU5ErkJggg==', '금': 'iVBORw0KGgoAAAANSUhEUgAAAEYAAABFCAYAAAD3upAqAAABgUlEQVR42u2azUoDMRSFz9EWQZcWQcEfRHFdETcufICCT+Hrdae+gQguFYqC4M+2Hd2IIE69PkCVW2fINDM53/YmgXzJDTchgBBCiMph0Y5mtgPgqMwYgbkmOZiFmEcAWxEv+iuADkmrWsw7gKXIM6JNMi/ScU6nicRIjMREKuZc+iLEzE7Np6VU0hnzrxrMUhSz4MTHJMcSM8lnqqnkXUc+UhWz7MSzVMV0nPgoVTErTnyYqphtJ/6SnBgzmwew7jR7TnHHbABoS8wk3Sna3KcoZt+J52XF0MnlMwC9ht4TbwAckPwqIsbQbHZJPujZIZE6RmIkpkZiRg2eew7g7a+g91h8DOCwoWIGJDPlhhBiFpT6DWVmXQCbkc5tSPKycjFmtgfgLvKF75G8qLrAW61BRqyp8tWVQGIkRmJqRCvw+IX/2U5ZMjyFqqO0YyRGYiRGYiRGYiRGBd7vnJjZd8DxF+sqpq9U0hkjMRIjJKYSMbco+ck4MBmAKy2xEELUiB86jnAwj3HJ/gAAAABJRU5ErkJggg==', '목': 'iVBORw0KGgoAAAANSUhEUgAAAEYAAABGCAYAAABxLuKEAAABh0lEQVR42u2ZsUoDURBFzw0pFOy1iKWIlYLBSrDQRmwt/QH/wE/xL0SxTCGIlZ2FhVgEbCIxiChRiDI2diGsvLCbzeaeemc27+TNZJiAMcaYwlFqYETUgVtgo6RnewI2JXVTgmtjvLhRYikAy8B6anDNRWMxFmMxFlM89ZzzHwOdHPOfTauYlqTHvJJHhEvJPcZiLMZiLMZzzNisRcSCxQxz4VJyj7EYizEWU4iYDvmuFMalDzykBmucN0fEHLCUGN4ArjOeOQJuEvP3JL1PZI6R9AW0E6X+57FnSe1pKyX3mFlEGdf9Ejio6NnvgKakQYqYqPjFWBm1k3YpucdYjMVMUsxLhc/+DbymTr47wFZFxdxL6rk2jCknEdGKctOPiMNCf67/9jC7Jf/u5oE9zzEe8CzGYqokZgC8VVlM0jJc0k9EbAPNCX/+E2DV93t4bLjKmGVO3WPcfC3GYizGYizGYizGWIzFzKCYrD8Eu6mJNc1WImIR2B+xJfgEziV9+P4bY8yU8AvTMw7sOK9I6AAAAABJRU5ErkJggg==', ')': 'iVBORw0KGgoAAAANSUhEUgAAACIAAABICAYAAACTKCf+AAACC0lEQVR42u2Zuy9EURDGZyRil4SEIEuBSkLiraIVHQm1isajVIhCIUqtRikS/4MoRDQqWc9oROKx2IJEBPH4FLbDnYN7vr2S/dpvcu8vM5NzZ+4RySmn/y4AcwDe8LW2AVSG+b68AK9YRPQbr0VElgAoIyMlAE4RrClWeXoNkGcA7SyYRQNmi1WiMgA3BswIKyuTBkgaQAkDpADAsQEzzcrKiAFyDSDOAIllXhakCVZWZg2QQxZIAsCrAdMR9hH/SaqaEpENI2yIlZVRh6bNY4BUOJSn02tpMuW5FpGkEdbjHSSj9bBBfluefqM0TwDyGSDlsNXkvTSqmhaRKyOsmdEjIiJ7UQHZNfwGFsiJ4VezQC6iApIy/DIAsSiAiIhUMEDuHWIKGSCPDjFxBsiDQ4z/HlHVp6hkJNTn+5+kfIM47ruvjIzEQmpoCsgjAyQelYy4bP/3DJCE1c8OUxwFJK2qzwyQKsM/Z80j9YZ/xgJpNPwDFog1HCe9gwCok48/00HaYWSk2+EgO4oCyKaqvjBAugx/jbGA1zgs4G2MeWTQ8C9FZJsBMmD4K6oK32Wpdfh/1sroj3kDYp8BUeRwXTLGABk3IC5/snT/JRsXWb/fAzDjcHFU7BuiEsCdATLMyMZy1i8XAfRl/boVQCmAVBQadMGAWA2zJEHfmtvMbvLdGDjk/ZuSU05R1DteczfePMxSaAAAAABJRU5ErkJggg=='}

def _ko_token_image(token, color, target_h=50):
    raw=_b64.b64decode(_MD_KO_GLYPHS[token])
    im=Image.open(BytesIO(raw)).convert('RGBA')
    if im.height != target_h:
        nw=max(1,round(im.width*target_h/im.height))
        im=im.resize((nw,target_h),Image.Resampling.LANCZOS)
    # Stored glyphs are white-alpha masks; recolor at runtime.
    alpha=im.getchannel('A')
    out=Image.new('RGBA',im.size,tuple(color)+(0,))
    out.putalpha(alpha)
    return out

def _paste_ko_center(base, token, center, color=(8,8,8), target_h=50):
    im=_ko_token_image(token,color,target_h)
    x=round(center[0]-im.width/2); y=round(center[1]-im.height/2)
    base.paste(im,(x,y),im)

def _draw_date_banner_text(base, d, target_draw, draw_date):
    # Bold Korean labels are embedded raster glyphs; digits use scalable bold font.
    _paste_ko_center(base,'제',(110,171),(8,8,8),52)
    d.text((320,166),str(int(target_draw)),font=_pick_font(88,True),
           fill=(208,0,0),anchor='mm')
    _paste_ko_center(base,'회',(486,171),(8,8,8),52)
    d.line((602,143,602,202),fill=(20,20,20),width=3)
    _paste_ko_center(base,'추첨일',(715,171),(8,8,8),48)

    if draw_date is None:
        return
    try:
        dt=pd.Timestamp(draw_date)
        parts=[str(dt.year),'년',str(dt.month),'월',str(dt.day),'일','(', '월화수목금토일'[dt.dayofweek], ')']
    except Exception:
        d.text((1165,167),str(draw_date),font=_pick_font(55,True),
               fill=(9,41,174),anchor='mm')
        return

    digit_font=_pick_font(55,True)
    gap=7
    rendered=[]
    total=0
    for part in parts:
        if part in _MD_KO_GLYPHS:
            im=_ko_token_image(part,(9,41,174),44)
            rendered.append(('img',im))
            total += im.width
        else:
            bb=d.textbbox((0,0),part,font=digit_font,stroke_width=1)
            w=bb[2]-bb[0]
            rendered.append(('txt',(part,w,bb)))
            total += w
        total += gap
    total -= gap
    x=1165-total/2
    for typ,obj in rendered:
        if typ=='img':
            im=obj
            base.paste(im,(round(x),round(167-im.height/2)),im)
            x += im.width+gap
        else:
            part,w,bb=obj
            # bbox-aware vertical centering
            y=167-(bb[1]+bb[3])/2
            d.text((x-bb[0],y),part,font=digit_font,fill=(9,41,174),
                   stroke_width=1,stroke_fill=(9,41,174))
            x += w+gap

def recommendation_image_bytes(games,target_draw,basis_draw=None,draw_date=None):
    """Render on the exact user-approved 1536x1024 SIGNATURE GOLD template.

    Static artwork is preserved pixel-for-pixel. Only the draw/date text and the six
    ball slots in each of the five rows are updated dynamically.
    """
    base=Image.open(BytesIO(_b64.b64decode(_FINAL5_TEMPLATE_B64))).convert('RGB')
    if base.size != (1536,1024):
        base=base.resize((1536,1024),Image.Resampling.LANCZOS)
    d=ImageDraw.Draw(base)

    # --- 1) Draw/date banner: keep original gold border and only clear the inner text field. ---
    # The approved template has a subtle vertical cream/gold gradient. Reconstruct only the
    # interior where sample text existed, leaving the frame, bevel and shadows untouched.
    bx0,by0,bx1,by1=38,128,1498,219
    top=(255,251,229); bottom=(246,232,177)
    for yy in range(by0,by1+1):
        a=(yy-by0)/max(1,(by1-by0))
        col=tuple(int(top[i]*(1-a)+bottom[i]*a) for i in range(3))
        d.line((bx0,yy,bx1,yy),fill=col,width=1)
    # light inner sheen matching the original plate
    d.line((bx0+8,by0+3,bx1-8,by0+3),fill=(255,255,244),width=2)

    _draw_date_banner_text(base,d,target_draw,draw_date)

    # --- 2) FINAL LOCKED LOTTO BALL TEMPLATE ---
    # Draw every dynamic ball from one renderer instead of cropping sample balls from
    # the background template. This prevents old sample colors/numbers from leaking
    # through and guarantees the approved white-center + colored 3D rim design.
    centers_x=[428,618,808,998,1188,1378]
    centers_y=[300,430,560,690,820]
    f_num=_pick_font(76,True)
    for g,cy in zip(games,centers_y):
        for cx,n in zip(centers_x,g):
            n=int(n)
            # Completely cover the sample ball embedded in the static board first.
            # Keep the surrounding row frame/label untouched.
            d.ellipse((cx-67,cy-67,cx+67,cy+73),fill=(242,244,247))
            _draw_signature_ball(d,cx,cy,n,f_num)

    out=BytesIO(); base.save(out,format='PNG',optimize=True)
    return out.getvalue()

def pct(v,d=2):
    try:return f'{float(v)*100:.{d}f}%'
    except:return '-'

def five_ticket_threeplus_theoretical_bounds():
    den=math.comb(45,6)
    p_single=sum(math.comb(6,k)*math.comb(39,6-k) for k in range(3,7))/den
    max_cov=min(1.0,5*p_single)
    return {
        'single_3plus':p_single,
        'max_5ticket_3plus_union_bound':max_cov,
        'min_5ticket_miss_union_bound':1.0-max_cov,
    }

def _xlsx_col_letter(n):
    s=''
    while n:
        n,rem=divmod(n-1,26)
        s=chr(65+rem)+s
    return s

def _xlsx_inline_cell(ref, value, style=0):
    if value is None or (isinstance(value,float) and pd.isna(value)):
        return f'<c r="{ref}" s="{style}"/>'
    if isinstance(value,(int,float)) and not isinstance(value,bool):
        return f'<c r="{ref}" s="{style}"><v>{value}</v></c>'
    txt=_xml_escape(str(value))
    return f'<c r="{ref}" t="inlineStr" s="{style}"><is><t>{txt}</t></is></c>'

def _history_xlsx_bytes(history_df, status_dict):
    d=history_df[['draw_no','draw_date','n1','n2','n3','n4','n5','n6','bonus']].copy()
    d=d.sort_values('draw_no').reset_index(drop=True)
    d['draw_date']=pd.to_datetime(d['draw_date']).dt.strftime('%Y-%m-%d')
    headers=['회차','추첨일','번호1','번호2','번호3','번호4','번호5','번호6','보너스']

    def sheet_xml(rows, widths, freeze=True, autofilter=None):
        max_cols=max(len(r) for r in rows)
        max_rows=len(rows)
        cols=''.join(
            f'<col min="{i}" max="{i}" width="{w}" customWidth="1"/>'
            for i,w in enumerate(widths,1)
        )
        xml_rows=[]
        for ri,row in enumerate(rows,1):
            cells=[]
            for ci,val in enumerate(row,1):
                style=1 if ri==1 else 0
                cells.append(_xlsx_inline_cell(f'{_xlsx_col_letter(ci)}{ri}',val,style))
            xml_rows.append(f'<row r="{ri}">'+''.join(cells)+'</row>')
        pane='<pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/>' if freeze else ''
        filt=f'<autoFilter ref="{autofilter}"/>' if autofilter else ''
        return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                f'<dimension ref="A1:{_xlsx_col_letter(max_cols)}{max_rows}"/>'
                f'<sheetViews><sheetView workbookViewId="0">{pane}</sheetView></sheetViews>'
                '<sheetFormatPr defaultRowHeight="18"/>'
                f'<cols>{cols}</cols><sheetData>{"".join(xml_rows)}</sheetData>{filt}</worksheet>')

    history_rows=[headers]
    for _,r in d.iterrows():
        history_rows.append([
            int(r.draw_no), str(r.draw_date),
            int(r.n1),int(r.n2),int(r.n3),int(r.n4),int(r.n5),int(r.n6),int(r.bonus)
        ])

    expected=list(range(1,int(d.draw_no.max())+1)) if len(d) else []
    actual=d.draw_no.astype(int).tolist()
    missing=sorted(set(expected)-set(actual))
    duplicate_count=int(d.draw_no.duplicated().sum())
    invalid_number_rows=0
    for _,r in d.iterrows():
        nums=[int(r[f'n{i}']) for i in range(1,7)]
        if len(set(nums))!=6 or not all(1<=x<=45 for x in nums) or int(r.bonus) in nums or not 1<=int(r.bonus)<=45:
            invalid_number_rows+=1

    audit_rows=[
        ['검증항목','결과'],
        ['파일 목적','MD LOTTO 앱이 실제 사용하는 전체 당첨이력 확인용'],
        ['최소 회차',int(d.draw_no.min()) if len(d) else '-'],
        ['최신 회차',int(d.draw_no.max()) if len(d) else '-'],
        ['총 데이터 행',int(len(d))],
        ['1회부터 연속 데이터','정상' if bool(status_dict.get('complete_from_draw1')) else '미완료'],
        ['누락 회차 수',len(missing)],
        ['누락 회차','없음' if not missing else ', '.join(map(str,missing[:100]))],
        ['중복 회차 수',duplicate_count],
        ['번호/보너스 유효성 오류 행',invalid_number_rows],
        ['최신 추첨일',str(status_dict.get('latest_date') or '-')],
        ['주의','이 파일은 앱 내부 분석에 사용되는 현재 데이터의 복사본입니다. 추천 확률을 의미하지 않습니다.'],
    ]

    content_types='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/><Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/><Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/><Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/></Types>'''
    root_rels='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>'''
    workbook='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="전체 당첨이력" sheetId="1" r:id="rId1"/><sheet name="데이터 검증" sheetId="2" r:id="rId2"/></sheets></workbook>'''
    wb_rels='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>'''
    styles='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><fonts count="2"><font><sz val="10"/><name val="Arial"/></font><font><b/><color rgb="FFFFFFFF"/><sz val="10"/><name val="Arial"/></font></fonts><fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF17365D"/><bgColor indexed="64"/></patternFill></fill></fills><borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders><cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs><cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/><xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"><alignment horizontal="center"/></xf></cellXfs><cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles></styleSheet>'''
    core='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>MD LOTTO 전체 당첨이력 검증</dc:title><dc:creator>MD LOTTO</dc:creator></cp:coreProperties>'''
    app_xml='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>MD LOTTO</Application></Properties>'''

    s1=sheet_xml(history_rows,[10,14,9,9,9,9,9,9,9],True,f'A1:I{len(history_rows)}')
    s2=sheet_xml(audit_rows,[25,65],True,None)

    out=BytesIO()
    with ZipFile(out,'w',ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml',content_types)
        z.writestr('_rels/.rels',root_rels)
        z.writestr('docProps/core.xml',core)
        z.writestr('docProps/app.xml',app_xml)
        z.writestr('xl/workbook.xml',workbook)
        z.writestr('xl/_rels/workbook.xml.rels',wb_rels)
        z.writestr('xl/styles.xml',styles)
        z.writestr('xl/worksheets/sheet1.xml',s1)
        z.writestr('xl/worksheets/sheet2.xml',s2)
    return out.getvalue()

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



def _weekly_prediction_compare(learning_path, history_df, current_games=None, current_target=None):
    rows=load_learning_log(learning_path)
    issued=[r for r in rows if r.get('games')]
    candidates=[r for r in issued if current_target is not None and int(r.get('target_draw',-1)) < int(current_target)]
    prev=candidates[-1] if candidates else (issued[-1] if issued else None)
    prev_games=[set(map(int,g)) for g in (prev.get('games',[]) if prev else [])]
    cur_games=[set(map(int,g)) for g in (current_games or [])]
    prev_union=set().union(*prev_games) if prev_games else set()
    cur_union=set().union(*cur_games) if cur_games else set()
    actual=set(map(int,prev.get('actual',[]) or [])) if prev else set()
    return {
        'previous_target':int(prev.get('target_draw')) if prev else None,
        'current_target':int(current_target) if current_target is not None else None,
        'previous_union':sorted(prev_union),'current_union':sorted(cur_union),
        'common':sorted(prev_union&cur_union),'added':sorted(cur_union-prev_union),
        'removed':sorted(prev_union-cur_union),
        'previous_union_hits':len(prev_union&actual) if actual else None,
        'previous_best_hits':max((len(g&actual) for g in prev_games),default=0) if actual else None,
        'ticket_overlap':[{'금주조합':i,
                           '전주와 최대중복':max((len(cg&pg) for pg in prev_games),default=0),
                           '신규번호':len(cg-prev_union)}
                          for i,cg in enumerate(cur_games,1)]
    }

def _build_integrated_correction():
    """Create the next-draw correction plan from last outcome + transition + FDR + backtest + AI.
    The plan is bounded and only changes ranking/coverage parameters; it never claims a probability boost.
    """
    adj=next_draw_adjustment_report(df)
    prof=adj.get('profile',{}) if adj.get('available') else {}
    fdr=fdr_summary(df)
    bt_df=cached_mobile_backtest(int(latest.draw_no),30)
    bt_sum=summarize_backtest(bt_df) if bt_df is not None and len(bt_df) else {'tests':0,'evidence_of_edge':False}
    ml=cached_mobile_ml_holdout(int(latest.draw_no))

    log=[r for r in load_learning_log(learning_path) if r.get('evaluated')]
    last=log[-1] if log else None
    failure_type='기본 분산전략'
    union_hits=None
    best_hits=None
    pool_size=20
    max_overlap=3
    actions=[]

    # v7.7 weekly evolutionary learner: only out-of-sample walk-forward
    # performance may alter pool breadth / ticket overlap.
    evo=_evolution_plan if isinstance(_evolution_plan,dict) else {}
    if evo.get('available'):
        pool_size=int(evo.get('pool_size',pool_size))
        max_overlap=int(evo.get('max_overlap',max_overlap))
        sel=evo.get('selected',{})
        actions.append(
            f"자기학습 {evo.get('mode','균형 유지')} → 후보 Pool {pool_size}개 · "
            f"5조합 최대중복 {max_overlap}개 · 최근10주 후보군 평균적중 "
            f"{float(sel.get('recent10_pool_hits',0)):.2f}개"
        )

    if last:
        best_hits=int(last.get('best_hits',0))
        missed=list(last.get('missed_actual_numbers',[]))
        union_hits=max(0,6-len(missed))
        if union_hits>=4 and best_hits<=2:
            failure_type='조합배치 보완 필요'
            max_overlap=min(max_overlap,2)
            actions.append('실제번호가 후보군에는 있었지만 서로 흩어진 것으로 판단 → 5조합 간 중복을 줄여 배치 커버리지를 확대')
        elif union_hits<=2:
            failure_type='후보번호 선정 보완 필요'
            pool_size=max(pool_size,22)
            actions.append('실제번호가 후보군 자체에 적게 포함됨 → 후보 Pool을 확대해 후보선정 편중을 완화')
        else:
            failure_type='후보선정·조합배치 혼합 보완'
            pool_size=max(pool_size,22)
            max_overlap=min(max_overlap,2)
            actions.append('후보선정과 조합배치를 동시에 소폭 보완')

    # Current-state analog profile supplies the next-draw structural targets.
    targets={}
    for k in ('sum','odd','range','consecutive_pairs','overlap_prev'):
        v=prof.get(k+'_mean')
        if v is not None:
            targets[k]=float(v)

    # Blend in accumulated post-evaluation profile only after enough real weekly evaluations.
    lp=learning_profile(learning_path)
    if lp.get('available'):
        lt=lp.get('targets',{})
        for k in ('sum','odd','range','consecutive_pairs','overlap_prev'):
            if k in lt:
                targets[k]=0.75*float(targets.get(k,lt[k]))+0.25*float(lt[k])
        actions.append('누적 사후평가 5회 이상 → 최근 실제 결과의 구조를 25% 이내로 보수적으로 반영')

    pair_sig=int(fdr.get('pair_fdr_significant',0))
    triple_sig=int(fdr.get('triple_fdr_significant',0))
    if pair_sig+triple_sig==0:
        pair_scale=.85
        fdr_status='Pair 가중 축소'
        actions.append('FDR에서 강한 Pair·Triple 근거가 없어 Pair 영향력을 축소')
    else:
        pair_scale=1.0
        fdr_status='Pair 가중 유지'

    bt_ok=bool(bt_sum.get('evidence_of_edge',False))
    ml_ok=bool(ml.get('available') and ml.get('beats_constant_logloss'))
    # Correction strength is deliberately bounded. Weak validation -> smaller influence.
    max_bonus=4.0 if (bt_ok and ml_ok) else 3.0 if (bt_ok or ml_ok) else 2.0
    if not bt_ok:
        actions.append('백테스트에서 랜덤 대비 뚜렷한 우위 근거가 부족 → 보정 강도를 낮춤')
    if not ml_ok:
        actions.append('AI Holdout이 기본모델 우위를 확인하지 못함 → AI 신호는 가중치 강화에 사용하지 않음')

    return {
        'available':True,
        'basis_draw':int(latest.draw_no),
        'target_draw':int(latest.draw_no)+1,
        'failure_type':failure_type,
        'best_hits':best_hits,
        'union_hits':union_hits,
        'targets':targets,
        'pool_size':pool_size,
        'max_overlap':max_overlap,
        'pair_scale':pair_scale,
        'max_bonus':max_bonus,
        'actions':actions[:6],
        'fdr_status':fdr_status,
        'backtest_status':'우위 확인' if bt_ok else '랜덤기준 유지',
        'ai_status':'가중 허용' if ml_ok else '가중 제외',
        'overall_status':'보정 적용' if targets else '기본전략 유지',
        'evidence':{'fdr':fdr,'backtest':bt_sum,'ml':ml}
    }

def _get_current_correction(force=False):
    key='integrated_correction_plan'
    plan=st.session_state.get(key)
    if force or not plan or int(plan.get('basis_draw',-1))!=int(latest.draw_no):
        plan=_build_integrated_correction()
        st.session_state[key]=plan
    return plan

@st.cache_data(show_spinner=False, max_entries=8)
def cached_mobile_ml_walk_forward(latest_draw, tests):
    return walk_forward_ml(load_csv(path),start_train=300,max_tests=tests)

# SAFE BOOT: render immediately from embedded/validated local history.
# External sync is manual so a slow/blocked network can never leave the app blank.
if not path.exists():
    st.error('내장 데이터 파일을 준비하지 못했습니다. 앱을 다시 배포해 주세요.')
    st.stop()
df=load_csv(path)

# v8.0 FINAL COMPLETE:
# Never perform external network recovery before the first screen is rendered.
# Streamlit Cloud can block/slow lottery endpoints and previously left the app
# sitting indefinitely on the full-history spinner. Use bundled/cached history
# immediately; the existing manual sync control performs recovery on demand.
if not st.session_state.get('_safe_boot_v784'):
    st.session_state['_safe_boot_v784']=True
    st.session_state['startup_sync_status']={
        'ok':True,'using_cached_data':True,'safe_boot':True,
        'message':'1회부터 최신 1241회까지 검증된 전체이력을 내장했습니다. 온라인 동기화가 실패해도 전체 기능을 사용할 수 있습니다.'
    }
    st.session_state['incremental_sync_status']={'ok':True,'safe_boot':True,'added_draws':[]}

df=load_csv(path)
status=dataset_status(df)
ns=number_stats(df)
latest=df.iloc[-1]

# v8.0 FINAL COMPLETE: bounded walk-forward evaluation for mobile/cloud startup.
try:
    if len(df) >= 120 and int(df.draw_no.min()) == 1:
        with st.spinner('주간 자기학습 데이터를 빠르게 점검하고 있습니다...'):
            _evolution_plan=evolutionary_weekly_plan(df,eval_weeks=52)
    else:
        _evolution_plan={'available':False,'reason':'전체 1회~최신회차 복구·동기화 후 자기학습이 활성화됩니다.'}
except Exception as _e:
    _evolution_plan={'available':False,'reason':f'자기학습 계산 오류: {_e}'}
try:
    _evolution_report=evolution_report(df,_evolution_plan,weeks=12)
except Exception as _e:
    _evolution_report={'available':False,'rows':[],'summary':f'학습진화 리포트 계산 오류: {_e}'}

# Invalidate results that were created for a previous draw.
_current_draw=int(latest.draw_no)
_previous_basis=st.session_state.get('_analysis_basis_draw_v76')
if _previous_basis is not None and int(_previous_basis)!=_current_draw:
    for _k in ('md_games','md_recommendation_record','last_bt','corr_reg_diag','sim_optimizer_result','md_sim_final_games','integrated_correction_plan'):
        st.session_state.pop(_k,None)
st.session_state['_analysis_basis_draw_v76']=_current_draw

ss=st.session_state.get('startup_sync_status') or load_sync_status(sp) or {'ok':True,'using_cached_data':True}

_learning_rows,_new_learning_reports=evaluate_pending(learning_path,df)
_learning_summary=learning_summary(learning_path)
_learning_profile=learning_profile(learning_path)
nums=[int(latest[f'n{i}']) for i in range(1,7)]; bonus=int(latest.bonus)

_status_ok=bool(ss.get('ok') and status.get('complete_from_draw1'))
_status_text='SYSTEM READY' if _status_ok else 'DATA CHECK'
_status_class='live' if _status_ok else ''
st.markdown(premium_brand_banner_html(),unsafe_allow_html=True)
st.markdown(
    f'''<div class="cmd-status">
        <div class="cmd-stat {_status_class}"><div class="lab">SYSTEM</div><div class="val">{_status_text}</div></div>
        <div class="cmd-stat"><div class="lab">LATEST DRAW</div><div class="val">제 {int(latest.draw_no)}회</div></div>
        <div class="cmd-stat"><div class="lab">HISTORY</div><div class="val">{len(df):,}회</div></div>
        <div class="cmd-stat"><div class="lab">LAST DATE</div><div class="val">{latest.draw_date.strftime("%Y-%m-%d")}</div></div>
    </div>''',unsafe_allow_html=True)

if not status.get('complete_from_draw1'):
    st.warning(f"전체이력 복구 필요 · 현재 {status.get('min_draw')}~{status.get('max_draw')}회만 보유 · 추천 잠금")
elif not ss.get('ok'):
    st.warning('온라인 최신 확인 실패 · 저장된 전체 검증 데이터를 사용 중입니다.')

st.markdown(
    f'''<div class="draw-stage">
      <div class="draw-stage-head">
        <div><div class="draw-stage-kicker">LATEST OFFICIAL RESULT</div><div class="draw-stage-title">제 {int(latest.draw_no)}회 최신 당첨번호</div></div>
        <div class="draw-stage-date">{latest.draw_date.strftime("%Y-%m-%d")}</div>
      </div>
      {balls_html(nums,bonus)}
    </div>''',unsafe_allow_html=True)

st.markdown(
    '''<div class="command-grid">
      <div class="command-card hot"><div class="no">STEP 01</div><div class="ttl">차기회차 보정</div><div class="txt">지난 결과·FDR·백테스트·AI 검증을 내부 종합해 다음 전략을 먼저 보정</div></div>
      <div class="command-card"><div class="no">STEP 02</div><div class="ttl">최종 5조합 생성</div><div class="txt">보정된 후보군으로 5조합을 한 화면에 압축 제시</div></div>
      <div class="command-card"><div class="no">STEP 03</div><div class="ttl">통합 최적화</div><div class="txt">반복 시뮬레이션 후 최종 조합을 다시 경쟁·선별</div></div>
    </div>''',unsafe_allow_html=True)

with st.expander('📘 사용 순서 자세히 보기',expanded=False):
    st.markdown('''
**① 앱 실행 → 데이터 상태 확인**  
맨 위가 `전체 데이터 정상`인지 먼저 봅니다. 정상이 아니면 다른 기능을 실행하지 말고 사이드바의 `🔄 지금 최신 데이터 확인`을 누릅니다.

**② 필요하면 Excel로 원본 확인**  
`1회~최신회차 전체 데이터 Excel 다운로드`를 눌러 누락 회차 0, 중복 0, 번호 오류 0인지 확인합니다. 매주 반드시 할 필요는 없고 데이터가 이상해 보일 때 확인하면 됩니다.

**③ 대시보드 확인**  
최근 1년 출현번호, 직전회차 대비 변화, 번호합·홀짝·연속수 흐름을 봅니다. 여기서는 직접 6개 번호를 고르지 않습니다. “이번 회차의 환경이 어떤가”만 파악합니다.

**④ 번호 추천 실행**  
`🎯 이번 회차 우선순위 5조합 만들기`를 누릅니다. 이것이 기본 추천 5조합입니다. 평가 이력이 5회 이상 쌓이면 프로그램이 누적 사후결과를 최대 2점 범위에서만 우선순위에 반영합니다.

**⑤ FDR 분석 확인**  
Pair·Triple 가운데 우연히 많이 나온 것으로 보이는 패턴을 걸러내는 단계입니다. 사용자가 숫자를 직접 계산할 필요는 없습니다. FDR 유의 패턴이 거의 없으면 Pair/Triple을 강한 근거로 믿지 않는다는 의미입니다.

**⑥ 백테스트 확인**  
과거 시점에서 같은 추천방식을 사용했을 때 랜덤 기준보다 안정적이었는지 봅니다. `랜덤 대비 개선 근거가 약함`이면 해당 전략을 강하게 믿지 않습니다.

**⑦ AI 진단 확인**  
AI가 미사용 미래구간에서도 기본모델보다 나았는지 확인합니다. 기본모델을 이기지 못하면 AI 신호의 가중치를 강화하지 않는 것이 정상입니다.

**⑧ 통합 시뮬레이션 실행**  
마지막으로 `🧠 통합 최적화 시뮬레이션 실행`을 누릅니다. FDR·백테스트·AI를 검증 게이트로 사용하고 후보 조합들을 반복 경쟁시켜 5조합의 3개+ 커버리지와 분산을 다시 최적화합니다.

**⑨ 실제 참고할 최종 번호**  
통합 시뮬레이션이 완료되면 화면의 `통합 분석이 선택한 최종 5조합`을 그 주의 최종 참고안으로 봅니다. 시뮬레이션을 실행하지 않았다면 기본 우선순위 5조합을 사용합니다.

**⑩ 다음 추첨 후 해야 할 일**  
다음 추첨이 끝난 뒤 앱을 다시 열고 `최신 데이터 확인`을 실행합니다. 프로그램이 지난주 최종 5조합과 실제 당첨번호를 자동 비교해 `누적 학습 · 사후평가`에 저장합니다.

**⑪ 누적 학습에서 볼 것**  
`평가 누적`, `평균 최고 일치`, `3개+ 발생률`, `최근10회 평균`을 봅니다. 최근 성능이 장기평균보다 계속 나빠지면 프로그램 전략의 재검증 신호로 봅니다.

**⑫ 사용자가 실제로 해야 하는 액션은 4개뿐입니다**  
`데이터 확인 → 기본 5조합 생성 → 통합 시뮬레이션 실행 → 다음 추첨 후 다시 동기화`. 나머지 FDR·백테스트·AI 숫자는 프로그램의 검증 근거를 확인하는 화면입니다.
''')

with st.sidebar:
    st.header('데이터 관리')
    if status.get('complete_from_draw1') and ss.get('ok'):
        st.success(f"1회~{status.get('max_draw')}회 전체이력 확인")
    elif status.get('complete_from_draw1'):
        st.warning(f"저장된 1회~{status.get('max_draw')}회 사용 중 · 온라인 확인 실패")
    else:
        st.error(f"전체이력 미완료 · {status.get('min_draw')}~{status.get('max_draw')}회")
    st.caption('연속 전체이력 정상' if status.get('complete_from_draw1') else '추천 전 전체이력 복구가 필요합니다.')
    if st.button('🔄 지금 최신 데이터 확인',use_container_width=True):
        with st.spinner('전체 회차와 최신 회차를 확인하는 중입니다...'):
            try:
                _df,_st=sync_history(path,verify_official_count=2)
                st.session_state['startup_sync_status']=_st
                save_sync_status(_st,sp)
                _df,_inc=sync_incremental_official(path,max_new=6,timeout=6)
                st.session_state['incremental_sync_status']=_inc
                for _k in ('md_games','md_recommendation_record','last_bt','corr_reg_diag','sim_optimizer_result','md_sim_final_games','integrated_correction_plan'):
                    st.session_state.pop(_k,None)
            except Exception as _e:
                st.session_state['startup_sync_status']={'ok':False,'error':str(_e),'using_cached_data':True}
        st.rerun()
    st.caption('동기화 실패 시 기존 검증 데이터는 보존됩니다.')
if not status['complete_from_draw1']: st.error(f"현재 데이터는 {status['min_draw']}~{status['max_draw']}회({status['draws']}회분)만 있습니다. 전체 1회~최신회차 복구 전에는 추천·시뮬레이션을 잠급니다.")


tabs=st.tabs(['🏠 대시보드','🔄 차기회차 보정','🎲 번호 추천','✅ 종합 검증'])
with tabs[0]:
    st.subheader('대시보드 · 운영 현황')
    _op_left,_op_right=st.columns([1.25,1])
    with _op_left:
        st.markdown('<div class="ops-title">🧠 누적 학습 · 사후평가</div>',unsafe_allow_html=True)
        if _new_learning_reports:
            _lrpt=_new_learning_reports[-1]
            st.success(f"제{_lrpt['target_draw']}회 이전 추천 자동평가 완료 · 최고 {_lrpt['best_hits']}개 일치")
        if _learning_summary.get('available'):
            _la,_lb=st.columns(2)
            _la.metric('평가 누적',f"{_learning_summary['evaluated_draws']}회")
            _lb.metric('평균 최고 일치',f"{_learning_summary['avg_best_hits']:.2f}개")
            _lc,_ld=st.columns(2)
            _lc.metric('3개+ 발생률',f"{100*_learning_summary['three_plus_rate']:.1f}%")
            _ld.metric('최근10회 평균',f"{_learning_summary['recent10_avg_best']:.2f}개")
            if _learning_profile.get('available'):
                st.caption(f"누적학습 보정 한도: 최대 {_learning_profile.get('max_bonus',2.0):.0f}점")
        else:
            st.info('추천 → 추첨 → 최신 전체이력 복구·동기화를 반복하면 사후평가가 자동 누적됩니다.')
    with _op_right:
        st.markdown('<div class="ops-title">📥 데이터 직접 검증</div>',unsafe_allow_html=True)
        if status.get('complete_from_draw1'):
            _audit_xlsx=_history_xlsx_bytes(df,status)
            _xlsx_name=f'MD_LOTTO_1_to_{int(status["max_draw"])}_history_audit.xlsx'
            st.download_button(
                '📊 1회~최신회차 Excel 다운로드',
                data=_audit_xlsx,
                file_name=_xlsx_name,
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                use_container_width=True
            )
            st.caption(f"1회~{int(status['max_draw'])}회 · 누락 없는 현재 분석 데이터")
        else:
            st.warning('전체이력 복구 후 Excel 검증이 활성화됩니다.')

    st.divider()
    st.subheader('데이터·무작위성 진단'); audit=randomness_audit(df); struct=structure_summary(df)
    st.markdown(
        f'''<div class="compact-audit-row">
        <div class="compact-audit"><span>전체 회차</span><b>{status['draws']:,}</b></div>
        <div class="compact-audit"><span>연속 데이터</span><b>{'정상' if status['contiguous'] else '점검 필요'}</b></div>
        <div class="compact-audit"><span>균등성 검정</span><b>{'특이점 없음' if audit.get('p_value',0)>=.05 else '검토 필요'}</b></div>
        </div>''',
        unsafe_allow_html=True
    )
    st.caption(f"번호합 평균 {struct.get('sum_mean',0):.1f} · 10~90% 범위 {struct.get('sum_q10',0):.0f}~{struct.get('sum_q90',0):.0f} · 흔한 홀수 개수 {struct.get('odd_mode','-')}개")
    _lr=latest_transition_report(df)
    if _lr.get('available'):
        st.info(f"최근 {_lr['previous_draw']}회→{_lr['current_draw']}회 변화: 직전번호 재등장 {int(_lr['current_features']['overlap_prev'])}개 · 연속수 {int(_lr['current_features']['consecutive_pairs'])}쌍 · 번호합 {int(_lr['previous_features']['sum'])}→{int(_lr['current_features']['sum'])}")

    _today=pd.Timestamp.now(tz='Asia/Seoul').tz_localize(None).normalize()
    _one_year_ago=_today-pd.Timedelta(days=365)
    _recent=df[(df['draw_date']>=_one_year_ago)&(df['draw_date']<=_today)].copy()
    _counts={n:0 for n in range(1,46)}
    for _,_r in _recent.iterrows():
        for _i in range(1,7):
            _counts[int(_r[f'n{_i}'])]+=1
    _chart=pd.DataFrame({'번호':list(range(1,46)),'최근 1년 출현':[_counts[n] for n in range(1,46)]})
    _chart['번호대']=_chart['번호'].map(lambda n:'1-10' if n<=10 else '11-20' if n<=20 else '21-30' if n<=30 else '31-40' if n<=40 else '41-45')
    st.markdown('#### 최근 1년 번호별 출현 빈도')
    st.caption(f"{_one_year_ago.strftime('%Y-%m-%d')} ~ {_today.strftime('%Y-%m-%d')} · 본번호 6개 기준 · 번호대별 색상 적용")
    _color_map={'1-10':'#FFD400','11-20':'#0F8DF5','21-30':'#F5232C','31-40':'#484E55','41-45':'#18B956'}
    fig=px.bar(_chart,x='번호',y='최근 1년 출현',color='번호대',color_discrete_map=_color_map,category_orders={'번호대':['1-10','11-20','21-30','31-40','41-45']},hover_data={'번호':True,'최근 1년 출현':True,'번호대':True})
    fig.update_layout(margin=dict(l=0,r=0,t=15,b=0),height=350,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font_color='#aeb8c8',legend_title_text='번호대',xaxis=dict(dtick=1),yaxis_title='출현 횟수')
    st.plotly_chart(fig,use_container_width=True)
with tabs[1]:
    st.subheader('🔄 차기회차 보정전략')
    st.caption('지난 추천과 실제 당첨결과의 차이, 최신 회차 변화, FDR·백테스트·AI 검증을 내부에서 종합해 다음 5조합 생성 전에 적용할 보정안을 만듭니다.')
    if st.button('🔄 최신 결과 반영 · 보정전략 계산',type='primary',use_container_width=True):
        with st.spinner('지난 결과 진단 → FDR → 백테스트 → AI 검증 → 차기회차 보정안 생성 중...'):
            _cp=_get_current_correction(force=True)
    else:
        _cp=st.session_state.get('integrated_correction_plan')

    if _cp and int(_cp.get('basis_draw',-1))==int(latest.draw_no):
        _cc=st.columns(4)
        _cc[0].metric('지난 결과 진단',_cp.get('failure_type','-'))
        _cc[1].metric('FDR',_cp.get('fdr_status','-'))
        _cc[2].metric('백테스트',_cp.get('backtest_status','-'))
        _cc[3].metric('AI 진단',_cp.get('ai_status','-'))
        st.markdown(f"### 🎯 제{int(_cp['target_draw'])}회 적용 대책")
        for _a in _cp.get('actions',[]):
            st.write('→ '+_a)
        st.success(f"추천엔진 적용값: 후보 Pool {_cp.get('pool_size',20)}개 · 조합간 최대중복 {_cp.get('max_overlap',3)}개 · 보정강도 최대 {_cp.get('max_bonus',2):.0f}점 · {_cp.get('overall_status','보정 적용')}")
        st.caption('이 보정은 실제 당첨확률을 계산하는 것이 아니라, 지난 실패유형과 검증결과를 다음 회차 후보선정·조합배치에 제한적으로 반영하는 장치입니다.')
    else:
        st.info('보정전략을 먼저 계산해 주세요. 번호 추천 버튼을 눌러도 보정전략이 없으면 자동으로 계산한 뒤 추천을 생성합니다.')

with tabs[2]:
    _adj=next_draw_adjustment_report(df)
    if _adj.get('available'):
        _tr=_adj['transition']; _pf=_adj.get('profile',{})
        st.markdown('### 🔁 전회차 대비 변화와 다음회차 보완')
        st.caption(f"{_tr['previous_draw']}회 → {_tr['current_draw']}회 실제 당첨번호 변화 분석")
        _cols=st.columns(4)
        _cols[0].metric('직전번호 재등장',f"{int(_tr['current_features']['overlap_prev'])}개")
        _cols[1].metric('연속수 Pair',f"{int(_tr['current_features']['consecutive_pairs'])}쌍")
        _cols[2].metric('번호합',f"{int(_tr['current_features']['sum'])}")
        _cols[3].metric('홀수',f"{int(_tr['current_features']['odd'])}개")
        with st.expander('무엇이 달라졌고 다음 회차에 어떻게 반영하는지 보기'):
            for _line in _tr.get('explanations',[]): st.write('• '+_line)
            st.markdown('**다음회차 보완책**')
            for _line in _adj.get('actions',[]): st.write('→ '+_line)
            _cg=_tr.get('current_consecutive_gap',0); _ag=_tr.get('historical_consecutive_avg_gap')
            if pd.notna(_ag): st.caption(f"연속수 과거 평균 출현간격 약 {_ag:.1f}회 · 현재 연속수 미출현 간격 {_cg}회")
    st.markdown('### 🧬 주간 자기학습 엔진')
    if _evolution_plan.get('available'):
        _evs=_evolution_plan.get('selected',{})
        _ec=st.columns(4)
        _ec[0].metric('재학습 검증',f"{int(_evolution_plan.get('evaluated_weeks',0))}주")
        _ec[1].metric('학습 모드',str(_evolution_plan.get('mode','-')))
        _ec[2].metric('후보 Pool',f"{int(_evolution_plan.get('pool_size',20))}개")
        _ec[3].metric('5조합 최대중복',f"{int(_evolution_plan.get('max_overlap',3))}개")
        st.caption(
            f"선택모델: 최근창 {int(_evs.get('window',0))}회 · 최근가중 {float(_evs.get('recent_weight',0)):.2f} · "
            f"최근10주 후보군 평균적중 {float(_evs.get('recent10_pool_hits',0)):.2f}개 · "
            f"동일 크기 무작위 기대 {float(_evs.get('random_expected_hits',0)):.2f}개"
        )
        st.caption('새 당첨번호가 들어올 때마다 과거 각 주를 그 이전 데이터만으로 다시 예측해 모델을 재선택합니다. 실제 로또 추첨은 독립·무작위이므로 이 학습은 추천 랭킹과 분산을 개선하는 연구 기능이며 당첨확률 상승을 보장하지 않습니다.')
    else:
        st.caption('자기학습 대기: '+str(_evolution_plan.get('reason','자기학습 대기')))
    st.markdown('### 📈 학습 진화 리포트')
    if _evolution_report.get('available'):
        _rr=_evolution_report
        _rc=st.columns(4)
        _rc[0].metric('최근 12주 평균적중',f"{float(_rr.get('avg_hits',0)):.2f}개")
        _rc[1].metric('무작위 기대',f"{float(_rr.get('expected',0)):.2f}개")
        _rc[2].metric('기대대비',f"{float(_rr.get('lift',0)):+.2f}개")
        _rc[3].metric('최근 추세',str(_rr.get('trend_label','-')))
        _rdf=pd.DataFrame(_rr.get('rows',[]))
        if len(_rdf):
            st.dataframe(_rdf.tail(12),use_container_width=True,hide_index=True)
        st.caption(str(_rr.get('summary','')))
        st.caption('※ 후보군 적중은 5조합의 실제 당첨을 뜻하지 않습니다. 동일 크기 무작위 후보군의 기대값과 함께 표시하여 학습이 단순히 후보 수를 늘려 좋아 보이는 착시를 줄였습니다.')
    else:
        st.caption(str(_evolution_report.get('summary','학습진화 리포트 대기')))
    subt=st.tabs(['🎯 최종 5조합','🧠 통합 최적화'])
    with subt[0]:
        st.info('차기회차 보정전략을 먼저 적용한 뒤 전체 과거패턴·최근 변화·연속수 주기·유사상태 흐름을 종합해 5조합만 제시합니다. 보정전략이 없으면 추천 버튼을 누를 때 자동 계산합니다.')
        if st.button('🎯 이번 회차 우선순위 5조합 만들기',type='primary',use_container_width=True):
            if not status.get('complete_from_draw1'):
                st.error('전체 과거회차 데이터가 아직 복구되지 않았습니다. 21개 내장 Seed만으로는 패턴이 왜곡될 수 있어 추천을 중단합니다. 사이드바의 「지금 최신 데이터 확인」으로 전체 회차를 먼저 복구해 주세요.')
            else:
                with st.spinner('과거 전체패턴과 최근 회차 변화까지 종합 분석하는 중...'):
                    _cp=_get_current_correction()
                    _base_games=adaptive_priority_five(
                        df,ns,
                        pool_size=int(_cp.get('pool_size',20)),
                        max_overlap=int(_cp.get('max_overlap',3)),
                        correction=_cp
                    )
                    st.session_state['md_games']=_base_games
                    _learning_profile=learning_profile(learning_path)
                    st.session_state['md_recommendation_record']={
                        'target_draw':int(latest.draw_no)+1,
                        'created_from_draw':int(latest.draw_no),
                        'games':[list(map(int,c)) for c in st.session_state['md_games'].combo.tolist()],
                        'mode':'V7_8_1_DEPLOY_FIXED_PRIORITY5'
                    }
                    record_recommendation(
                        learning_path,
                        target_draw=int(latest.draw_no)+1,
                        created_from_draw=int(latest.draw_no),
                        games=st.session_state['md_games'].combo.tolist(),
                        meta={
                            'mode':'pattern_priority5',
                            'learning_profile':_learning_profile
                        }
                    )
        games=st.session_state.get('md_games')
        _rec_basis=st.session_state.get('md_recommendation_record') or {}
        if games is not None and len(games) and int(_rec_basis.get('created_from_draw',-1))!=int(latest.draw_no):
            st.session_state.pop('md_games',None)
            st.session_state.pop('md_recommendation_record',None)
            games=None
            st.info('새 당첨회차가 반영되어 이전 추천은 자동 폐기했습니다. 이번 회차 기준으로 다시 생성해 주세요.')
        if games is not None and len(games):
            _display_games=[list(map(int,g)) for g in games.combo.tolist()]
            _target_draw=int(latest.draw_no)+1
            _target_date=pd.Timestamp(latest.draw_date)+pd.Timedelta(days=7)
            _img=recommendation_image_bytes(_display_games,_target_draw,int(latest.draw_no),_target_date)
            st.image(_img,use_container_width=True,caption=f'제 {_target_draw}회 우선순위 최종 5조합')
            st.download_button(
                '🖼️ 5조합 이미지(PNG) 다운로드',
                data=_img,
                file_name=f'MD_LOTTO_{_target_draw}_FINAL5.png',
                mime='image/png',
                use_container_width=True
            )
            st.caption('5조합 전체를 한 화면에 표시합니다. 개별 조합 설명은 제거했습니다.')
            _wc=_weekly_prediction_compare(learning_path,df,_display_games,_target_draw)
            st.markdown('#### 📊 전주 추천 vs 금주 예측 비교')
            if _wc and _wc.get('previous_target'):
                _pl=f"제{_wc['previous_target']}회 추천"; _cl=f"제{_wc['current_target']}회 예측"
                _cmp=[
                    {'비교항목':'후보번호 수',_pl:len(_wc['previous_union']),_cl:len(_wc['current_union']),'분석':'분산 범위'},
                    {'비교항목':'공통 유지번호',_pl:'-',_cl:' '.join(map(str,_wc['common'])) or '-','분석':f"{len(_wc['common'])}개 유지"},
                    {'비교항목':'신규 편입번호',_pl:'-',_cl:' '.join(map(str,_wc['added'])) or '-','분석':f"{len(_wc['added'])}개 교체"},
                    {'비교항목':'제외된 번호',_pl:' '.join(map(str,_wc['removed'])) or '-',_cl:'-','분석':f"{len(_wc['removed'])}개 제외"}]
                if _wc.get('previous_best_hits') is not None:
                    _cmp.append({'비교항목':'전주 실제평가',
                                 _pl:f"최고 {_wc['previous_best_hits']}개 · 후보군 {_wc['previous_union_hits']}개 적중",
                                 _cl:'추첨 전','분석':'실제 결과 기준'})
                st.dataframe(pd.DataFrame(_cmp),use_container_width=True,hide_index=True)
                if _wc.get('ticket_overlap'):
                    st.dataframe(pd.DataFrame(_wc['ticket_overlap']),use_container_width=True,hide_index=True)
                st.caption('전주에 실제 저장된 추천번호와 금주 예측을 비교합니다. 유지·교체·조합중복을 다음 회차 분산전략 판단에 사용합니다.')
            else:
                st.info('전주 저장 추천이 아직 없습니다. 이번 추천부터 기록되어 다음 회차부터 비교표가 자동 생성됩니다.')
        else:
            st.info('「이번 회차 우선순위 5조합 만들기」를 누르세요.')
    with subt[1]:
        _tb=five_ticket_threeplus_theoretical_bounds()
        st.info(f'목표: 5조합의 3개 이상 적중 커버리지를 가능한 한 높입니다. 하지만 5게임만으로는 수학적 한계가 있습니다. 단일 게임의 3개+ 확률은 약 {100*_tb["single_3plus"]:.2f}%이고, 5게임 전체의 3개+ 커버리지는 합집합 상한으로 최대 {100*_tb["max_5ticket_3plus_union_bound"]:.2f}%를 넘을 수 없습니다. 따라서 미당첨률 50% 이하는 5게임 조건에서는 불가능하며, 이론적 절대 하한도 약 {100*_tb["min_5ticket_miss_union_bound"]:.2f}%입니다.')
        if st.button('🧠 통합 최적화 시뮬레이션 실행',use_container_width=True,type='primary'):
            if not status.get('complete_from_draw1'):
                st.error('전체 과거회차 복구 후 실행해 주세요.')
            else:
                with st.spinner('FDR 패턴검증 → 백테스트 → AI 진단 → 후보확대 → 미당첨률 최소화 탐색 중...'):
                    _fdr=fdr_summary(df)
                    _bt=cached_mobile_backtest(int(latest.draw_no),30)
                    _bts=summarize_backtest(_bt) if _bt is not None and len(_bt) else {}
                    _ml=cached_mobile_ml_holdout(int(latest.draw_no))

                    # FDR/백테스트/AI는 번호를 "확정"하지 않고 과적합 방지용 검증 게이트로 사용.
                    _evidence={
                        'fdr_pair_sig':int(_fdr.get('pair_fdr_significant',0)),
                        'fdr_triple_sig':int(_fdr.get('triple_fdr_significant',0)),
                        'backtest':_bts,
                        'ml':_ml,
                    }
                    _cp=_get_current_correction()
                    _batches=[]
                    for _n in (24,36,48):
                        _cdf=corrected_candidate_games(
                            df,ns,correction=_cp,limit=_n,
                            pool_size=max(22,int(_cp.get('pool_size',20)))
                        )
                        _batches.append(_cdf.combo.tolist())
                    _simopt=converge_min_miss_portfolio(_batches,ns,stages=(10000,25000,50000),max_overlap=3)
                    _simopt['evidence']=_evidence
                    st.session_state['sim_optimizer_result']=_simopt
                    record_recommendation(
                        learning_path,
                        target_draw=int(latest.draw_no)+1,
                        created_from_draw=int(latest.draw_no),
                        games=_simopt['selected_games'],
                        meta={
                            'mode':'integrated_simulation_final5',
                            'pattern_miss_rate':float(_simopt.get('miss_rate_pattern',1.0)),
                            'evidence':_evidence
                        }
                    )
                    # 최종 추천 화면에서도 통합 최적화 결과를 사용할 수 있게 연결.
                    st.session_state['md_sim_final_games']=[list(g) for g in _simopt['selected_games']]

        _so=st.session_state.get('sim_optimizer_result')
        if _so:
            _final_games=[list(map(int,g)) for g in _so['selected_games']]
            _target_draw=int(latest.draw_no)+1
            _target_date=pd.Timestamp(latest.draw_date)+pd.Timedelta(days=7)
            _final_img=recommendation_image_bytes(_final_games,_target_draw,int(latest.draw_no),_target_date)
            st.image(_final_img,use_container_width=True,caption=f'제 {_target_draw}회 통합 분석 최종 5조합')
            st.download_button(
                '🖼️ 최종 5조합 이미지(PNG) 다운로드',
                data=_final_img,
                file_name=f'MD_LOTTO_{_target_draw}_OPTIMIZED_FINAL5.png',
                mime='image/png',
                use_container_width=True
            )

            _miss=100*_so['miss_rate_pattern']; _fairmiss=100*_so['miss_rate_fair']
            _c=st.columns(3)
            _c[0].metric('패턴모델 미당첨률',f'{_miss:.2f}%')
            _c[1].metric('패턴모델 3개+ 커버리지',f"{100*_so['pattern_model']['any3plus']:.2f}%")
            _c[2].metric('패턴모델 4개+ 커버리지',f"{100*_so['pattern_model']['any4plus']:.2f}%")
            _tb=five_ticket_threeplus_theoretical_bounds()
            _ach=float(_so['pattern_model']['any3plus'])
            _upper=float(_tb['max_5ticket_3plus_union_bound'])
            _eff=(_ach/_upper*100) if _upper>0 else 0
            _gap=max(0.0,(_upper-_ach)*100)
            _d=st.columns(3)
            _d[0].metric('5게임 이론상 미당첨 하한',f"{100*_tb['min_5ticket_miss_union_bound']:.2f}%")
            _d[1].metric('3개+ 상한 대비 효율',f"{_eff:.1f}%")
            _d[2].metric('이론상 상한까지 격차',f"{_gap:.2f}%p")
            if _eff>=90:
                st.success('현재 5조합은 5게임의 이론상 3개+ 커버리지 상한에 매우 근접한 편입니다. 더 큰 폭의 개선은 번호 교체만으로는 어렵고 게임 수 확대가 필요합니다.')
            elif _eff>=80:
                st.info('현재 조합은 5게임 이론상 커버리지 상한의 80% 이상입니다. 추가 탐색은 가능하지만 개선폭은 제한적일 수 있습니다.')
            else:
                st.warning('현재 조합의 커버리지 효율이 낮아 후보공간 확대와 조합 중복 억제를 계속 탐색합니다.')
            st.markdown('#### ✅ 내부 검증 종합 결과')
            _ev=_so.get('evidence',{})
            _ml=_ev.get('ml') or {}
            _btok=bool((_ev.get('backtest') or {}).get('evidence_of_edge',False))
            _aiok=bool(_ml.get('available') and _ml.get('beats_constant_logloss'))
            _fok=bool(_ev.get('fdr_pair_sig',0) or _ev.get('fdr_triple_sig',0))
            _vc=st.columns(3)
            _vc[0].metric('FDR 검증','패턴 확인' if _fok else '보수 적용')
            _vc[1].metric('백테스트','검증 통과' if _btok else '근거 제한')
            _vc[2].metric('AI 진단','검증 통과' if _aiok else '보수 적용')
            st.caption('FDR·백테스트·AI의 세부 통계는 내부에서 계산하며, 화면에는 최종 판단만 표시합니다.')
            st.metric('5게임 1등 이론확률',f"1 / {round(1/_so['theoretical_first_probability_5tickets']):,}")
            st.markdown('#### 🛠️ 미당첨률을 더 낮추기 위한 현실적 대책')
            st.write('① 5조합 내부 번호 중복을 줄여 서로 다른 당첨영역을 넓힙니다. ② FDR에서 우연성이 높은 Pair·Triple은 가중치를 낮춥니다. ③ 백테스트에서 랜덤보다 반복적으로 약한 전략은 제외합니다. ④ AI Holdout이 기본모델을 이기지 못하면 AI 가중치를 강화하지 않습니다. ⑤ 5게임 한계를 넘는 큰 폭의 미당첨률 감소가 목표라면 조합 수 자체를 늘려야 합니다.')
            st.warning('중요: 로또 추첨이 공정하고 독립적이라면 서로 다른 5게임의 1등 이론확률은 번호 구성과 무관하게 동일합니다. 여기서 최소화하는 “미당첨률”은 연구용 시뮬레이션 목적함수이며 실제 미래 당첨확률 보장이 아닙니다.')
with tabs[3]:
    st.subheader('✅ 종합 검증 결과')
    st.caption('FDR·백테스트·AI·지난 추천 오차분석은 내부에서 실행합니다. 여기서는 다음 회차 추천에 실제로 어떤 판단이 반영되는지만 간단히 보여줍니다.')
    if st.button('✅ 종합 검증 새로 실행',use_container_width=True):
        with st.spinner('내부 검증을 다시 계산하는 중...'):
            _vp=_get_current_correction(force=True)
    else:
        _vp=st.session_state.get('integrated_correction_plan')

    if _vp and int(_vp.get('basis_draw',-1))==int(latest.draw_no):
        st.markdown('#### 🎯 다음 추천에 실제 반영되는 값')
        _v=st.columns(3)
        _v[0].metric('후보 Pool',f"{int(_vp.get('pool_size',20))}개")
        _v[1].metric('조합 최대중복',f"{int(_vp.get('max_overlap',3))}개")
        _v[2].metric('보정강도',f"{float(_vp.get('max_bonus',2)):.0f}점")
        if _vp.get('overall_status')=='보정 적용':
            st.success(f"종합판정: 제{int(_vp['target_draw'])}회 추천에 보정전략을 적용합니다.")
        else:
            st.info('종합판정: 강한 보정 근거가 부족해 기본전략을 유지합니다.')
        st.markdown('#### 프로그램이 실제로 바꾸는 것')
        st.write(f"• 후보번호 탐색범위: {_vp.get('pool_size',20)}개")
        st.write(f"• 5조합 간 최대 중복: {_vp.get('max_overlap',3)}개")
        st.write(f"• Pair 영향력: {'축소' if float(_vp.get('pair_scale',1))<1 else '기본 유지'}")
        st.write(f"• 차기회차 구조 보정 강도: 최대 {_vp.get('max_bonus',2):.0f}점")
        st.caption('FDR·백테스트·AI는 내부 검증용으로 유지하고, 화면에는 추천 생성에 실제 반영되는 Pool·중복·보정강도만 표시합니다.')
    else:
        st.info('아직 이번 회차 기준 종합 검증이 없습니다. 차기회차 보정 메뉴에서 계산하거나 번호 추천을 실행하면 자동 생성됩니다.')

st.caption('MD LOTTO 6/45 · v8.0 FINAL COMPLETE · 모든 특정 6개 조합의 1등 확률은 동일합니다.')
