import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #e6f7ff, #ffffff);
    }
    .element-grid {
        display: grid;
        grid-template-columns: repeat(18, 1fr);
        gap: 2px; /* 간격 최소화 */
        justify-items: center;
        align-items: center;
    }
    .element {
        width: 70px;
        height: 70px;
        border-radius: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 12px;
        font-weight: bold;
        cursor: pointer;
        border: 1px solid #888;
        transition: 0.2s;
    }
    .metal { background-color: #b3e5ff; }       /* 금속 = 하늘색 */
    .nonmetal { background-color: #fff7b3; }    /* 비금속/준금속 = 연노랑 */
    .selected { background-color: #ff6666 !important; color: white; } /* 선택시 빨간색 */
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------
# 원소 데이터 (1~54번)
# ----------------------
elements = [
    {"num": 1, "symbol": "H", "name": "Hydrogen", "type": "nonmetal", "feature": "우주에서 가장 풍부한 원소"},
    {"num": 2, "symbol": "He", "name": "Helium", "type": "nonmetal", "feature": "비활성 기체, 가벼움"},
    {"num": 3, "symbol": "Li", "name": "Lithium", "type": "metal", "feature": "배터리에 사용"},
    {"num": 4, "symbol": "Be", "name": "Beryllium", "type": "metal", "feature": "합금에 사용"},
    {"num": 5, "symbol": "B", "name": "Boron", "type": "nonmetal", "feature": "유리, 세라믹 원료"},
    {"num": 6, "symbol": "C", "name": "Carbon", "type": "nonmetal", "feature": "생명체 구성 원소"},
    {"num": 7, "symbol": "N", "name": "Nitrogen", "type": "nonmetal", "feature": "공기 78% 차지"},
    {"num": 8, "symbol": "O", "name": "Oxygen", "type": "nonmetal", "feature": "호흡에 필요"},
    {"num": 9, "symbol": "F", "name": "Fluorine", "type": "nonmetal", "feature": "강한 반응성"},
    {"num": 10, "symbol": "Ne", "name": "Neon", "type": "nonmetal", "feature": "네온사인에 사용"},
    # ... (11번 ~ 54번까지 모든 원소 데이터 채우기. 금속은 metal, 나머지는 nonmetal로 표기)
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
