import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="주기율표 웹", layout="wide")

st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom, #E0F7FA, #FFFFFF);
        }
        .element {
            display: inline-block;
            width: 70px;
            height: 70px;
            margin: 1px;
            border-radius: 15px;
            text-align: center;
            vertical-align: middle;
            line-height: 1.2;
            font-size: 12px;
            font-weight: bold;
            cursor: pointer;
        }
        .metal {
            background-color: #ADD8E6;
        }
        .nonmetal {
            background-color: #FFFACD;
        }
        .selected {
            background-color: red !important;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# 원소 데이터 (번호, 기호, 이름, 분류, 특징)
elements = [
    (1, "H", "수소", "nonmetal", "가장 가벼운 원소, 무색무취 기체"),
    (2, "He", "헬륨", "nonmetal", "비활성 기체, 풍선 등에 사용"),
    (3, "Li", "리튬", "metal", "가벼운 금속, 배터리에 사용"),
    (4, "Be", "베릴륨", "metal", "단단하고 가벼운 금속"),
    (5, "B", "붕소", "nonmetal", "준금속, 반도체 재료"),
    (6, "C", "탄소", "nonmetal", "생명체의 기본 원소, 다이아몬드·흑연"),
    (7, "N", "질소", "nonmetal", "대기 78%, 단백질 구성"),
    (8, "O", "산소", "nonmetal", "호흡에 필요, 연소에 관여"),
    (9, "F", "플루오린", "nonmetal", "반응성이 매우 강한 할로젠"),
    (10, "Ne", "네온", "nonmetal", "네온사인에 사용되는 비활성 기체"),
    (11, "Na", "나트륨", "metal", "소금(NaCl)의 구성 원소"),
    (12, "Mg", "마그네슘", "metal", "가볍고 강한 금속, 폭죽에 사용"),
    (13, "Al", "알루미늄", "metal", "가볍고 부식에 강한 금속"),
    (14, "Si", "규소", "nonmetal", "반도체의 핵심 원소"),
    (15, "P", "인", "nonmetal", "DNA, ATP 구성 원소"),
    (16, "S", "황", "nonmetal", "고무, 화약 원료"),
    (17, "Cl", "염소", "nonmetal", "소독제, PVC 원료"),
    (18, "Ar", "아르곤", "nonmetal", "비활성 기체, 전구 충전"),
    (19, "K", "칼륨", "metal", "세포 내 주요 이온"),
    (20, "Ca", "칼슘", "metal", "뼈와 치아의 주요 성분"),
    (21, "Sc", "스칸듐", "metal", "가벼운 금속, 항공 소재"),
    (22, "Ti", "티타늄", "metal", "강하고 가벼운 금속"),
    (23, "V", "바나듐", "metal", "강철 합금 원소"),
    (24, "Cr", "크로뮴", "metal", "스테인리스강 원소"),
    (25, "Mn", "망간", "metal", "철강 원료, 효소 구성"),
    (26, "Fe", "철", "metal", "지구 핵 구성, 혈액의 헤모글로빈"),
    (27, "Co", "코발트", "metal", "리튬이온 배터리 원소"),
    (28, "Ni", "니켈", "metal", "합금, 촉매에 사용"),
    (29, "Cu", "구리", "metal", "전선, 전도율이 높음"),
    (30, "Zn", "아연", "metal", "도금, 효소 구성"),
    (31, "Ga", "갈륨", "metal", "반도체 재료"),
    (32, "Ge", "게르마늄", "nonmetal", "반도체 소재"),
    (33, "As", "비소", "nonmetal", "준금속, 독성 원소"),
    (34, "Se", "셀레늄", "nonmetal", "항산화 작용"),
    (35, "Br", "브로민", "nonmetal", "적갈색 액체 할로젠"),
    (36, "Kr", "크립톤", "nonmetal", "비활성 기체, 조명에 사용"),
]

# 선택 상태 초기화
if "selected" not in st.session_state:
    st.session_state.selected = set()

# 원소 클릭 함수
def toggle_element(el_num):
    if el_num in st.session_state.selected:
        st.session_state.selected.remove(el_num)
    else:
        st.session_state.selected.add(el_num)

# 주기율표 출력 (4주기까지)
rows = [
    [1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 2],
    [3, 4, None, None, None, None, None, None, None, None, None, None, 5, 6, 7, 8, 9, 10],
    [11, 12, None, None, None, None, None, None, None, None, None, None, 13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
]

for row in rows:
    cols = st.columns(len(row))
    for i, num in enumerate(row):
        if num is None:
            cols[i].markdown("<div style='width:70px;height:70px;'></div>", unsafe_allow_html=True)
        else:
            el = next(e for e in elements if e[0] == num)
            base_class = "metal" if el[3] == "metal" else "nonmetal"
            extra_class = " selected" if num in st.session_state.selected else ""
            html = f"""
                <div class='element {base_class}{extra_class}' onclick="fetch('/?toggle={num}', {{method:'POST'}})">
                    {el[0]}<br>{el[1]}
                </div>
            """
            cols[i].markdown(html, unsafe_allow_html=True)

# 선택 원소 출력
if st.session_state.selected:
    st.subheader("선택된 원소 정보")
    for num in st.session_state.selected:
        el = next(e for e in elements if e[0] == num)
        st.markdown(f"**{el[0]}번 {el[1]} ({el[2]})** → {el[4]}")

    # 두 개 이상 선택 시 결합 정보
    if len(st.session_state.selected) >= 2:
        st.subheader("결합 정보")
        selected_elements = [next(e for e in elements if e[0] == n) for n in st.session_state.selected]
        st.write("선택된 원소:", ", ".join([f"{e[1]}({e[2]})" for e in selected_elements]))

        # 단순 결합 규칙 예시
        if all(e[3] == "metal" for e in selected_elements):
            st.write("→ 금속결합: 전자가 자유롭게 이동, 전기 전도성이 크다.")
        elif all(e[3] == "nonmetal" for e in selected_elements):
            st.write("→ 공유결합: 전자쌍 공유, 분자는 안정된 형태.")
        else:
            st.write("→ 이온결합: 전자 이동으로 양이온/음이온 형성, 강한 정전기적 인력.")
