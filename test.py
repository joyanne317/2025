import streamlit as st

st.set_page_config(layout="wide")

# ----------------------
# CSS 스타일
# ----------------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #e6f7ff, #ffffff);
    }
    .element-grid {
        display: grid;
        grid-template-columns: repeat(18, 1fr);
        gap: 1px; /* 원소 간격 최소 */
        justify-items: center;
        align-items: center;
    }
    .element {
        width: 75px;
        height: 75px;
        border-radius: 15px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        font-size: 12px;
        font-weight: bold;
        cursor: pointer;
        border: 1px solid #888;
        transition: 0.2s;
        text-align: center;
    }
    .metal { background-color: #b3e5ff; }       /* 금속 = 하늘색 */
    .nonmetal { background-color: #fff7b3; }    /* 비금속/준금속 = 연노랑 */
    .selected { background-color: #ff4d4d !important; color: white; } /* 선택시 빨강 */
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------
# 원소 데이터 (1~36번, 4주기 끝까지)
# ----------------------
elements = [
    {"num": 1, "symbol": "H", "name": "Hydrogen", "type": "nonmetal", "feature": "가장 가벼운 원소, 우주에서 가장 풍부"},
    {"num": 2, "symbol": "He", "name": "Helium", "type": "nonmetal", "feature": "비활성 기체, 풍선과 냉각에 사용"},
    {"num": 3, "symbol": "Li", "name": "Lithium", "type": "metal", "feature": "리튬이온 배터리 원료"},
    {"num": 4, "symbol": "Be", "name": "Beryllium", "type": "metal", "feature": "합금과 전자기기에 사용"},
    {"num": 5, "symbol": "B", "name": "Boron", "type": "nonmetal", "feature": "유리, 세라믹, 반도체"},
    {"num": 6, "symbol": "C", "name": "Carbon", "type": "nonmetal", "feature": "생명체 기본 구성 원소"},
    {"num": 7, "symbol": "N", "name": "Nitrogen", "type": "nonmetal", "feature": "대기 중 78% 차지"},
    {"num": 8, "symbol": "O", "name": "Oxygen", "type": "nonmetal", "feature": "호흡에 필요, 연소 반응"},
    {"num": 9, "symbol": "F", "name": "Fluorine", "type": "nonmetal", "feature": "반응성이 가장 큰 원소"},
    {"num": 10, "symbol": "Ne", "name": "Neon", "type": "nonmetal", "feature": "네온사인 조명"},
    {"num": 11, "symbol": "Na", "name": "Sodium", "type": "metal", "feature": "소금(NaCl)의 구성 원소"},
    {"num": 12, "symbol": "Mg", "name": "Magnesium", "type": "metal", "feature": "가볍고 강한 금속, 합금 원료"},
    {"num": 13, "symbol": "Al", "name": "Aluminum", "type": "metal", "feature": "가벼운 금속, 알루미늄 캔"},
    {"num": 14, "symbol": "Si", "name": "Silicon", "type": "nonmetal", "feature": "반도체 산업의 핵심 원소"},
    {"num": 15, "symbol": "P", "name": "Phosphorus", "type": "nonmetal", "feature": "DNA, ATP 구성 성분"},
    {"num": 16, "symbol": "S", "name": "Sulfur", "type": "nonmetal", "feature": "고무 가공, 화약, 단백질 성분"},
    {"num": 17, "symbol": "Cl", "name": "Chlorine", "type": "nonmetal", "feature": "소독제, PVC 원료"},
    {"num": 18, "symbol": "Ar", "name": "Argon", "type": "nonmetal", "feature": "비활성 기체, 용접에 사용"},
    {"num": 19, "symbol": "K", "name": "Potassium", "type": "metal", "feature": "세포 기능에 필수적"},
    {"num": 20, "symbol": "Ca", "name": "Calcium", "type": "metal", "feature": "뼈와 치아의 주성분"},
    {"num": 21, "symbol": "Sc", "name": "Scandium", "type": "metal", "feature": "항공 합금에 사용"},
    {"num": 22, "symbol": "Ti", "name": "Titanium", "type": "metal", "feature": "강하고 가벼운 금속, 인공 뼈"},
    {"num": 23, "symbol": "V", "name": "Vanadium", "type": "metal", "feature": "강철 합금 강화"},
    {"num": 24, "symbol": "Cr", "name": "Chromium", "type": "metal", "feature": "스테인리스 강, 도금"},
    {"num": 25, "symbol": "Mn", "name": "Manganese", "type": "metal", "feature": "철강 생산에 중요"},
    {"num": 26, "symbol": "Fe", "name": "Iron", "type": "metal", "feature": "지구 핵의 주성분, 강철"},
    {"num": 27, "symbol": "Co", "name": "Cobalt", "type": "metal", "feature": "배터리, 자석 원료"},
    {"num": 28, "symbol": "Ni", "name": "Nickel", "type": "metal", "feature": "스테인리스 강, 화폐"},
    {"num": 29, "symbol": "Cu", "name": "Copper", "type": "metal", "feature": "전선, 열전도성 우수"},
    {"num": 30, "symbol": "Zn", "name": "Zinc", "type": "metal", "feature": "도금, 합금, 아연 화합물"},
    {"num": 31, "symbol": "Ga", "name": "Gallium", "type": "metal", "feature": "반도체, LED"},
    {"num": 32, "symbol": "Ge", "name": "Germanium", "type": "nonmetal", "feature": "반도체, 광섬유"},
    {"num": 33, "symbol": "As", "name": "Arsenic", "type": "nonmetal", "feature": "살충제, 반도체"},
    {"num": 34, "symbol": "Se", "name": "Selenium", "type": "nonmetal", "feature": "광전 효과, 건강 보조"},
    {"num": 35, "symbol": "Br", "name": "Bromine", "type": "nonmetal", "feature": "액체 할로겐, 살충제"},
    {"num": 36, "symbol": "Kr", "name": "Krypton", "type": "nonmetal", "feature": "조명, 레이저에 사용"},
]

# ----------------------
# 선택 상태 저장
# ----------------------
if "selected" not in st.session_state:
    st.session_state.selected = []

# ----------------------
# 주기율표 HTML 생성
# ----------------------
def render_table():
    html = '<div class="element-grid">'
    for el in elements:
        css_class = el["type"]
        if el["symbol"] in st.session_state.selected:
            css_class += " selected"
        html += f"""
        <div class="element {css_class}" onclick="window.parent.postMessage({{'element': '{el['symbol']}' }}, '*')">
            {el['num']}<br>{el['symbol']}
        </div>
        """
    html += "</div>"
    return html

# ----------------------
# 클릭 이벤트 처리
# ----------------------
clicked_element = st.experimental_get_query_params().get("element", [None])[0]
if clicked_element:
    if clicked_element in st.session_state.selected:
        st.session_state.selected.remove(clicked_element)
    else:
        st.session_state.selected.append(clicked_element)

# ----------------------
# 주기율표 출력
# ----------------------
st.markdown(render_table(), unsafe_allow_html=True)

# ----------------------
# 선택된 원소 정보 출력
# ----------------------
if st.session_state.selected:
    st.subheader("🔎 선택한 원소 정보")
    for el in elements:
        if el["symbol"] in st.session_state.selected:
            st.write(f"**{el['num']}번 {el['symbol']} ({el['name']})** → {el['feature']}")

    if len(st.session_state.selected) >= 2:
        st.subheader("⚛️ 결합 정보")
        st.write("선택된 원소들의 전자 배치와 성질에 따라 결합 종류가 달라집니다.")
        st.write("예: 금속 + 비금속 → 이온결합, 비금속 + 비금속 → 공유결합, 금속 + 금속 → 금속결합")
        st.write("각 결합은 강도, 전기 전도성, 녹는점 등의 특성 차이가 있습니다.")
