import streamlit as st

# MBTI 유형별 직업 추천 데이터 (예시)
# 실제 데이터는 더 상세하고 정확하게 작성해야 함
mbti_jobs = {
    'ENFJ': ['선생님', '상담사', '인사 담당자'],
    'ENTP': ['변호사', '마케팅 전문가', '기업가'],
    'ISFJ': ['사회복지사', '간호사', '사서'],
    'INFP': ['작가', '디자이너', '심리학자'],
    'ESTJ': ['경영인', '공무원', '회계사'],
    'ISTP': ['기술자', '경찰관', '소방관'],
    'ESFP': ['연기자', '가이드', '유치원 교사'],
    'INFJ': ['예술가', '성직자', '컨설턴트'],
    'ISTJ': ['정보보안 전문가', '은행원', '공무원'],
    'ESFJ': ['영업 관리자', '교사', '승무원'],
    'ENTJ': ['사업가', '변호사', '기업 CEO'],
    'INTJ': ['과학자', '프로그래머', '분석가'],
    'ESTP': ['운동선수', '소방관', '영업사원'],
    'INTP': ['연구원', '교수', '프로그래머'],
    'ENFP': ['방송인', '광고 기획자', '이벤트 기획자'],
    'ISFP': ['미용사', '요리사', '패션 디자이너'],
}

# 웹사이트 제목
st.title('MBTI 기반 진로 추천 사이트')

# MBTI 유형 선택
st.sidebar.header('나의 MBTI 유형은?')
mbti_list = sorted(list(mbti_jobs.keys()))
selected_mbti = st.sidebar.selectbox('MBTI 유형을 선택하세요.', mbti_list)

# 선택된 MBTI에 대한 직업 추천
if selected_mbti:
    st.header(f'**{selected_mbti}** 유형에게 적합한 직업은 다음과 같아요.')
    jobs = mbti_jobs.get(selected_mbti, [])
    
    # 추천 직업을 리스트로 보여줌
    if jobs:
        for job in jobs:
            st.success(f'✅ {job}')
    else:
        st.info('아직 등록된 직업이 없습니다.')

# 추가 설명
st.markdown("""
<br>
<hr>
<br>
이 웹사이트는 **진로 탐색**을 위한 보조 도구로 활용될 수 있으며,
실제 직업 선택은 개인의 적성과 흥미를 고려하여 신중하게 결정해야 합니다.
""", unsafe_allow_html=True)
