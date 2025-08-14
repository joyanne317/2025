import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="🎵 학년별 최신 음악 추천", page_icon="🎧", layout="centered")

# 제목
st.title("🎵 학년별 최신 인기 음악 추천 💃🕺")
st.write("🏫 학년을 선택하면, 요즘 **HOT🔥**한 음악 5곡을 추천해드려요! 🎶")

# 학년 리스트
grade_list = ["중1", "중2", "중3", "고1", "고2", "고3"]

# 학년별 추천 음악 데이터 (예시)
music_recommendations = {
    "중1": ["🎤 NewJeans - Super Shy", "💃 IVE - I AM", "🔥 Stray Kids - S-Class", "🎧 LE SSERAFIM - Eve, Psyche & The Bluebeard’s wife", "🌟 aespa - Spicy"],
    "중2": ["🎶 NewJeans - OMG", "🎤 BTS - Dynamite", "💃 BLACKPINK - Pink Venom", "🎧 ITZY - Cake", "🌈 SEVENTEEN - Super"],
    "중3": ["🔥 Stray Kids - God's Menu", "🎤 NewJeans - Hype Boy", "💃 TWICE - Set Me Free", "🎧 IVE - Love Dive", "🌟 aespa - Next Level"],
    "고1": ["🎶 BTS - Butter", "🎤 LE SSERAFIM - Unforgiven", "💃 ITZY - Wannabe", "🎧 BLACKPINK - Shut Down", "🌈 NewJeans - Attention"],
    "고2": ["🔥 IVE - After LIKE", "🎤 SEVENTEEN - HOT", "💃 TWICE - Fancy", "🎧 aespa - Savage", "🌟 BTS - Boy With Luv"],
    "고3": ["🎶 NewJeans - Ditto", "🎤 BLACKPINK - How You Like That", "💃 ITZY - Not Shy", "🎧 BTS - Idol", "🌈 IVE - Eleven"]
}

# 학년 선택
selected_grade = st.selectbox("🏫 학년을 선택하세요!", grade_list)

# 추천 버튼
if st.button("🎁 음악 추천 받기 🎁"):
    st.subheader(f"🌟 {selected_grade} 추천 음악 TOP 5 🌟")
    for song in music_recommendations[selected_grade]:
        st.markdown(f"- {song}")
    st.balloons()

# 하단 안내
st.write("---")
st.info("💡 **Tip:** 추천 음악은 매달 업데이트됩니다! 🎧")
