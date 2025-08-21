import streamlit as st

# 페이지 설정
st.set_page_config(layout="wide", page_title="주기율표 웹", page_icon="🔬")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #E0F7FA, #FFFFFF);
    }
    .element-button {
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 10px;
        font-size: 14px;
        font-weight: bold;
        margin: 1px;
        padding: 6px;
        height: 70px;
        width: 70px;
        text-align: center;
    }
    .selected {
        background-color: red !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 원소 데이터 (1번~36번)
elements = [
    (1, "H", "수소", "비금속"),
    (2, "He", "헬륨", "비금속"),
    (3, "Li", "리튬", "금속"),
    (4, "Be", "베릴륨", "금속"),
    (5, "B", "붕소", "준금속"),
    (6, "C", "탄소", "비금속"),
    (7, "N", "질소", "비금속"),
    (8, "O", "산소", "비금속"),
    (9, "F", "플루오린", "비금속"),
    (10, "Ne", "네온", "비금속"),
    (11, "Na", "나트륨", "금속"),
    (12, "Mg", "마그네슘", "금속"),
    (13, "Al", "알루미늄", "금속"),
    (14, "Si", "규소", "준금속"),
    (15, "P", "인", "비금속"),
    (16, "S", "황", "비금속"),
    (17, "Cl", "염소", "비금속"),
    (18, "Ar", "아르곤", "비금속"),
    (19, "K", "칼륨", "금속"),
    (20, "Ca", "칼슘", "금속"),
    (21, "Sc", "스칸듐", "금속"),
    (22, "Ti", "타이타늄", "금속"),
    (23, "V", "바나듐", "금속"),
    (24, "Cr", "크로뮴", "금속"),
    (25, "Mn", "망간", "금속"),
    (26, "Fe", "철", "금속"),
    (27, "Co", "코발트", "금속"),
    (28, "Ni", "니켈", "금속"),
    (29, "Cu", "구리", "금속"),
    (30, "Zn", "아연", "금속"),
    (31, "Ga", "갈륨", "금속"),
    (32, "Ge", "게르마늄", "준금속"),
    (33, "As", "비소", "준금속"),
    (34, "Se", "셀레늄", "비금속"),
    (35, "Br", "브로민", "비금속"),
    (36, "Kr", "크립톤", "비금속"),
]

# 원소별 색상
def get_color(category, selected=False):
    if selected:
        return "red"
    if category == "금속":
        return "#87CEEB"  # 하늘색
    else:
        return "#FFFACD"  # 연노란색

# session_state 안전 초기화
for num, sym, name, cat in elements:
    key = f"{num}_{sym}"
    if key not in st.session_state:
        st.session_state[key] = False

# 원소 버튼 그리드 (4주기까지 배치)
rows = [
    [1, 2],
    list(range(3, 11)),
    list(range(11, 19)),
    list(range(19, 37)),
]

selected_elements = []

for row in rows:
    cols = st.columns(len(row))
    for i, num in enumerate(row):
        element = [e for e in elements if e[0] == num][0]
        key = f"{element[0]}_{element[1]}"
        selected = st.session_state[key]

        color = get_color(element[3], selected)

        if cols[i].button(f"{element[0]} {element[1]}", key=key, help=element[2]):
            st.session_state[key] = not selected
            selected = st.session_state[key]
            color = get_color(element[3], selected)

        cols[i].markdown(
            f"""
            <div class="element-button" style="background-color:{color}">
                {element[0]} {element[1]}
            </div>
            """,
            unsafe_allow_html=True
        )

        if selected:
            selected_elements.append(element)

# 선택된 원소 특징 출력
if selected_elements:
    st.subheader("🔎 선택된 원소 특징")
    for el in selected_elements:
        st.write(f"**{el[1]} ({el[2]})** - {el[3]} 원소")

    if len(selected_elements) >= 2:
        st.subheader("⚛️ 결합 정보")
        st.write("결합 종류와 분자의 특성은 화학적 성질에 따라 다름")
