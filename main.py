import streamlit as st

# 페이지 설정
st.set_page_config(page_title="🌟 MBTI 진로 추천기", page_icon="💼", layout="centered")

# 제목
st.title("🌟 MBTI 기반 직업 추천 사이트 💼✨")
st.write("당신의 **MBTI**를 선택하면, 성격에 맞는 멋진 직업을 추천해드려요! 🎯💡")

# MBTI 리스트
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI별 직업 추천 데이터 (이모지 포함)
job_recommendations = {
    "ISTJ": ["📊 회계사", "🏛️ 공무원", "📦 물류 관리자"],
    "ISFJ": ["🏥 간호사", "🍎 영양사", "📚 사서"],
    "INFJ": ["🎨 예술가", "🧠 상담사", "✍️ 작가"],
    "INTJ": ["💻 데이터 분석가", "🧪 연구원", "🏢 경영 컨설턴트"],
    "ISTP": ["🔧 기술자", "🚗 자동차 정비사", "🛠️ 목수"],
    "ISFP": ["🎶 음악가", "🖌️ 디자이너", "🌿 플로리스트"],
    "INFP": ["📖 작가", "🎭 배우", "🕊️ 사회운동가"],
    "INTP": ["🔬 과학자", "💡 발명가", "📐 엔지니어"],
    "ESTP": ["💼 영업사원", "🚀 스타트업 창업자", "🎯 스포츠 코치"],
    "ESFP": ["🎤 가수", "📺 방송인", "💃 무용가"],
    "ENFP": ["🌍 여행가", "🎨 창작자", "🎤 강연가"],
    "ENTP": ["🧠 기업가", "📢 마케터", "🎬 영화 제작자"],
    "ESTJ": ["🏢 관리자", "📈 경영자", "🚓 경찰관"],
    "ESFJ": ["👩‍🏫 교사", "🍽️ 요리사", "🤝 사회복지사"],
    "ENFJ": ["🎤 강사", "📚 교육 컨설턴트", "🎯 리더십 코치"],
    "ENTJ": ["💼 CEO", "📊 투자자", "🏛️ 정치가"]
}

# 선택 박스
selected_mbti = st.selectbox("🔍 당신의 MBTI를 선택하세요!", mbti_list)

# 추천 버튼
if st.button("💫 추천 받기 💫"):
    st.subheader(f"🌟 {selected_mbti} 타입을 위한 추천 직업 🌟")
    jobs = job_recommendations.get(selected_mbti, [])
    for job in jobs:
        st.markdown(f"- {job}")
    st.success("✨ 당신의 성향에 딱 맞는 직업들이에요! ✨")
    st.balloons()

# 하단 문구
st.write("---")
st.write("💡 **Tip:** MBTI는 참고용이며, 모든 직업은 당신의 노력과 열정에 따라 가능합니다! 🚀")
