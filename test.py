import streamlit as st
from itertools import combinations

# ===============================
# 페이지 & 전역 스타일
# ===============================
st.set_page_config(page_title="주기율표 결합 학습", layout="wide")

st.markdown("""
<style>
body { background: linear-gradient(135deg, #E9F6FF 0%, #FFFFFF 65%); }

/* 스티커 느낌의 희미한 이모지 */
.stApp:before, .stApp:after {
  content: "🧪  🔬  ⚗️  🧬";
  position: fixed; z-index: -1; font-size: 40px; opacity: .06; color: #0c6cd4;
}
.stApp:before { top: 6%; left: 5%; transform: rotate(-10deg); }
.stApp:after  { bottom: 7%; right: 6%; transform: rotate(12deg); }

/* 칸(셀) 공통 */
.cell {
  border-radius: 10px; padding: 6px 6px; margin: 4px 2px;
  border: 1px solid rgba(0,0,0,.08);
  box-shadow: 0 1px 6px rgba(0, 70, 140, .07);
  text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", Arial, "Helvetica Neue", Helvetica, sans-serif;
}
.cell:hover { box-shadow: 0 4px 12px rgba(0, 70, 140, .12); }
.cell .line { font-weight: 800; font-size: 13px; line-height: 1; } /* 한 줄 표시 */
.cell .name { font-size: 10px; opacity: .85; }

/* 섹션 구분 카드 */
.card {
  background:#fff; border-left:6px solid #1c6dd0; padding:12px 14px; margin:10px 0;
  border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,.05)
}

/* 체크박스 간격 줄이기 */
.block-container .stCheckbox { margin-top: -6px; }
</style>
""", unsafe_allow_html=True)

st.title("🔬 주기율표 결합 학습 (118 원소)")
st.caption("금속: 하늘색, 준금속·비금속: 노란색. 칸을 토글(체크)해 선택하세요. "
           "두 개 이상 선택하면 결합 종류·특징·생성 물질의 성질을 보여줍니다.")

COLOR_METAL = "#ADD8E6"
COLOR_NONMET = "#FFF8B5"  # 비금속 + 준금속

def cell_color(category: str) -> str:
    return COLOR_METAL if category == "금속" else COLOR_NONMET

# =========================================================
# 118개 원소 데이터 (번호, 기호, 이름, 분류, 특징, 주기, 족)
# 분류: 금속 / 준금속 / 비금속
# 주기/족: 실제 주기율표 배치 (f-블록은 별도)
# 특징은 한 줄 요약(학습용 단순화)
# =========================================================
E = [
 # Z, Sym, Name-KR, Category, Feature, Period, Group
 (1,  "H",  "수소",      "비금속",  "가장 가벼움·연료·환원제", 1, 1),
 (2,  "He", "헬륨",      "비금속",  "불활성 기체·극저온 냉각", 1, 18),
 (3,  "Li", "리튬",      "금속",    "알칼리 금속·2차전지", 2, 1),
 (4,  "Be", "베릴륨",    "금속",    "가볍고 강함·항공합금", 2, 2),
 (5,  "B",  "붕소",      "준금속",  "유리·세라믹·반도체 도핑", 2, 13),
 (6,  "C",  "탄소",      "비금속",  "생명 기본·흑연/다이아", 2, 14),
 (7,  "N",  "질소",      "비금속",  "대기 78%·비료·냉각", 2, 15),
 (8,  "O",  "산소",      "비금속",  "호흡·산화제", 2, 16),
 (9,  "F",  "플루오린",  "비금속",  "전기음성도 최고·반응성 큼", 2, 17),
 (10, "Ne", "네온",      "비금속",  "불활성 기체·방전등", 2, 18),
 (11, "Na", "나트륨",    "금속",    "소금 구성·반응성 큼", 3, 1),
 (12, "Mg", "마그네슘",  "금속",    "가벼운 합금·엽록소", 3, 2),
 (13, "Al", "알루미늄",  "금속",    "가벼움·내식성", 3, 13),
 (14, "Si", "규소",      "준금속",  "반도체 핵심·규사", 3, 14),
 (15, "P",  "인",        "비금속",  "DNA·ATP·비료", 3, 15),
 (16, "S",  "황",        "비금속",  "황산·가황·비료", 3, 16),
 (17, "Cl", "염소",      "비금속",  "소독·PVC", 3, 17),
 (18, "Ar", "아르곤",    "비금속",  "불활성 기체·용접", 3, 18),
 (19, "K",  "칼륨",      "금속",    "알칼리 금속·비료", 4, 1),
 (20, "Ca", "칼슘",      "금속",    "뼈/치아·석회석", 4, 2),
 (21, "Sc", "스칸듐",    "금속",    "경량 합금", 4, 3),
 (22, "Ti", "티타늄",    "금속",    "강·가벼움·임플란트", 4, 4),
 (23, "V",  "바나듐",    "금속",    "강철 첨가", 4, 5),
 (24, "Cr", "크로뮴",    "금속",    "스테인리스·도금", 4, 6),
 (25, "Mn", "망간",      "금속",    "강철 합금", 4, 7),
 (26, "Fe", "철",        "금속",    "강철·핵심 금속", 4, 8),
 (27, "Co", "코발트",    "금속",    "배터리·자석", 4, 9),
 (28, "Ni", "니켈",      "금속",    "스테인리스·도금", 4, 10),
 (29, "Cu", "구리",      "금속",    "전도 우수·전선", 4, 11),
 (30, "Zn", "아연",      "금속",    "도금·배터리", 4, 12),
 (31, "Ga", "갈륨",      "금속",    "GaN/LED·반도체", 4, 13),
 (32, "Ge", "게르마늄",  "준금속",  "반도체·적외선", 4, 14),
 (33, "As", "비소",      "준금속",  "도핑·독성", 4, 15),
 (34, "Se", "셀레늄",    "비금속",  "광전·미량원소", 4, 16),
 (35, "Br", "브로민",    "비금속",  "액체 할로젠·난연", 4, 17),
 (36, "Kr", "크립톤",    "비금속",  "방전등·레이저", 4, 18),
 (37, "Rb", "루비듐",    "금속",    "알칼리·원자시계", 5, 1),
 (38, "Sr", "스트론튬",  "금속",    "적색 불꽃·세라믹", 5, 2),
 (39, "Y",  "이트륨",    "금속",    "형광체·초전도", 5, 3),
 (40, "Zr", "지르코늄",  "금속",    "내식·원자로 피복", 5, 4),
 (41, "Nb", "나이오븀",  "금속",    "초전도·합금", 5, 5),
 (42, "Mo", "몰리브데넘","금속",    "고온 합금·촉매", 5, 6),
 (43, "Tc", "테크네튬",  "금속",    "의학 방사성 동위원소", 5, 7),
 (44, "Ru", "루테늄",    "금속",    "촉매·전극", 5, 8),
 (45, "Rh", "로듐",      "금속",    "자동차 촉매", 5, 9),
 (46, "Pd", "팔라듐",    "금속",    "촉매·수소 흡장", 5, 10),
 (47, "Ag", "은",        "금속",    "전도 최고·귀금속", 5, 11),
 (48, "Cd", "카드뮴",    "금속",    "배터리·독성", 5, 12),
 (49, "In", "인듐",      "금속",    "ITO·디스플레이", 5, 13),
 (50, "Sn", "주석",      "금속",    "땜납·도금", 5, 14),
 (51, "Sb", "안티몬",    "준금속",  "난연·반도체", 5, 15),
 (52, "Te", "텔루륨",    "준금속",  "열전·태양전지", 5, 16),
 (53, "I",  "아이오딘",  "비금속",  "소독·갑상선", 5, 17),
 (54, "Xe", "제논",      "비금속",  "헤드램프·마취", 5, 18),
 (55, "Cs", "세슘",      "금속",    "알칼리·원자시계", 6, 1),
 (56, "Ba", "바륨",      "금속",    "조영제·불꽃", 6, 2),
 # 란타넘계(별행) — 주기 6, 그룹 f-block
 (57, "La", "란타넘",    "금속",    "배터리·촉매", 6, None),
 (58, "Ce", "세륨",      "금속",    "연마·촉매", 6, None),
 (59, "Pr", "프라세오디뮴","금속",  "자석·광학", 6, None),
 (60, "Nd", "네오디뮴",  "금속",    "강자석", 6, None),
 (61, "Pm", "프로메튬",  "금속",    "방사성·희귀", 6, None),
 (62, "Sm", "사마륨",    "금속",    "SmCo 자석", 6, None),
 (63, "Eu", "유로퓸",    "금속",    "형광체 적색", 6, None),
 (64, "Gd", "가돌리늄",  "금속",    "MRI 조영·중성자 흡수", 6, None),
 (65, "Tb", "터븀",      "금속",    "형광체·자석", 6, None),
 (66, "Dy", "디스프로슘","금속",    "자석 열안정", 6, None),
 (67, "Ho", "홀뮴",      "금속",    "레이저·자성", 6, None),
 (68, "Er", "어븀",      "금속",    "광증폭 도핑", 6, None),
 (69, "Tm", "툴륨",      "금속",    "레이저", 6, None),
 (70, "Yb", "이터븀",    "금속",    "레이저·합금", 6, None),
 (71, "Lu", "루테튬",    "금속",    "PET·촉매", 6, None),
 # 주기 6 d/p 블록 계속
 (72, "Hf", "하프늄",    "금속",    "원자로 제어봉", 6, 4),
 (73, "Ta", "탄탈럼",    "금속",    "콘덴서·내식", 6, 5),
 (74, "W",  "텅스텐",    "금속",    "융점↑·공구강", 6, 6),
 (75, "Re", "레늄",      "금속",    "초합금·촉매", 6, 7),
 (76, "Os", "오스뮴",    "금속",    "고밀도·합금", 6, 8),
 (77, "Ir", "이리듐",    "금속",    "내식 최고·촉매", 6, 9),
 (78, "Pt", "백금",      "금속",    "귀금속·촉매", 6, 10),
 (79, "Au", "금",        "금속",    "귀금속·전자", 6, 11),
 (80, "Hg", "수은",      "금속",    "상온 액체·독성", 6, 12),
 (81, "Tl", "탈륨",      "금속",    "전자재료·독성", 6, 13),
 (82, "Pb", "납",        "금속",    "배터리·차폐", 6, 14),
 (83, "Bi", "비스무트",  "금속",    "저독성 합금·의약", 6, 15),
 (84, "Po", "폴로늄",    "준금속",  "방사성 준금속", 6, 16),
 (85, "At", "아스타틴",  "비금속",  "희귀 방사성 할로젠", 6, 17),
 (86, "Rn", "라돈",      "비금속",  "방사성 비활성 기체", 6, 18),
 (87, "Fr", "프랑슘",    "금속",    "희귀 알칼리·방사성", 7, 1),
 (88, "Ra", "라듐",      "금속",    "알칼리토·방사성", 7, 2),
 # 악티늄계(별행) — 주기 7, f-block
 (89, "Ac", "악티늄",    "금속",    "방사성·연구", 7, None),
 (90, "Th", "토륨",      "금속",    "원자로 연료 후보", 7, None),
 (91, "Pa", "프로트악티늄","금속",  "희귀 방사성", 7, None),
 (92, "U",  "우라늄",    "금속",    "원자력 연료", 7, None),
 (93, "Np", "넵투늄",    "금속",    "방사성·연구", 7, None),
 (94, "Pu", "플루토늄",  "금속",    "원자로·핵기술", 7, None),
 (95, "Am", "아메리슘",  "금속",    "연기감지기 방사선원", 7, None),
 (96, "Cm", "퀴륨",      "금속",    "방사성·연구", 7, None),
 (97, "Bk", "버클륨",    "금속",    "인공·연구", 7, None),
 (98, "Cf", "캘리포늄",  "금속",    "중성자원·분석", 7, None),
 (99, "Es", "아인슈타이늄","금속",  "인공·연구", 7, None),
 (100,"Fm", "페르뮴",    "금속",    "인공·연구", 7, None),
 (101,"Md", "멘델레븀",  "금속",    "인공·연구", 7, None),
 (102,"No", "노벨륨",    "금속",    "인공·연구", 7, None),
 (103,"Lr", "로렌슘",    "금속",    "인공·연구", 7, None),
 # 주기 7 d/p 블록 계속
 (104,"Rf", "러더포듐",  "금속",    "초중원소·연구", 7, 4),
 (105,"Db", "더브늄",    "금속",    "초중원소·연구", 7, 5),
 (106,"Sg", "시보귬",    "금속",    "초중원소·연구", 7, 6),
 (107,"Bh", "보륨",      "금속",    "초중원소·연구", 7, 7),
 (108,"Hs", "하슘",      "금속",    "초중원소·연구", 7, 8),
 (109,"Mt", "마이트너륨","금속",    "초중원소·연구", 7, 9),
 (110,"Ds", "다름슈타튬","금속",    "초중원소·연구", 7, 10),
 (111,"Rg", "뢴트게늄",  "금속",    "초중원소·연구", 7, 11),
 (112,"Cn", "코페르니슘","금속",    "초중원소·연구", 7, 12),
 (113,"Nh", "니호늄",    "금속",    "인공 초중원소", 7, 13),
 (114,"Fl", "플레로븀",  "금속",    "인공 초중원소", 7, 14),
 (115,"Mc", "모스코븀",  "금속",    "인공 초중원소", 7, 15),
 (116,"Lv", "리버모륨",  "금속",    "인공 초중원소", 7, 16),
 (117,"Ts", "테네신",    "비금속",  "인공 할로젠 성격", 7, 17),
 (118,"Og", "오가네손",  "비금속",  "가장 무거운 비활성 기체 성격", 7, 18),
]

# 빠른 접근용 딕셔너리
by_sym = {sym: dict(Z=Z, Sym=sym, Name=nm, Cat=cat, Feat=feat, P=p, G=g) for (Z, sym, nm, cat, feat, p, g) in E}

# ===============================
# 선택 상태
# ===============================
if "sel" not in st.session_state:
    st.session_state.sel = set()

# ===============================
# 주기율표 메인 그리드 (1~7주기, 18족)
# f-블록은 별도 두 줄로 렌더
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
    # 작고 라벨 없는 체크박스 (토글)
    checked = st.checkbox(" ", key=f"chk_{sym}", value=(sym in st.session_state.sel), label_visibility="collapsed")
    if checked: st.session_state.sel.add(sym)
    else: st.session_state.sel.discard(sym)

# 각 주기의 실제 그룹 배치
# None은 빈 칸
period_rows = {
    1: ["H"] + [None]*16 + ["He"],
    2: ["Li","Be"] + [None]*10 + ["B","C","N","O","F","Ne"],
    3: ["Na","Mg"] + [None]*10 + ["Al","Si","P","S","Cl","Ar"],
    4: ["K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr"],
    5: ["Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe"],
    6: ["Cs","Ba"] + [None] + ["Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn"],
    7: ["Fr","Ra"] + [None] + ["Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"],
}

st.subheader("📋 주기율표")
for period in range(1, 8):
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

# f-블록(란타넘/악티늄) 표시
st.markdown("**란타넘계 (6주기, f-블록)**")
lan_row = ["La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu"]
lan_cols = st.columns(15)
for i, col in enumerate(lan_cols):
    with col:
        render_element(lan_row[i])

st.markdown("**악티늄계 (7주기, f-블록)**")
act_row = ["Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr"]
act_cols = st.columns(15)
for i, col in enumerate(act_cols):
    with col:
        render_element(act_row[i])

# ===============================
# 선택된 원소 정보
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
        # 체크박스 & 선택상태 모두 해제
        for k in list(st.session_state.keys()):
            if k.startswith("chk_"):
                st.session_state[k] = False
        st.session_state.sel = set()
        st.experimental_rerun()

with right:
    st.info("팁: 하늘색(금속) + 노란색(비·준금속)을 함께 선택하면 이온결합 예시를 볼 수 있어요. "
            "노란색끼리 선택하면 공유결합, 하늘색끼리는 금속결합이 나옵니다.")
