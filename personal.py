import streamlit as st

# 페이지 설정
st.set_page_config(page_title="🎵 MBTI & 학년별 음악 추천", page_icon="🎧", layout="centered")

# 제목
st.title("🎵 MBTI & 학년별 맞춤 음악 추천 🌟")
st.write("당신의 **MBTI**와 **학년**을 선택하면, 요즘 HOT🔥한 음악 5곡을 추천해드립니다! 💃🕺")

# MBTI 리스트
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 학년 리스트
grade_list = ["중1", "중2", "중3", "고1", "고2", "고3"]

# MBTI+학년별 추천 음악 데이터 (예시)
# 실사용 시 최신 곡으로 업데이트 가능
music_recommendations = {
    ("ISTJ", "중1"): ["🎤 NewJeans - Super Shy", "🎧 IVE - I AM", "💃 BLACKPINK - Pink Venom", "🎶 세븐틴 - Super", "🔥 Stray Kids - S-Class"],
    ("ENFP", "고3"): ["🎤 BTS - Dynamite", "🎧 aespa - Spicy", "💃 TWICE - Set Me Free", "🎶 NewJeans - OMG", "🔥 ITZY - Cake"],
    # 모든 조합을 채우려면 여기서 확장
}

# 선택 입력
col1, col2 = st.columns(2)
with col1:
    selected_mbti = st.selectbox("💡 MBTI 선택", mbti_list)
with col2:
    selected_grade = st.selectbox("🏫 학년 선택", grade_list)

# 추천 버튼
if st.button("🎁 음악 추천 받기 🎁"):
    key = (selected_mbti, selected_grade)
    if key in music_recommendations:
        st.subheader(f"🌟 {selected_mbti} | {selected_grade} 추천 음악 🌟")
        for song in music_recommendations[key]:
            st.markdown(f"- {song}")
        st.balloons()
    else:
        st.warning("😅 아직 해당 조합의 음악 데이터가 없습니다. 곧 업데이트할게요!")

# 하단 안내
st.write("---")
st.info("💡 **Tip:** 음악은 취향에 따라 다를 수 있어요. 여러 곡 들어보고 마음에 드는 걸 찾아보세요! 🎧🎵")
