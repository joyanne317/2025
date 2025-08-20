# app.py
# -*- coding: utf-8 -*-
"""
Streamlit 원소주기율표 웹앱
- 118개 원소를 주기율표 레이아웃(18열)로 표시
- 각 원소를 클릭하면 5가지 정보 표시: [실생활 사례, 원소 이름, 원소번호, 원소 특징, 미래 활용 방향]
- 좌측 검색/필터: 심볼, 이름, 그룹, 주기, 계열(알카리/할로겐/전이금속 등)
- 데이터는 코드 내에 내장(오프라인 동작). 필요 시 CSV로 내보내거나 수정 가능.

실행방법
$ streamlit run app.py
"""

import streamlit as st
from dataclasses import dataclass
from typing import Dict, List, Optional

# ------------------------- 기본 데이터 -------------------------
@dataclass
class Element:
    Z: int
    symbol: str
    name: str
    period: int
    group: int

# Z순서 기본 목록 (심볼과 영문명)
# — 간결성을 위해 이름은 영어 표기 사용. 필요하면 한국어 이름으로 바꿔도 됨.
ELEMENTS_ORDERED: List[Element] = [
    Element(1, "H", "Hydrogen", 1, 1),
    Element(2, "He", "Helium", 1, 18),
    Element(3, "Li", "Lithium", 2, 1),
    Element(4, "Be", "Beryllium", 2, 2),
    Element(5, "B", "Boron", 2, 13),
    Element(6, "C", "Carbon", 2, 14),
    Element(7, "N", "Nitrogen", 2, 15),
    Element(8, "O", "Oxygen", 2, 16),
    Element(9, "F", "Fluorine", 2, 17),
    Element(10, "Ne", "Neon", 2, 18),
    Element(11, "Na", "Sodium", 3, 1),
    Element(12, "Mg", "Magnesium", 3, 2),
    Element(13, "Al", "Aluminium", 3, 13),
    Element(14, "Si", "Silicon", 3, 14),
    Element(15, "P", "Phosphorus", 3, 15),
    Element(16, "S", "Sulfur", 3, 16),
    Element(17, "Cl", "Chlorine", 3, 17),
    Element(18, "Ar", "Argon", 3, 18),
    Element(19, "K", "Potassium", 4, 1),
    Element(20, "Ca", "Calcium", 4, 2),
    Element(21, "Sc", "Scandium", 4, 3),
    Element(22, "Ti", "Titanium", 4, 4),
    Element(23, "V", "Vanadium", 4, 5),
    Element(24, "Cr", "Chromium", 4, 6),
    Element(25, "Mn", "Manganese", 4, 7),
    Element(26, "Fe", "Iron", 4, 8),
    Element(27, "Co", "Cobalt", 4, 9),
    Element(28, "Ni", "Nickel", 4, 10),
    Element(29, "Cu", "Copper", 4, 11),
    Element(30, "Zn", "Zinc", 4, 12),
    Element(31, "Ga", "Gallium", 4, 13),
    Element(32, "Ge", "Germanium", 4, 14),
    Element(33, "As", "Arsenic", 4, 15),
    Element(34, "Se", "Selenium", 4, 16),
    Element(35, "Br", "Bromine", 4, 17),
    Element(36, "Kr", "Krypton", 4, 18),
    Element(37, "Rb", "Rubidium", 5, 1),
    Element(38, "Sr", "Strontium", 5, 2),
    Element(39, "Y", "Yttrium", 5, 3),
    Element(40, "Zr", "Zirconium", 5, 4),
    Element(41, "Nb", "Niobium", 5, 5),
    Element(42, "Mo", "Molybdenum", 5, 6),
    Element(43, "Tc", "Technetium", 5, 7),
    Element(44, "Ru", "Ruthenium", 5, 8),
    Element(45, "Rh", "Rhodium", 5, 9),
    Element(46, "Pd", "Palladium", 5, 10),
    Element(47, "Ag", "Silver", 5, 11),
    Element(48, "Cd", "Cadmium", 5, 12),
    Element(49, "In", "Indium", 5, 13),
    Element(50, "Sn", "Tin", 5, 14),
    Element(51, "Sb", "Antimony", 5, 15),
    Element(52, "Te", "Tellurium", 5, 16),
    Element(53, "I", "Iodine", 5, 17),
    Element(54, "Xe", "Xenon", 5, 18),
    Element(55, "Cs", "Cesium", 6, 1),
    Element(56, "Ba", "Barium", 6, 2),
    Element(57, "La", "Lanthanum", 6, 3),
    Element(58, "Ce", "Cerium", 8, 4),
    Element(59, "Pr", "Praseodymium", 8, 5),
    Element(60, "Nd", "Neodymium", 8, 6),
    Element(61, "Pm", "Promethium", 8, 7),
    Element(62, "Sm", "Samarium", 8, 8),
    Element(63, "Eu", "Europium", 8, 9),
    Element(64, "Gd", "Gadolinium", 8, 10),
    Element(65, "Tb", "Terbium", 8, 11),
    Element(66, "Dy", "Dysprosium", 8, 12),
    Element(67, "Ho", "Holmium", 8, 13),
    Element(68, "Er", "Erbium", 8, 14),
    Element(69, "Tm", "Thulium", 8, 15),
    Element(70, "Yb", "Ytterbium", 8, 16),
    Element(71, "Lu", "Lutetium", 6, 3),
    Element(72, "Hf", "Hafnium", 6, 4),
    Element(73, "Ta", "Tantalum", 6, 5),
    Element(74, "W", "Tungsten", 6, 6),
    Element(75, "Re", "Rhenium", 6, 7),
    Element(76, "Os", "Osmium", 6, 8),
    Element(77, "Ir", "Iridium", 6, 9),
    Element(78, "Pt", "Platinum", 6, 10),
    Element(79, "Au", "Gold", 6, 11),
    Element(80, "Hg", "Mercury", 6, 12),
    Element(81, "Tl", "Thallium", 6, 13),
    Element(82, "Pb", "Lead", 6, 14),
    Element(83, "Bi", "Bismuth", 6, 15),
    Element(84, "Po", "Polonium", 6, 16),
    Element(85, "At", "Astatine", 6, 17),
    Element(86, "Rn", "Radon", 6, 18),
    Element(87, "Fr", "Francium", 7, 1),
    Element(88, "Ra", "Radium", 7, 2),
    Element(89, "Ac", "Actinium", 7, 3),
    Element(90, "Th", "Thorium", 9, 4),
    Element(91, "Pa", "Protactinium", 9, 5),
    Element(92, "U", "Uranium", 9, 6),
    Element(93, "Np", "Neptunium", 9, 7),
    Element(94, "Pu", "Plutonium", 9, 8),
    Element(95, "Am", "Americium", 9, 9),
    Element(96, "Cm", "Curium", 9, 10),
    Element(97, "Bk", "Berkelium", 9, 11),
    Element(98, "Cf", "Californium", 9, 12),
    Element(99, "Es", "Einsteinium", 9, 13),
    Element(100, "Fm", "Fermium", 9, 14),
    Element(101, "Md", "Mendelevium", 9, 15),
    Element(102, "No", "Nobelium", 9, 16),
    Element(103, "Lr", "Lawrencium", 7, 3),
    Element(104, "Rf", "Rutherfordium", 7, 4),
    Element(105, "Db", "Dubnium", 7, 5),
    Element(106, "Sg", "Seaborgium", 7, 6),
    Element(107, "Bh", "Bohrium", 7, 7),
    Element(108, "Hs", "Hassium", 7, 8),
    Element(109, "Mt", "Meitnerium", 7, 9),
    Element(110, "Ds", "Darmstadtium", 7, 10),
    Element(111, "Rg", "Roentgenium", 7, 11),
    Element(112, "Cn", "Copernicium", 7, 12),
    Element(113, "Nh", "Nihonium", 7, 13),
    Element(114, "Fl", "Flerovium", 7, 14),
    Element(115, "Mc", "Moscovium", 7, 15),
    Element(116, "Lv", "Livermorium", 7, 16),
    Element(117, "Ts", "Tennessine", 7, 17),
    Element(118, "Og", "Oganesson", 7, 18),
]

# 표시용 좌표(18열 x 여러 행). 주력 표(1–7주기) + 란타넘/악티늄 별도 줄
# 좌표는 (period_row, group_col)로 배치. 8=란타넘 줄, 9=악티늄 줄.
SYMBOL_TO_ELEMENT: Dict[str, Element] = {e.symbol: e for e in ELEMENTS_ORDERED}
Z_TO_SYMBOL = {e.Z: e.symbol for e in ELEMENTS_ORDERED}

MAIN_ROWS = {
    1: {1: "H", 18: "He"},
    2: {1: "Li", 2: "Be", 13: "B", 14: "C", 15: "N", 16: "O", 17: "F", 18: "Ne"},
    3: {1: "Na", 2: "Mg", 13: "Al", 14: "Si", 15: "P", 16: "S", 17: "Cl", 18: "Ar"},
    4: {1: "K", 2: "Ca", 3: "Sc", 4: "Ti", 5: "V", 6: "Cr", 7: "Mn", 8: "Fe", 9: "Co", 10: "Ni", 11: "Cu", 12: "Zn", 13: "Ga", 14: "Ge", 15: "As", 16: "Se", 17: "Br", 18: "Kr"},
    5: {1: "Rb", 2: "Sr", 3: "Y", 4: "Zr", 5: "Nb", 6: "Mo", 7: "Tc", 8: "Ru", 9: "Rh", 10: "Pd", 11: "Ag", 12: "Cd", 13: "In", 14: "Sn", 15: "Sb", 16: "Te", 17: "I", 18: "Xe"},
    6: {1: "Cs", 2: "Ba", 3: "La", 4: "Hf", 5: "Ta", 6: "W", 7: "Re", 8: "Os", 9: "Ir", 10: "Pt", 11: "Au", 12: "Hg", 13: "Tl", 14: "Pb", 15: "Bi", 16: "Po", 17: "At", 18: "Rn"},
    7: {1: "Fr", 2: "Ra", 3: "Ac", 4: "Rf", 5: "Db", 6: "Sg", 7: "Bh", 8: "Hs", 9: "Mt", 10: "Ds", 11: "Rg", 12: "Cn", 13: "Nh", 14: "Fl", 15: "Mc", 16: "Lv", 17: "Ts", 18: "Og"},
}

LANTHANIDES = ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]
ACTINIDES   = ["Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]

# 분류(색상용)
ALKALI = {"Li","Na","K","Rb","Cs","Fr"}
ALKALINE = {"Be","Mg","Ca","Sr","Ba","Ra"}
HALOGENS = {"F","Cl","Br","I","At","Ts"}
NOBLE = {"He","Ne","Ar","Kr","Xe","Rn","Og"}

METALLOIDS = {"B","Si","Ge","As","Sb","Te","Po"}
REACTIVE_NONMETALS = {"H","C","N","O","P","S","Se"}
POST_TRANSITION = {"Al","Ga","In","Sn","Tl","Pb","Bi","Nh","Fl","Mc","Lv"}

TRANSITION = set()
for row in (4,5,6,7):
    for g in range(3,13):
        sym = MAIN_ROWS[row].get(g)
        if sym:
            TRANSITION.add(sym)
TRANSITION.update({"Sc","Y","La","Ac"})

F_BLOCK = set(LANTHANIDES + ACTINIDES)

# 간단 특징/용도 템플릿
CATEGORY_LABELS = {
    'alkali': '알칼리 금속',
    'alkaline': '알칼리 토금속',
    'halogen': '할로겐',
    'noble': '비활성 기체',
    'transition': '전이 금속',
    'post-transition': '전이 후 금속',
    'metalloid': '준금속',
    'reactive-nonmetal': '비금속',
    'f-block': '란타넘/악티늄족',
}

def classify(symbol: str) -> str:
    if symbol in ALKALI: return 'alkali'
    if symbol in ALKALINE: return 'alkaline'
    if symbol in HALOGENS: return 'halogen'
    if symbol in NOBLE: return 'noble'
    if symbol in F_BLOCK: return 'f-block'
    if symbol in TRANSITION: return 'transition'
    if symbol in METALLOIDS: return 'metalloid'
    if symbol in POST_TRANSITION: return 'post-transition'
    if symbol in REACTIVE_NONMETALS: return 'reactive-nonmetal'
    return 'transition'  # 기본값

TEMPLATES = {
    'alkali': {
        'features': "반응성이 큰 연질 금속, 1가 양이온 형성, 물과 격렬 반응",
        'uses': "배터리(리튬), 나트륨등 조명, 유리/화학합성",
        'future': "차세대 이온전지, 고에너지 저장장치"
    },
    'alkaline': {
        'features': "단단하고 은백색, 2가 양이온, 열/전기 전도도 우수",
        'uses': "합금, 뼈/건강(칼슘), 불꽃놀이 착색, 탈황제",
        'future': "의료 소재, 경량 구조재, 친환경 공정"
    },
    'halogen': {
        'features': "높은 반응성 비금속, 강한 산화제",
        'uses': "소독·살균(염소), 조명·전자, 유기합성",
        'future': "고성능 전해질, 차세대 광원·디스플레이"
    },
    'noble': {
        'features': "화학적으로 매우 안정, 기체(상온)",
        'uses': "조명(네온), 냉각(헬륨), 레이저·의료",
        'future': "심해/극저온 기술, 우주·양자 실험"
    },
    'transition': {
        'features': "다양한 산화수·촉매활성, 높은 강도/전도도",
        'uses': "강철(Fe), 촉매(Pt, Pd), 전자·배선(Cu)",
        'future': "수소촉매, 그린케미스트리, 고내열 합금"
    },
    'post-transition': {
        'features': "상대적으로 연하며 가공 쉬움, 금속성",
        'uses': "납축전지(Pb), 주석 코팅(Sn), 반도체 납땜",
        'future': "무독성 대체합금, 전력전자 솔더 재료"
    },
    'metalloid': {
        'features': "금속/비금속의 중간 성질, 반도체적 성향",
        'uses': "반도체(Si, Ge), 유리강화(B)",
        'future': "차세대 반도체, 포토닉스 소재"
    },
    'reactive-nonmetal': {
        'features': "공유결합 성향, 생명·환경 필수",
        'uses': "유기물·의약·비료(N,P), 에너지 저장(C)",
        'future': "친환경 촉매, 고성능 전극/분리막"
    },
    'f-block': {
        'features': "내자성/발광 특성(란타넘족), 방사성(악티늄족)",
        'uses': "영구자석(Nd, Dy), 레이저/형광체, 원자력(U)",
        'future': "고성능 모터, 희소자원 대체/재활용 기술"
    },
}

# 대표 원소 상세 오버라이드(간단 사례 보강)
DETAIL_OVERRIDES: Dict[str, Dict[str,str]] = {
    "H": {"uses": "연료전지, 암모니아 합성(Haber-Bosch)", "future": "그린수소, 수소항공"},
    "C": {"uses": "그래파이트·다이아몬드, 탄소섬유", "future": "그래핀·탄소나노튜브 전자소자"},
    "Si": {"uses": "반도체 칩, 태양전지", "future": "차세대 반도체·포토닉스"},
    "Fe": {"uses": "강철 제조, 건축·자동차", "future": "녹색수소 제철(HBI)"},
    "Cu": {"uses": "전선·모터·배터리 집전체", "future": "고효율 전력망, 재생에너지 확충"},
    "Li": {"uses": "리튬이온배터리", "future": "고체전해질·리튬황 배터리"},
    "Au": {"uses": "전자·커넥터·투자", "future": "바이오센서·의료 나노소재"},
    "Ag": {"uses": "도전성 잉크·항균 코팅", "future": "고집적 전자패키징"},
    "U": {"uses": "원자력 연료", "future": "고속로·소형모듈원전(SMR)"},
}

# ------------------------- UI 스타일 -------------------------
st.set_page_config(page_title="원소 주기율표", page_icon="🧪", layout="wide")

COLOR_MAP = {
    'alkali': '#ffd1dc',
    'alkaline': '#ffe8b6',
    'halogen': '#ffddb3',
    'noble': '#d9f1ff',
    'transition': '#e1ffe1',
    'post-transition': '#f0f0f0',
    'metalloid': '#fff2c2',
    'reactive-nonmetal': '#e6f7ff',
    'f-block': '#f5d9ff',
}

st.markdown(
    """
    <style>
    .cell {border-radius:10px; padding:8px; text-align:center; border:1px solid #e5e7eb;}
    .sym {font-weight:700; font-size:1.1rem;}
    .z {font-size:0.75rem; opacity:0.7}
    .nm {font-size:0.75rem; opacity:0.8}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------- 사이드바 -------------------------
with st.sidebar:
    st.header("검색 / 필터")
    q = st.text_input("심볼/이름 검색", "").strip().lower()
    group_sel = st.selectbox("그룹(족)", ["전체"] + list(range(1,19)))
    period_sel = st.selectbox("주기", ["전체"] + list(range(1,8)))
    fam_map = {k: CATEGORY_LABELS[k] for k in CATEGORY_LABELS}
    fam_sel = st.selectbox("계열", ["전체"] + [fam_map[k] for k in fam_map])

# 선택 상태
if "selected_symbol" not in st.session_state:
    st.session_state.selected_symbol = "C"

# ------------------------- 메인 제목 -------------------------
st.title("🧪 원소 주기율표 — 클릭해서 자세히 보기")
st.caption("118개 원소를 클릭하면 실생활 사례·이름·번호·특징·미래 활용을 확인할 수 있어요.")

# ------------------------- 필터 로직 -------------------------
def passes_filters(sym: str) -> bool:
    elem = SYMBOL_TO_ELEMENT[sym]
    # 검색어
    if q:
        if not (sym.lower().startswith(q) or elem.name.lower().startswith(q)):
            return False
    # 그룹
    if group_sel != "전체" and elem.group != group_sel:
        return False
    # 주기
    if period_sel != "전체":
        # 란타넘/악티늄 줄(8,9)은 필터 제외
        if elem.period != period_sel:
            return False
    # 계열
    if fam_sel != "전체":
        key = classify(sym)
        if CATEGORY_LABELS.get(key) != fam_sel:
            return False
    return True

# ------------------------- 테이블 그리기 -------------------------
col_left, col_right = st.columns([2, 1], gap="large")

with col_left:
    # 1~7주기 본체
    for row in range(1, 8):
        cols = st.columns(18)
        for g in range(1, 19):
            sym = MAIN_ROWS.get(row, {}).get(g)
            if sym is None:
                cols[g-1].markdown("&nbsp;")
                continue
            elem = SYMBOL_TO_ELEMENT[sym]
            fam = classify(sym)
            color = COLOR_MAP[fam]
            disabled = not passes_filters(sym)
            html = f"<div class='cell' style='background:{color}'><div class='z'>{elem.Z}</div><div class='sym'>{sym}</div><div class='nm'>{elem.name}</div></div>"
            if cols[g-1].button(label=sym, key=f"btn-{sym}-{row}-{g}", help=f"{elem.name} (Z={elem.Z})", disabled=disabled):
                st.session_state.selected_symbol = sym
            cols[g-1].markdown(html, unsafe_allow_html=True)

    st.markdown("""
    **란타넘족 / 악티늄족**
    """)
    # 란타넘/악티늄 줄
    for label, seq in [("Lanthanoids", LANTHANIDES), ("Actinoids", ACTINIDES)]:
        st.caption(label)
        cols = st.columns(len(seq))
        for i, sym in enumerate(seq):
            elem = SYMBOL_TO_ELEMENT[sym]
            fam = 'f-block'
            color = COLOR_MAP[fam]
            disabled = not passes_filters(sym)
            html = f"<div class='cell' style='background:{color}'><div class='z'>{elem.Z}</div><div class='sym'>{sym}</div><div class='nm'>{elem.name}</div></div>"
            if cols[i].button(label=sym, key=f"btn-{sym}-f", help=f"{elem.name} (Z={elem.Z})", disabled=disabled):
                st.session_state.selected_symbol = sym
            cols[i].markdown(html, unsafe_allow_html=True)

with col_right:
    sym = st.session_state.selected_symbol
    e = SYMBOL_TO_ELEMENT[sym]
    fam_key = classify(sym)
    fam_name = CATEGORY_LABELS[fam_key]

    st.subheader(f"{e.symbol} — {e.name}")
    st.write(f"원소번호: **{e.Z}** | 그룹: **{e.group}** | 주기: **{e.period if e.period<8 else 'f-Block'}** | 계열: **{fam_name}**")

    tmpl = TEMPLATES[fam_key]
    uses = DETAIL_OVERRIDES.get(sym, {}).get('uses', tmpl['uses'])
    features = tmpl['features']
    future = DETAIL_OVERRIDES.get(sym, {}).get('future', tmpl['future'])

    # 5가지 정보 카드
    st.markdown("### 🔎 정보")
    st.markdown("**1) 실생활 사례**")
    st.write(uses)

    st.markdown("**2) 원소 이름**")
    st.write(e.name)

    st.markdown("**3) 원소번호**")
    st.write(e.Z)

    st.markdown("**4) 원소의 특징**")
    st.write(features)

    st.markdown("**5) 미래에 사용될 방향**")
    st.write(future)

    st.divider()
    st.caption("※ 데이터는 교육용 요약입니다. 더 상세한 설명/예시는 자유롭게 편집해 확장하세요.")

# ------------------------- 확장: 데이터 내보내기 -------------------------
with st.expander("CSV로 내보내기/가져오기"):
    import pandas as pd
    rows = []
    for e in ELEMENTS_ORDERED:
        fam = classify(e.symbol)
        tmpl = TEMPLATES[fam]
        rows.append({
            'Z': e.Z, 'symbol': e.symbol, 'name': e.name,
            'period': e.period, 'group': e.group, 'family': CATEGORY_LABELS[fam],
            'uses': DETAIL_OVERRIDES.get(e.symbol, {}).get('uses', tmpl['uses']),
            'features': tmpl['features'],
            'future': DETAIL_OVERRIDES.get(e.symbol, {}).get('future', tmpl['future']),
        })
    df = pd.DataFrame(rows)
    st.download_button("CSV 다운로드", data=df.to_csv(index=False).encode('utf-8'), file_name="elements_summary.csv", mime="text/csv")
    up = st.file_uploader("CSV 불러오기(동일 컬럼)", type=["csv"])
    if up is not None:
        try:
            udf = pd.read_csv(up)
            st.dataframe(udf.head(10))
            st.success("미리보기 표시 — 앱 로직에 연결하려면 코드 내 병합 부분을 확장하세요.")
        except Exception as ex:
            st.error(f"CSV 파싱 오류: {ex}")
