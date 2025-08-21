import streamlit as st
from itertools import combinations

# ===============================
# 페이지 & 전역 스타일
# ===============================
st.set_page_config(page_title="주기율표 결합 학습 (1~5주기)", layout="wide")

st.markdown("""
<style>
body { background: linear-gradient(135deg, #E9F6FF 0%, #FFFFFF 65%); }

/* 희미한 과학 스티커 느낌 이모지 */
.stApp:before, .stApp:after {
  content: "🧪  🔬  ⚗️  🧬";
  position: fixed; z-index: -1; font-size: 40px; opacity: .06; color: #0c6cd4;
}
.stApp:before { top: 6%; left: 5%; transform: rotate(-10deg); }
.stApp:after  { bottom: 7%; right: 6%; transform: rotate(12deg); }

/* 셀 스타일: 네모 + 둥근 모서리 */
.cell {
  border-radius: 12px;
  padding: 6px 6px;
  margin: 4px 2px;
  border: 1px solid rgba(0,0,0,.08);
  box-shadow: 0 1px 6px rgba(0, 70, 140, .07);
  text-align: center;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", Arial, "Helvetica Neue", Helvetica, sans-serif;
  min-height: 44px;
}
.cell:hover { box-shadow: 0 4px 12px rgba(0, 70, 140, .12); }
.cell .line { font-weight: 800; font-size: 13px; line-height: 1; }

/* 정보 카드 */
.card {
  background:#fff; border-left:6px solid #1c6dd0; padding:12px 14px; margin:10px 0;
  border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,.05)
}

/* 체크박스 간격 줄이기 */
.block-container .stCheckbox { margin-top: -6px; }
</style>
""", unsafe_allow_html=True)

st.title("🔬 주기율표 결합 학습 (1~5주기, #1~#54)")
st.caption("금속: 하늘색, 준금속·비금속: 노란색. 칸을 토글(체크)해 선택하세요. "
           "두 개 이상 선택하면 결합 종류·특징·생성 물질의 성질을 보여줍니다.")

COLOR_METAL = "#ADD8E6"
COLOR_NONMET = "#FFF8B5"  # 준금속·비금속 공통

def cell_color(category: str) -> str:
    return COLOR_METAL if category == "금속" else COLOR_NONMET

# =========================================================
# 1~54번(1~5주기) 원소 데이터:
# (Z, Sym, Name, Category[금속/준금속/비금속], Feature, Period, Group)
# =========================================================
E = [
 (1,"H","수소","비금속","가장 가벼움·연료·환원제",1,1),
 (2,"He","헬륨","비금속","불활성 기체·극저온 냉각",1,18),

 (3,"Li","리튬","금속","알칼리 금속·2차전지",2,1),
 (4,"Be","베릴륨","금속","가볍고 강함·항공합금",2,2),
 (5,"B","붕소","준금속","유리·세라믹·반도체 도핑",2,13),
 (6,"C","탄소","비금속","생명 기본·흑연/다이아",2,14),
 (7,"N","질소","비금속","대기 78%·비료·냉각",2,15),
 (8,"O","산소","비금속","호흡·강한 산화제",2,16),
 (9,"F","플루오린","비금속","전기음성도 최고·반응성 큼",2,17),
 (10,"Ne","네온","비금속","불활성 기체·방전등",2,18),

 (11,"Na","나트륨","금속","소금 구성·반응성 큼",3,1),
 (12,"Mg","마그네슘","금속","가벼운 합금·엽록소",3,2),
 (13,"Al","알루미늄","금속","가벼움·내식성",3,13),
 (14,"Si","규소","준금속","반도체 핵심·규사",3,14),
 (15,"P","인","비금속","DNA·ATP·비료",3,15),
 (16,"S","황","비금속","황산·가황·비료",3,16),
 (17,"Cl","염소","비금속","소독·PVC",3,17),
 (18,"Ar","아르곤","비금속","불활성 기체·용접",3,18),

 (19,"K","칼륨","금속","알칼리 금속·비료",4,1),
 (20,"Ca","칼슘","금속","뼈/치아·석회석",4,2),
 (21,"Sc","스칸듐","금속","경량 합금",4,3),
 (22,"Ti","티타늄","금속","강·가벼움·임플란트",4,4),
 (23,"V","바나듐","금속","강철 첨가",4,5),
 (24,"Cr","크로뮴","금속","스테인리스·도금",4,6),
 (25,"Mn","망간","금속","강철 합금",4,7),
 (26,"Fe","철","금속","강철·핵심 금속",4,8),
 (27,"Co","코발트","금속","배터리·자석",4,9),
 (28,"Ni","니켈","금속","스테인리스·도금",4,10),
 (29,"Cu","구리","금속","전도 우수·전선",4,11),
 (30,"Zn","아연","금속","도금·배터리",4,12),
 (31,"Ga","갈륨","금속","GaN/LED·반도체",4,13),
 (32,"Ge","게르마늄","준금속","반도체·적외선",4,14),
 (33,"As","비소","준금속","도핑·독성",4,15),
 (34,"Se","셀레늄","비금속","광전·미량원소",4,16),
 (35,"Br","브로민","비금속","액체 할로젠·난연",4,17),
 (36,"Kr","크립톤","비금속","방전등·레이저",4,18),

 (37,"Rb","루비듐","금속","알칼리·원자시계",5,1),
 (38,"Sr","스트론튬","금속","적색 불꽃·세라믹",5,2),
 (39,"Y","이트륨","금속","형광체·초전도",5,3),
 (40,"Zr","지르코늄","금속","내식·원자로 피복",5,4),
 (41,"Nb","나이오븀","금속","초전도·합금",5,5),
 (42,"Mo","몰리브데넘","금속","고온 합금·촉매",5,6),
 (43,"Tc","테크네튬","금속","의학 방사성 동위원소",5,7),
 (44,"Ru","루테늄","금속","촉매·전극",5,8),
 (45,"Rh","로듐","금속","자동차 촉매",5,9),
 (46,"Pd","팔라듐","금속","촉매·수소 흡장",5,10),
 (47,"Ag","은","금속","전도 최고·귀금속",5,11),
 (48,"Cd","카드뮴","금속","배터리·독성",5,12),
 (49,"In","인듐","금속","ITO·디스플레이",5,13),
 (50,"Sn","주석","금속","땜납·도금",5,14),
 (51,"Sb","안티몬","준금속","난연·반도체",5,15),
 (52,"Te","텔루륨","준금속","열전·태양전지",5,16),
 (53,"I","아이오딘","비금속","소독·갑상선",5,17),
 (54,"Xe","제논","비금속","헤드램프·마취",5,18),
]

# 빠른 접근용 딕셔너리
by_sym = {sym: dict(Z=Z, Sym=sym, Name=nm, Cat=cat, Feat=feat, P=p, G=g) for (Z, sym, nm, cat, feat, p, g) in E}

# ===============================
# 선택 상태
# ===============================
if "sel" not in st.session_state:
    st.session_state.sel = set()

# ===============================
# 주기율표 그리드 (1~5주기, 18족)
# None은 빈 칸
# ===============================
def empty_cell():
    st.write("")

def render_element(sym):
    e = by_sym[sym]
    bg = cell_color(e["Cat"])
    st.markdown(
        f'<div class="cell" style="background:{bg}"><div class="line">#{e["Z"]} {e["Sym"]}</div></div>',
        unsafe_allow_html=True
    )
    # 토글 체크박스 (작고 라벨 숨김)
    checked = st.checkbox(" ", key=f"chk_{sym}", value=(sym in st.session_state.sel), label_visibility="collapsed")
    if checked: st.session_state.sel.add(sym)
    else: st.session_state.sel.discard(sym)

# 실제 배치 (1~5주기)
period_rows = {
    1: ["H"] + [None]*16 + ["He"],
    2: ["Li","Be"] + [None]*10 + ["B","C","N","O","F","Ne"],
    3: ["Na","Mg"] + [None]*10 + ["Al","Si","P","S","Cl","Ar"],
    4: ["K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr"],
    5: ["Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe"],
}

st.subheader("📋 주기율표 (1~5주기)")
for period in range(1, 6):
    st.markdown(f"**{period} 주기**")
    row = period_rows[period]
    cols = st.columns(18)
    for i, col in enumerate(cols):
        with col:
            sym = row[i] if i < len(row) else None
            if sym is None:
                empty_cell()
            else:
                render_element(sym)

# ===============================
# 선택한 원소 정보
# ===============================
selected = [by_sym[s] for s in sorted(st.session_state.sel, key=lambda s: by_sym[s]["Z"])]

if selected:
    st.subheader("📌 선택한 원소")
    for e in selected:
        st.markdown(
            f"""
            <div class="card" style="border-left-color:#1c6dd0">
              <b>#{e['Z']} {e['Sym']} — {e['Name']}</b><br/>
              분류: {e['Cat']}<br/>
              특징: {e['Feat']}
            </div>
            """,
            unsafe_allow_html=True
        )

# ===============================
# 결합 로직 (학습용 단순화)
# ===============================
def bond_info(cat1, cat2):
    metals = {"금속"}
    nonmet_like = {"비금속", "준금속"}
    if cat1 in metals and cat2 in metals:
        return ("금속 결합",
                "자유 전자(전자 바다)가 금속 양이온 사이를 매개.",
                "전기·열 전도 우수, 광택/연성/전성, 결정격자.")
    if (cat1 in metals and cat2 in nonmet_like) or (cat2 in metals and cat1 in nonmet_like):
        return ("이온 결합",
                "금속이 전자를 잃어 양이온, 비/준금속이 받아 음이온 → 정전기 인력.",
                "높은 융점/끓는점, 용융·수용액에서 전도, 단단한 결정.")
    return ("공유 결합",
            "전자쌍을 공유하여 분자·거대공유결정 형성.",
            "분자는 비교적 낮은 융/끓는점, 전도성 낮음(흑연 예외), 방향성.")

if len(selected) >= 2:
    st.subheader("🔗 결합 분석")
    for a, b in combinations(selected, 2):
        btype, bdesc, mprop = bond_info(a["Cat"], b["Cat"])
        st.markdown(
            f"""
            <div class="card">
              <div><b>{a['Name']}({a['Sym']}) + {b['Name']}({b['Sym']})</b></div>
              <div>결합 종류: <b>{btype}</b></div>
              <div>결합 특징: {bdesc}</div>
              <div>생성 물질의 성질: {mprop}</div>
              <details style="margin-top:8px;">
                <summary>각 원소 특징 다시 보기</summary>
                <div style="padding-top:6px;">
                  • #{a['Z']} {a['Sym']} ({a['Cat']}): {a['Feat']}<br/>
                  • #{b['Z']} {b['Sym']} ({b['Cat']}): {b['Feat']}
                </div>
              </details>
            </div>
            """,
            unsafe_allow_html=True
        )

# ===============================
# 리셋 버튼
# ===============================
left, right = st.columns([1,3])
with left:
    if st.button("🔄 선택 초기화"):
        for k in list(st.session_state.keys()):
            if k.startswith("chk_"):
                st.session_state[k] = False
        st.session_state.sel = set()
        st.experimental_rerun()

with right:
    st.info("팁: 하늘색(금속) + 노란색(비·준금속)을 함께 선택하면 이온결합 예시를, "
            "노란색끼리는 공유결합, 하늘색끼리는 금속결합 예시가 나옵니다.")
