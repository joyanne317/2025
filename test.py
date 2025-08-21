import streamlit as st

# ===============================
# 118개 원소 데이터
# ===============================
elements = [
    {"symbol": "H", "name": "수소", "atomic_number": 1, "feature": "가장 가벼운 원소, 연료전지와 암모니아 합성에 활용"},
    {"symbol": "He", "name": "헬륨", "atomic_number": 2, "feature": "비활성 기체, 기구와 MRI 냉각에 사용"},
    {"symbol": "Li", "name": "리튬", "atomic_number": 3, "feature": "리튬이온 배터리의 핵심 원소"},
    {"symbol": "Be", "name": "베릴륨", "atomic_number": 4, "feature": "경량 금속, 우주항공 소재"},
    {"symbol": "B", "name": "붕소", "atomic_number": 5, "feature": "세라믹과 유리 제조에 활용"},
    {"symbol": "C", "name": "탄소", "atomic_number": 6, "feature": "생명체의 기본 원소, 다양한 동소체 존재"},
    {"symbol": "N", "name": "질소", "atomic_number": 7, "feature": "대기 중 78%, 비료의 주요 성분"},
    {"symbol": "O", "name": "산소", "atomic_number": 8, "feature": "호흡과 연소에 필수적"},
    {"symbol": "F", "name": "플루오린", "atomic_number": 9, "feature": "치약과 불소 화합물에 사용"},
    {"symbol": "Ne", "name": "네온", "atomic_number": 10, "feature": "네온사인 조명에 사용"},
    {"symbol": "Na", "name": "나트륨", "atomic_number": 11, "feature": "소금(NaCl)의 구성 성분"},
    {"symbol": "Mg", "name": "마그네슘", "atomic_number": 12, "feature": "합금, 폭죽, 건강 보조제에 사용"},
    {"symbol": "Al", "name": "알루미늄", "atomic_number": 13, "feature": "가볍고 내식성, 포장재와 항공기 소재"},
    {"symbol": "Si", "name": "규소", "atomic_number": 14, "feature": "반도체 칩과 유리의 주재료"},
    {"symbol": "P", "name": "인", "atomic_number": 15, "feature": "DNA와 ATP의 구성 성분, 비료에 사용"},
    {"symbol": "S", "name": "황", "atomic_number": 16, "feature": "황산과 고무 가공에 사용"},
    {"symbol": "Cl", "name": "염소", "atomic_number": 17, "feature": "소독과 PVC 제조에 사용"},
    {"symbol": "Ar", "name": "아르곤", "atomic_number": 18, "feature": "비활성 기체, 용접 보호가스"},
    {"symbol": "K", "name": "칼륨", "atomic_number": 19, "feature": "세포 내 주요 이온, 비료에 사용"},
    {"symbol": "Ca", "name": "칼슘", "atomic_number": 20, "feature": "뼈와 치아의 주요 성분"},
    # ... 여기서 118번 오가네손(Og)까지 동일한 형식으로 리스트를 채워 넣음
    {"symbol": "Og", "name": "오가네손", "atomic_number": 118, "feature": "초중원소, 인공적으로 합성됨"},
]

# ===============================
# 결합 종류 및 분자 특성 판정 함수
# ===============================
def get_bond_info(e1, e2):
    metals = ["Li","Be","Na","Mg","Al","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ag","Cd","Sn","Au","Hg","Pb","Ba","Ra"]  
    non_metals = ["H","C","N","O","F","P","S","Cl","Se","Br","I"]

    # 이온 결합 (금속 + 비금속)
    if (e1 in metals and e2 in non_metals) or (e2 in metals and e1 in non_metals):
        return "이온 결합", "전자 이동으로 양이온과 음이온 형성", "높은 녹는점과 끓는점, 물에 잘 녹고 전기 전도성 가짐(용융/수용액 상태)"

    # 금속 결합 (금속 + 금속)
    elif (e1 in metals and e2 in metals):
        return "금속 결합", "금속 원자핵 사이를 자유롭게 이동하는 전자 구름 형성", "전기 및 열 전도성이 뛰어나고, 연성과 전성이 큼"

    # 공유 결합 (비금속 + 비금속)
    elif (e1 in non_metals and e2 in non_metals):
        return "공유 결합", "전자쌍을 공유하여 분자 형성", "상대적으로 낮은 녹는점과 끓는점, 전기 전도성이 낮음"

    # 기본값
    else:
        return "불명", "데이터 부족", "추가 연구 필요"

# ===============================
# Streamlit UI
# ===============================
st.set_page_config(page_title="주기율표 결합 학습", layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: #e6f2ff;
    }
    .stButton button {
        background-color: #cce6ff;
        color: #003366;
        border-radius: 8px;
        padding: 8px;
        margin: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔬 주기율표 기반 결합 학습 웹")

# 선택 저장 공간
if "selected" not in st.session_state:
    st.session_state.selected = []

# 118개 원소 버튼 생성 (10열 그리드)
cols = st.columns(10)
for idx, elem in enumerate(elements):
    col = cols[idx % 10]
    if col.button(elem["symbol"]):
        if elem["symbol"] not in st.session_state.selected:
            if len(st.session_state.selected) < 2:
                st.session_state.selected.append(elem["symbol"])

# ===============================
# 결과 출력
# ===============================
if len(st.session_state.selected) == 2:
    e1, e2 = st.session_state.selected

    # 개별 원소 특징
    elem1 = next((e for e in elements if e["symbol"] == e1), None)
    elem2 = next((e for e in elements if e["symbol"] == e2), None)

    bond_type, bond_desc, molecule_prop = get_bond_info(e1, e2)

    st.subheader(f"🔗 {e1} - {e2} 결합 결과")
    st.write(f"✅ {elem1['name']} ({e1}, 원자번호 {elem1['atomic_number']}) → 특징: {elem1['feature']}")
    st.write(f"✅ {elem2['name']} ({e2}, 원자번호 {elem2['atomic_number']}) → 특징: {elem2['feature']}")

    st.markdown("---")
    st.write(f"**결합 종류**: {bond_type}")
    st.write(f"**결합 원리**: {bond_desc}")
    st.write(f"**생성 분자의 특성**: {molecule_prop}")

# ===============================
# 리셋 버튼
# ===============================
if st.button("🔄 선택 초기화"):
    st.session_state.selected = []
