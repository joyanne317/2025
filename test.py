# -*- coding: utf-8 -*-
import streamlit as st

# 페이지 설정 및 배경 스타일 적용
st.set_page_config(layout="wide", page_title="나만의 주기율표")
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
    
    html, body, [class*="st-emotion-cache"] {
        font-family: 'Nanum Gothic', sans-serif;
    }

    /* 전체 배경 스타일 */
    .stApp {
        background: linear-gradient(to bottom right, #e0f2fe, #ffffff);
    }
    
    /* 주기율표 컨테이너 스타일 */
    .element-grid {
        display: grid;
        grid-template-columns: repeat(18, minmax(60px, 1fr));
        grid-gap: 5px;
        margin: 20px 0;
        align-items: center;
        justify-content: center;
    }
    
    /* 각 원소 칸 스타일 (버튼) */
    .element-cell {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 70px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
        border: 2px solid;
    }
    
    .element-cell:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
    }
    
    /* 금속, 준금속/비금속 색상 */
    .metal {
        background-color: #a0dfff; /* 하늘색 */
        border-color: #0077c9;
    }
    .nonmetal-metalloid {
        background-color: #fff9c4; /* 노란색 */
        border-color: #ffd700;
    }
    
    .element-number {
        font-size: 0.75em;
        align-self: flex-start;
        padding-left: 5px;
    }
    
    .element-symbol {
        font-size: 1.5em;
        font-weight: bold;
    }
    
    .element-name {
        font-size: 0.6em;
        text-align: center;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        padding: 0 2px;
    }
    
    /* 빈 칸 스타일 */
    .empty-cell {
        height: 70px;
    }
    
    /* 스티커용 이모지 스타일 */
    .sticker {
        font-size: 2em;
        position: absolute;
        animation: spin 10s linear infinite;
        z-index: 1;
    }
    
    .sticker-1 { top: 5%; left: 10%; }
    .sticker-2 { top: 15%; right: 5%; animation-duration: 15s; }
    .sticker-3 { bottom: 5%; left: 5%; animation-duration: 8s; }
    .sticker-4 { bottom: 10%; right: 15%; animation-duration: 12s; }

    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# 스티커 이모지 추가
st.markdown('<div class="sticker sticker-1">⚛️</div>', unsafe_allow_html=True)
st.markdown('<div class="sticker sticker-2">🔬</div>', unsafe_allow_html=True)
st.markdown('<div class="sticker sticker-3">🧪</div>', unsafe_allow_html=True)
st.markdown('<div class="sticker sticker-4">🧬</div>', unsafe_allow_html=True)

# 모든 원소 데이터 (118개)
elements_data = [
    {"number": 1, "symbol": "H", "name": "수소", "type": "비금속", "period": 1, "group": 1, "properties": "가장 가벼운 원소, 우주 질량의 75%를 차지함."},
    {"number": 2, "symbol": "He", "name": "헬륨", "type": "비금속", "period": 1, "group": 18, "properties": "무색, 무취의 비활성 기체. 풍선에 사용됨."},
    {"number": 3, "symbol": "Li", "name": "리튬", "type": "금속", "period": 2, "group": 1, "properties": "가장 가벼운 금속, 배터리 제조에 사용됨."},
    {"number": 4, "symbol": "Be", "name": "베릴륨", "type": "금속", "period": 2, "group": 2, "properties": "매우 단단하고 가벼운 금속. 항공우주 산업에 사용됨."},
    {"number": 5, "symbol": "B", "name": "붕소", "type": "준금속", "period": 2, "group": 13, "properties": "녹색 불꽃을 내는 원소. 붕산염으로 유리나 세제에 사용됨."},
    {"number": 6, "symbol": "C", "name": "탄소", "type": "비금속", "period": 2, "group": 14, "properties": "모든 유기물의 기본 원소. 다이아몬드, 흑연 형태를 가짐."},
    {"number": 7, "symbol": "N", "name": "질소", "type": "비금속", "period": 2, "group": 15, "properties": "지구 대기의 78%를 차지. 단백질의 필수 성분."},
    {"number": 8, "symbol": "O", "name": "산소", "type": "비금속", "period": 2, "group": 16, "properties": "호흡에 필수적인 기체. 지구 지각의 50% 이상을 차지."},
    {"number": 9, "symbol": "F", "name": "플루오린", "type": "비금속", "period": 2, "group": 17, "properties": "가장 반응성이 높은 원소. 불소치약에 사용됨."},
    {"number": 10, "symbol": "Ne", "name": "네온", "type": "비금속", "period": 2, "group": 18, "properties": "무색, 무취의 비활성 기체. 네온사인에 사용됨."},
    {"number": 11, "symbol": "Na", "name": "나트륨", "type": "금속", "period": 3, "group": 1, "properties": "매우 반응성이 높은 알칼리 금속. 염화나트륨(소금)의 주성분."},
    {"number": 12, "symbol": "Mg", "name": "마그네슘", "type": "금속", "period": 3, "group": 2, "properties": "가볍고 단단한 금속. 폭발물, 조명탄에 사용됨."},
    {"number": 13, "symbol": "Al", "name": "알루미늄", "type": "금속", "period": 3, "group": 13, "properties": "가볍고 부식에 강한 금속. 항공기, 건축 자재에 사용됨."},
    {"number": 14, "symbol": "Si", "name": "규소", "type": "준금속", "period": 3, "group": 14, "properties": "지구 지각에서 산소 다음으로 풍부한 원소. 반도체 재료로 사용됨."},
    {"number": 15, "symbol": "P", "name": "인", "type": "비금속", "period": 3, "group": 15, "properties": "생체 에너지 물질 ATP의 구성 원소. 성냥 제조에 사용됨."},
    {"number": 16, "symbol": "S", "name": "황", "type": "비금속", "period": 3, "group": 16, "properties": "특유의 냄새를 가진 노란색 고체. 화약, 비료에 사용됨."},
    {"number": 17, "symbol": "Cl", "name": "염소", "type": "비금속", "period": 3, "group": 17, "properties": "자극적인 냄새의 유독한 기체. 수돗물 소독에 사용됨."},
    {"number": 18, "symbol": "Ar", "name": "아르곤", "type": "비금속", "period": 3, "group": 18, "properties": "무색, 무취의 비활성 기체. 형광등 충전 기체로 사용됨."},
    {"number": 19, "symbol": "K", "name": "칼륨", "type": "금속", "period": 4, "group": 1, "properties": "매우 반응성이 높은 알칼리 금속. 동식물 생명 유지에 필수적."},
    {"number": 20, "symbol": "Ca", "name": "칼슘", "type": "금속", "period": 4, "group": 2, "properties": "뼈와 치아의 주성분. 시멘트와 석회 제조에 사용됨."},
    {"number": 21, "symbol": "Sc", "name": "스칸듐", "type": "금속", "period": 4, "group": 3, "properties": "가볍고 단단한 금속. 항공우주 부품에 사용됨."},
    {"number": 22, "symbol": "Ti", "name": "타이타늄", "type": "금속", "period": 4, "group": 4, "properties": "가볍고 강하며 부식에 강함. 인공 관절, 항공기 부품에 사용됨."},
    {"number": 23, "symbol": "V", "name": "바나듐", "type": "금속", "period": 4, "group": 5, "properties": "강철의 강도를 높이는 데 사용되는 단단한 금속."},
    {"number": 24, "symbol": "Cr", "name": "크로뮴", "type": "금속", "period": 4, "group": 6, "properties": "단단하고 빛나는 금속. 스테인리스강, 도금에 사용됨."},
    {"number": 25, "symbol": "Mn", "name": "망가니즈", "type": "금속", "period": 4, "group": 7, "properties": "강철 생산에 필수적인 금속. 건전지에도 사용됨."},
    {"number": 26, "symbol": "Fe", "name": "철", "type": "금속", "period": 4, "group": 8, "properties": "지구에서 가장 흔한 금속. 건축, 자동차 등 광범위하게 사용됨."},
    {"number": 27, "symbol": "Co", "name": "코발트", "type": "금속", "period": 4, "group": 9, "properties": "단단한 자성 금속. 배터리, 자석에 사용됨."},
    {"number": 28, "symbol": "Ni", "name": "니켈", "type": "금속", "period": 4, "group": 10, "properties": "은백색의 단단한 금속. 합금, 동전, 배터리에 사용됨."},
    {"number": 29, "symbol": "Cu", "name": "구리", "type": "금속", "period": 4, "group": 11, "properties": "열과 전기 전도성이 뛰어남. 전선, 동전에 사용됨."},
    {"number": 30, "symbol": "Zn", "name": "아연", "type": "금속", "period": 4, "group": 12, "properties": "철의 부식을 막는 데 사용. 건전지, 합금에 사용됨."},
    {"number": 31, "symbol": "Ga", "name": "갈륨", "type": "금속", "period": 4, "group": 13, "properties": "손바닥 온도에서 녹는 금속. 반도체, LED에 사용됨."},
    {"number": 32, "symbol": "Ge", "name": "저마늄", "type": "준금속", "period": 4, "group": 14, "properties": "반도체 재료로 사용됨. 광섬유에도 쓰임."},
    {"number": 33, "symbol": "As", "name": "비소", "type": "준금속", "period": 4, "group": 15, "properties": "독성이 강한 물질. 반도체, 살충제에 사용됨."},
    {"number": 34, "symbol": "Se", "name": "셀레늄", "type": "비금속", "period": 4, "group": 16, "properties": "빛에 따라 전기 전도도가 변함. 복사기, 태양 전지에 사용됨."},
    {"number": 35, "symbol": "Br", "name": "브로민", "type": "비금속", "period": 4, "group": 17, "properties": "상온에서 액체인 유일한 비금속 원소. 난연제에 사용됨."},
    {"number": 36, "symbol": "Kr", "name": "크립톤", "type": "비금속", "period": 4, "group": 18, "properties": "무색, 무취의 비활성 기체. 고속 카메라 플래시에 사용됨."},
    {"number": 37, "symbol": "Rb", "name": "루비듐", "type": "금속", "period": 5, "group": 1, "properties": "매우 반응성이 높은 알칼리 금속. 광전지에 사용됨."},
    {"number": 38, "symbol": "Sr", "name": "스트론튬", "type": "금속", "period": 5, "group": 2, "properties": "불꽃놀이에서 붉은색을 냄."},
    {"number": 39, "symbol": "Y", "name": "이트륨", "type": "금속", "period": 5, "group": 3, "properties": "텔레비전 화면의 빨간색 발광체로 사용됨."},
    {"number": 40, "symbol": "Zr", "name": "지르코늄", "type": "금속", "period": 5, "group": 4, "properties": "부식에 강하고 핵 반응로의 연료봉 피복재로 사용됨."},
    {"number": 41, "symbol": "Nb", "name": "나이오븀", "type": "금속", "period": 5, "group": 5, "properties": "강철의 강도를 높이고 초전도 자석에 사용됨."},
    {"number": 42, "symbol": "Mo", "name": "몰리브데넘", "type": "금속", "period": 5, "group": 6, "properties": "매우 단단하고 내열성이 높음. 합금에 사용됨."},
    {"number": 43, "symbol": "Tc", "name": "테크네튬", "type": "금속", "period": 5, "group": 7, "properties": "인공적으로 만들어진 첫 번째 원소. 방사성."},
    {"number": 44, "symbol": "Ru", "name": "루테늄", "type": "금속", "period": 5, "group": 8, "properties": "백금족 금속 중 하나. 합금, 촉매에 사용됨."},
    {"number": 45, "symbol": "Rh", "name": "로듐", "type": "금속", "period": 5, "group": 9, "properties": "매우 희귀하고 부식에 강한 백금족 금속. 촉매 변환기에 사용됨."},
    {"number": 46, "symbol": "Pd", "name": "팔라듐", "type": "금속", "period": 5, "group": 10, "properties": "백금족 금속. 촉매 변환기, 보석에 사용됨."},
    {"number": 47, "symbol": "Ag", "name": "은", "type": "금속", "period": 5, "group": 11, "properties": "최고의 전기 및 열 전도성. 보석, 화폐에 사용됨."},
    {"number": 48, "symbol": "Cd", "name": "카드뮴", "type": "금속", "period": 5, "group": 12, "properties": "독성이 있는 금속. 니켈-카드뮴 배터리에 사용됨."},
    {"number": 49, "symbol": "In", "name": "인듐", "type": "금속", "period": 5, "group": 13, "properties": "매우 부드러운 금속. 투명 전극, LCD 화면에 사용됨."},
    {"number": "50", "symbol": "Sn", "name": "주석", "type": "금속", "period": 5, "group": 14, "properties": "부드럽고 잘 녹는 금속. 통조림 코팅에 사용됨."},
    {"number": "51", "symbol": "Sb", "name": "안티모니", "type": "준금속", "period": 5, "group": 15, "properties": "금속과 비금속의 성질을 모두 가짐. 반도체, 합금에 사용됨."},
    {"number": "52", "symbol": "Te", "name": "텔루륨", "type": "준금속", "period": 5, "group": 16, "properties": "반도체, 합금에 사용되는 은백색의 준금속."},
    {"number": "53", "symbol": "I", "name": "아이오딘", "type": "비금속", "period": 5, "group": 17, "properties": "상온에서 보라색 고체. 소독약으로 사용됨."},
    {"number": "54", "symbol": "Xe", "name": "제논", "type": "비금속", "period": 5, "group": 18, "properties": "무색, 무취의 비활성 기체. 전구, 섬광등에 사용됨."},
    {"number": "55", "symbol": "Cs", "name": "세슘", "type": "금속", "period": 6, "group": 1, "properties": "가장 반응성이 높은 알칼리 금속. 원자 시계에 사용됨."},
    {"number": "56", "symbol": "Ba", "name": "바륨", "type": "금속", "period": 6, "group": 2, "properties": "녹색 불꽃을 냄. 의료용 조영제로 사용됨."},
    {"number": "57", "symbol": "La", "name": "란타넘", "type": "금속", "period": 6, "group": 3, "properties": "희토류 원소 중 하나. 광학 렌즈에 사용됨."},
    {"number": "58", "symbol": "Ce", "name": "세륨", "type": "금속", "period": 6, "group": 3, "properties": "라이터 돌에 사용되는 희토류 금속."},
    {"number": "59", "symbol": "Pr", "name": "프라세오디뮴", "type": "금속", "period": 6, "group": 3, "properties": "유리, 세라믹의 녹색 색소로 사용됨."},
    {"number": "60", "symbol": "Nd", "name": "네오디뮴", "type": "금속", "period": 6, "group": 3, "properties": "가장 강력한 영구 자석을 만드는 데 사용됨."},
    {"number": "61", "symbol": "Pm", "name": "프로메튬", "type": "금속", "period": 6, "group": 3, "properties": "방사성을 띠는 희토류 원소."},
    {"number": "62", "symbol": "Sm", "name": "사마륨", "type": "금속", "period": 6, "group": 3, "properties": "강력한 영구 자석, 중성자 흡수재로 사용됨."},
    {"number": "63", "symbol": "Eu", "name": "유로퓸", "type": "금속", "period": 6, "group": 3, "properties": "텔레비전 화면의 빨간색 발광체로 사용됨."},
    {"number": "64", "symbol": "Gd", "name": "가돌리늄", "type": "금속", "period": 6, "group": 3, "properties": "자기 공명 영상(MRI) 조영제로 사용됨."},
    {"number": "65", "symbol": "Tb", "name": "터븀", "type": "금속", "period": 6, "group": 3, "properties": "형광등, 텔레비전 화면의 녹색 발광체로 사용됨."},
    {"number": "66", "symbol": "Dy", "name": "디스프로슘", "type": "금속", "period": 6, "group": 3, "properties": "강력한 영구 자석에 사용됨."},
    {"number": "67", "symbol": "Ho", "name": "홀뮴", "type": "금속", "period": 6, "group": 3, "properties": "가장 강력한 자성 원소. 레이저에 사용됨."},
    {"number": "68", "symbol": "Er", "name": "어븀", "type": "금속", "period": 6, "group": 3, "properties": "광섬유, 레이저에 사용됨."},
    {"number": "69", "symbol": "Tm", "name": "툴륨", "type": "금속", "period": 6, "group": 3, "properties": "휴대용 엑스선 장치에 사용됨."},
    {"number": "70", "symbol": "Yb", "name": "이터븀", "type": "금속", "period": 6, "group": 3, "properties": "금속학, 광섬유 통신에 사용됨."},
    {"number": "71", "symbol": "Lu", "name": "루테튬", "type": "금속", "period": 6, "group": 3, "properties": "가장 희귀하고 비싼 희토류 금속 중 하나."},
    {"number": "72", "symbol": "Hf", "name": "하프늄", "type": "금속", "period": 6, "group": 4, "properties": "핵 반응로의 제어봉 재료로 사용됨."},
    {"number": "73", "symbol": "Ta", "name": "탄탈럼", "type": "금속", "period": 6, "group": 5, "properties": "부식에 매우 강함. 휴대폰, 카메라 렌즈에 사용됨."},
    {"number": "74", "symbol": "W", "name": "텅스텐", "type": "금속", "period": 6, "group": 6, "properties": "가장 높은 녹는점을 가진 금속. 전구 필라멘트에 사용됨."},
    {"number": "75", "symbol": "Re", "name": "레늄", "type": "금속", "period": 6, "group": 7, "properties": "매우 희귀한 금속. 제트 엔진에 사용됨."},
    {"number": "76", "symbol": "Os", "name": "오스뮴", "type": "금속", "period": 6, "group": 8, "properties": "가장 밀도가 높은 원소. 만년필 펜촉에 사용됨."},
    {"number": "77", "symbol": "Ir", "name": "이리듐", "type": "금속", "period": 6, "group": 9, "properties": "매우 희귀하고 부식에 강함. 만년필, 엔진 부품에 사용됨."},
    {"number": "78", "symbol": "Pt", "name": "백금", "type": "금속", "period": 6, "group": 10, "properties": "부식에 강하고 아름다움. 보석, 촉매에 사용됨."},
    {"number": "79", "symbol": "Au", "name": "금", "type": "금속", "period": 6, "group": 11, "properties": "아름답고 부식에 강함. 보석, 전자제품에 사용됨."},
    {"number": "80", "symbol": "Hg", "name": "수은", "type": "금속", "period": 6, "group": 12, "properties": "상온에서 액체인 유일한 금속 원소. 온도계에 사용됨."},
    {"number": "81", "symbol": "Tl", "name": "탈륨", "type": "금속", "period": 6, "group": 13, "properties": "매우 유독한 금속. 광전자 장치에 사용됨."},
    {"number": "82", "symbol": "Pb", "name": "납", "type": "금속", "period": 6, "group": 14, "properties": "무르고 녹는점이 낮음. 배터리, 납땜에 사용됨."},
    {"number": "83", "symbol": "Bi", "name": "비스무트", "type": "금속", "period": 6, "group": 15, "properties": "녹는점이 낮고 자성체가 아님. 화장품, 의약품에 사용됨."},
    {"number": "84", "symbol": "Po", "name": "폴로늄", "type": "준금속", "period": 6, "group": 16, "properties": "매우 높은 방사능을 가진 준금속."},
    {"number": "85", "symbol": "At", "name": "아스타틴", "type": "준금속", "period": 6, "group": 17, "properties": "지구상에 극히 드문 방사성 준금속."},
    {"number": "86", "symbol": "Rn", "name": "라돈", "type": "비금속", "period": 6, "group": 18, "properties": "방사성 비활성 기체. 폐암의 원인이 될 수 있음."},
    {"number": "87", "symbol": "Fr", "name": "프랑슘", "type": "금속", "period": 7, "group": 1, "properties": "매우 불안정한 방사성 알칼리 금속."},
    {"number": "88", "symbol": "Ra", "name": "라듐", "type": "금속", "period": 7, "group": 2, "properties": "매우 높은 방사능을 가진 알칼리 토금속. 암 치료에 사용됨."},
    {"number": "89", "symbol": "Ac", "name": "악티늄", "type": "금속", "period": 7, "group": 3, "properties": "방사성을 띠는 악티늄족 원소. 방사선원으로 사용됨."},
    {"number": "90", "symbol": "Th", "name": "토륨", "type": "금속", "period": 7, "group": 3, "properties": "방사성 원소. 핵연료로 사용될 가능성이 있음."},
    {"number": "91", "symbol": "Pa", "name": "프로탁티늄", "type": "금속", "period": 7, "group": 3, "properties": "매우 희귀하고 독성이 강한 방사성 원소."},
    {"number": "92", "symbol": "U", "name": "우라늄", "type": "금속", "period": 7, "group": 3, "properties": "핵발전, 핵무기에 사용되는 방사성 원소."},
    {"number": "93", "symbol": "Np", "name": "넵투늄", "type": "금속", "period": 7, "group": 3, "properties": "핵반응로에서 생성되는 인공 원소."},
    {"number": "94", "symbol": "Pu", "name": "플루토늄", "type": "금속", "period": 7, "group": 3, "properties": "핵무기, 원자로에 사용되는 인공 방사성 원소."},
    {"number": "95", "symbol": "Am", "name": "아메리슘", "type": "금속", "period": 7, "group": 3, "properties": "연기 감지기에 사용되는 인공 방사성 원소."},
    {"number": "96", "symbol": "Cm", "name": "퀴륨", "type": "금속", "period": 7, "group": 3, "properties": "매우 높은 방사능을 가진 인공 원소."},
    {"number": "97", "symbol": "Bk", "name": "버클륨", "type": "금속", "period": 7, "group": 3, "properties": "사이클로트론에서 생성되는 인공 원소."},
    {"number": "98", "symbol": "Cf", "name": "캘리포늄", "type": "금속", "period": 7, "group": 3, "properties": "중성자원으로 사용되는 인공 원소."},
    {"number": "99", "symbol": "Es", "name": "아인슈타이늄", "type": "금속", "period": 7, "group": 3, "properties": "수소 폭탄 실험의 부산물로 발견된 인공 원소."},
    {"number": "100", "symbol": "Fm", "name": "페르뮴", "type": "금속", "period": 7, "group": 3, "properties": "핵폭탄 실험에서 처음 발견된 인공 원소."},
    {"number": "101", "symbol": "Md", "name": "멘델레븀", "type": "금속", "period": 7, "group": 3, "properties": "원자 충돌 실험으로 만들어진 인공 원소."},
    {"number": "102", "symbol": "No", "name": "노벨륨", "type": "금속", "period": 7, "group": 3, "properties": "매우 짧은 반감기를 가진 인공 원소."},
    {"number": "103", "symbol": "Lr", "name": "로렌슘", "type": "금속", "period": 7, "group": 3, "properties": "가장 무거운 악티늄족 원소."},
    {"number": "104", "symbol": "Rf", "name": "러더포듐", "type": "금속", "period": 7, "group": 4, "properties": "인공적으로 합성된 원소. 매우 불안정."},
    {"number": "105", "symbol": "Db", "name": "더브늄", "type": "금속", "period": 7, "group": 5, "properties": "인공적으로 합성된 원소. 매우 짧은 반감기."},
    {"number": "106", "symbol": "Sg", "name": "시보귬", "type": "금속", "period": 7, "group": 6, "properties": "인공적으로 합성된 원소."},
    {"number": "107", "symbol": "Bh", "name": "보륨", "type": "금속", "period": 7, "group": 7, "properties": "인공적으로 합성된 원소."},
    {"number": "108", "symbol": "Hs", "name": "하슘", "type": "금속", "period": 7, "group": 8, "properties": "인공적으로 합성된 원소."},
    {"number": "109", "symbol": "Mt", "name": "마이트너륨", "type": "금속", "period": 7, "group": 9, "properties": "인공적으로 합성된 원소."},
    {"number": "110", "symbol": "Ds", "name": "다름슈타튬", "type": "금속", "period": 7, "group": 10, "properties": "인공적으로 합성된 원소."},
    {"number": "111", "symbol": "Rg", "name": "뢴트게늄", "type": "금속", "period": 7, "group": 11, "properties": "인공적으로 합성된 원소."},
    {"number": "112", "symbol": "Cn", "name": "코페르니슘", "type": "금속", "period": 7, "group": 12, "properties": "인공적으로 합성된 원소."},
    {"number": "113", "symbol": "Nh", "name": "니호늄", "type": "금속", "period": 7, "group": 13, "properties": "인공적으로 합성된 원소."},
    {"number": "114", "symbol": "Fl", "name": "플레로븀", "type": "금속", "period": 7, "group": 14, "properties": "인공적으로 합성된 원소."},
    {"number": "115", "symbol": "Mc", "name": "모스코븀", "type": "금속", "period": 7, "group": 15, "properties": "인공적으로 합성된 원소."},
    {"number": "116", "symbol": "Lv", "name": "리버모륨", "type": "금속", "period": 7, "group": 16, "properties": "인공적으로 합성된 원소."},
    {"number": "117", "symbol": "Ts", "name": "테네신", "type": "비금속", "period": 7, "group": 17, "properties": "인공적으로 합성된 원소."},
    {"number": "118", "symbol": "Og", "name": "오가네손", "type": "비금속", "period": 7, "group": 18, "properties": "인공적으로 합성된 원소."},
]

# 란타넘족과 악티늄족 데이터
lanthanides_data = [d for d in elements_data if d["number"] in range(57, 72)]
actinides_data = [d for d in elements_data if d["number"] in range(89, 104)]

# Session State 초기화
if 'selected_elements' not in st.session_state:
    st.session_state.selected_elements = []

def get_element_info(symbol):
    """원소 기호를 바탕으로 원소 데이터를 찾습니다."""
    for element in elements_data:
        if element["symbol"] == symbol:
            return element
    return None

def display_bond_info(elements):
    """선택된 원소들의 결합 정보를 표시합니다."""
    st.markdown("---")
    st.subheader("🧪 원소 결합 정보")
    
    if len(elements) < 2:
        st.warning("결합 정보를 보려면 2개 이상의 원소를 선택해주세요.")
        return

    # 선택된 원소들의 타입 확인
    types = [e["type"] for e in elements]
    
    # 결합 종류 판별
    bond_type = "기타 결합"
    bond_properties = "해당 원소들의 결합 종류는 복잡하여 여기에 설명되지 않았습니다."
    molecule_properties = "예상 분자의 특징은 복잡하며 추가 분석이 필요합니다."
    
    if "금속" in types and "비금속" in types:
        bond_type = "이온 결합 (Ionic bond)"
        bond_properties = "금속 원소와 비금속 원소가 만나 전자를 주고받아 형성되는 정전기적 인력에 의한 결합입니다. 주로 안정한 이온 화합물을 형성합니다."
        molecule_properties = "결합된 분자는 단단한 결정 구조를 가지며, 수용액 상태에서 전기가 잘 통합니다."
    elif all(t == "비금속" for t in types):
        bond_type = "공유 결합 (Covalent bond)"
        bond_properties = "두 비금속 원자가 서로 전자를 공유하여 형성하는 결합입니다. 주로 분자 화합물을 형성하며, 액체나 기체 상태로 존재할 수 있습니다."
        molecule_properties = "결합된 분자는 비교적 약한 분자간 힘을 가지며, 녹는점과 끓는점이 낮습니다."
    elif all(t == "금속" for t in types):
        bond_type = "합금 (Alloy)"
        bond_properties = "두 가지 이상의 금속 원소가 섞여 형성되는 물질입니다. 금속 결합의 일종으로, 기존 금속보다 강도, 내식성 등이 우수할 수 있습니다."
        molecule_properties = "결합된 물질은 금속의 성질을 가지며, 주로 고체 상태로 존재합니다."
        
    st.markdown(f"**결합 종류:** {bond_type}")
    st.markdown(f"**결합 종류의 특징:** {bond_properties}")
    st.markdown(f"**결합된 분자의 특징:** {molecule_properties}")
    st.markdown("---")
    st.subheader("💡 결합에 사용된 원소의 특징")
    for element in elements:
        st.markdown(f"**[{element['symbol']}]** {element['name']}: {element['properties']}")

# 주기율표 렌더링
st.title("나만의 주기율표 ⚛️")
st.markdown("---")

# 주기율표 본문
with st.container():
    st.markdown('<div class="element-grid">', unsafe_allow_html=True)
    
    # 그룹 번호 헤더
    st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True) # 공백
    st.markdown('<div>**1**</div>', unsafe_allow_html=True)
    st.markdown('<div>**2**</div>', unsafe_allow_html=True)
    st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)
    st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)
    st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)
    st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)
    st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)
    st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)
    st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)
    st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)
    st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)
    st.markdown('<div>**13**</div>', unsafe_allow_html=True)
    st.markdown('<div>**14**</div>', unsafe_allow_html=True)
    st.markdown('<div>**15**</div>', unsafe_allow_html=True)
    st.markdown('<div>**16**</div>', unsafe_allow_html=True)
    st.markdown('<div>**17**</div>', unsafe_allow_html=True)
    st.markdown('<div>**18**</div>', unsafe_allow_html=True)

    # 주기율표 레이아웃
    grid_data = [
        {"period": 1, "group": 1},
        {"period": 1, "group": 18},
        {"period": 2, "group": 1},
        {"period": 2, "group": 2},
        {"period": 2, "group": 13},
        {"period": 2, "group": 14},
        {"period": 2, "group": 15},
        {"period": 2, "group": 16},
        {"period": 2, "group": 17},
        {"period": 2, "group": 18},
        {"period": 3, "group": 1},
        {"period": 3, "group": 2},
        {"period": 3, "group": 13},
        {"period": 3, "group": 14},
        {"period": 3, "group": 15},
        {"period": 3, "group": 16},
        {"period": 3, "group": 17},
        {"period": 3, "group": 18},
        {"period": 4, "group": 1, "end": 18},
        {"period": 5, "group": 1, "end": 18},
        {"period": 6, "group": 1},
        {"period": 6, "group": 2},
        {"period": 6, "group": 3},
        {"period": 6, "group": 4, "end": 18},
        {"period": 7, "group": 1},
        {"period": 7, "group": 2},
        {"period": 7, "group": 3},
        {"period": 7, "group": 4, "end": 18},
    ]

    # 주기율표 생성
    current_grid_pos = 0
    total_cells = 18 * 7 + 34  # 전체 셀 수 (빈칸 포함)
    
    element_map = {(e['period'], e['group']): e for e in elements_data}

    # 1, 2주기
    for period in range(1, 3):
        col_list = st.columns(18)
        for group in range(1, 19):
            if (period, group) in element_map:
                element = element_map[(period, group)]
                color_class = "metal" if element["type"] == "금속" else "nonmetal-metalloid"
                with col_list[group-1]:
                    if st.button(f"""
                        <div class="element-cell {color_class}">
                            <div class="element-number">{element['number']}</div>
                            <div class="element-symbol">{element['symbol']}</div>
                            <div class="element-name">{element['name']}</div>
                        </div>
                    """, key=f"element-{element['symbol']}", unsafe_allow_html=True):
                        st.session_state.last_selected = element['symbol']
                        if element['symbol'] in [e['symbol'] for e in st.session_state.selected_elements]:
                            st.session_state.selected_elements.remove(element)
                        else:
                            st.session_state.selected_elements.append(element)
            else:
                with col_list[group-1]:
                    st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)

    # 3주기
    col_list = st.columns(18)
    for group in range(1, 19):
        if (3, group) in element_map:
            element = element_map[(3, group)]
            color_class = "metal" if element["type"] == "금속" else "nonmetal-metalloid"
            with col_list[group-1]:
                if st.button(f"""
                    <div class="element-cell {color_class}">
                        <div class="element-number">{element['number']}</div>
                        <div class="element-symbol">{element['symbol']}</div>
                        <div class="element-name">{element['name']}</div>
                    </div>
                """, key=f"element-{element['symbol']}", unsafe_allow_html=True):
                    st.session_state.last_selected = element['symbol']
                    if element['symbol'] in [e['symbol'] for e in st.session_state.selected_elements]:
                        st.session_state.selected_elements.remove(element)
                    else:
                        st.session_state.selected_elements.append(element)
        else:
            with col_list[group-1]:
                st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)

    # 4-5주기
    for period in range(4, 6):
        col_list = st.columns(18)
        for group in range(1, 19):
            if (period, group) in element_map:
                element = element_map[(period, group)]
                color_class = "metal" if element["type"] == "금속" else "nonmetal-metalloid"
                with col_list[group-1]:
                    if st.button(f"""
                        <div class="element-cell {color_class}">
                            <div class="element-number">{element['number']}</div>
                            <div class="element-symbol">{element['symbol']}</div>
                            <div class="element-name">{element['name']}</div>
                        </div>
                    """, key=f"element-{element['symbol']}", unsafe_allow_html=True):
                        st.session_state.last_selected = element['symbol']
                        if element['symbol'] in [e['symbol'] for e in st.session_state.selected_elements]:
                            st.session_state.selected_elements.remove(element)
                        else:
                            st.session_state.selected_elements.append(element)

    # 6주기
    col_list = st.columns(18)
    for group in range(1, 19):
        if (6, group) in element_map:
            element = element_map[(6, group)]
            color_class = "metal" if element["type"] == "금속" else "nonmetal-metalloid"
            with col_list[group-1]:
                if group == 3:
                    st.markdown("""
                        <div class="empty-cell" style="display: flex; flex-direction: column; justify-content: center; align-items: center; background-color: #e0f2fe; border-radius: 12px; border: 2px solid #0077c9; padding: 5px;">
                            <div style="font-size: 0.8em;">57-71</div>
                            <div style="font-size: 0.7em;">란타넘족</div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    if st.button(f"""
                        <div class="element-cell {color_class}">
                            <div class="element-number">{element['number']}</div>
                            <div class="element-symbol">{element['symbol']}</div>
                            <div class="element-name">{element['name']}</div>
                        </div>
                    """, key=f"element-{element['symbol']}", unsafe_allow_html=True):
                        st.session_state.last_selected = element['symbol']
                        if element['symbol'] in [e['symbol'] for e in st.session_state.selected_elements]:
                            st.session_state.selected_elements.remove(element)
                        else:
                            st.session_state.selected_elements.append(element)
        else:
            with col_list[group-1]:
                st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)
    
    # 7주기
    col_list = st.columns(18)
    for group in range(1, 19):
        if (7, group) in element_map:
            element = element_map[(7, group)]
            color_class = "metal" if element["type"] == "금속" else "nonmetal-metalloid"
            with col_list[group-1]:
                if group == 3:
                    st.markdown("""
                        <div class="empty-cell" style="display: flex; flex-direction: column; justify-content: center; align-items: center; background-color: #e0f2fe; border-radius: 12px; border: 2px solid #0077c9; padding: 5px;">
                            <div style="font-size: 0.8em;">89-103</div>
                            <div style="font-size: 0.7em;">악티늄족</div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    if st.button(f"""
                        <div class="element-cell {color_class}">
                            <div class="element-number">{element['number']}</div>
                            <div class="element-symbol">{element['symbol']}</div>
                            <div class="element-name">{element['name']}</div>
                        </div>
                    """, key=f"element-{element['symbol']}", unsafe_allow_html=True):
                        st.session_state.last_selected = element['symbol']
                        if element['symbol'] in [e['symbol'] for e in st.session_state.selected_elements]:
                            st.session_state.selected_elements.remove(element)
                        else:
                            st.session_state.selected_elements.append(element)
        else:
            with col_list[group-1]:
                st.markdown('<div class="empty-cell"></div>', unsafe_allow_html=True)

    # 란타넘족과 악티늄족 분리 표
    st.markdown("---")
    st.markdown("##### 란타넘족 (Lanthanides) & 악티늄족 (Actinides)")
    st.markdown("")

    # 란타넘족
    lanthanide_columns = st.columns(len(lanthanides_data))
    for i, element in enumerate(lanthanides_data):
        color_class = "metal" if element["type"] == "금속" else "nonmetal-metalloid"
        with lanthanide_columns[i]:
            if st.button(f"""
                <div class="element-cell {color_class}">
                    <div class="element-number">{element['number']}</div>
                    <div class="element-symbol">{element['symbol']}</div>
                    <div class="element-name">{element['name']}</div>
                </div>
            """, key=f"lanthanide-{element['symbol']}", unsafe_allow_html=True):
                st.session_state.last_selected = element['symbol']
                if element['symbol'] in [e['symbol'] for e in st.session_state.selected_elements]:
                    st.session_state.selected_elements.remove(element)
                else:
                    st.session_state.selected_elements.append(element)
    
    st.markdown("") # 공백
    
    # 악티늄족
    actinide_columns = st.columns(len(actinides_data))
    for i, element in enumerate(actinides_data):
        color_class = "metal" if element["type"] == "금속" else "nonmetal-metalloid"
        with actinide_columns[i]:
            if st.button(f"""
                <div class="element-cell {color_class}">
                    <div class="element-number">{element['number']}</div>
                    <div class="element-symbol">{element['symbol']}</div>
                    <div class="element-name">{element['name']}</div>
                </div>
            """, key=f"actinide-{element['symbol']}", unsafe_allow_html=True):
                st.session_state.last_selected = element['symbol']
                if element['symbol'] in [e['symbol'] for e in st.session_state.selected_elements]:
                    st.session_state.selected_elements.remove(element)
                else:
                    st.session_state.selected_elements.append(element)

# 사이드바에 정보 표시
st.sidebar.header("선택된 원소 정보")

if st.session_state.selected_elements:
    selected_symbols = ", ".join([e["symbol"] for e in st.session_state.selected_elements])
    st.sidebar.markdown(f"**선택된 원소:** {selected_symbols}")
    
    for element in st.session_state.selected_elements:
        st.sidebar.markdown(f"---")
        st.sidebar.subheader(f"{element['symbol']} - {element['name']}")
        st.sidebar.write(f"**원소 번호:** {element['number']}")
        st.sidebar.write(f"**원소 종류:** {element['type']}")
        st.sidebar.write(f"**특징:** {element['properties']}")

    display_bond_info(st.session_state.selected_elements)
    
    if st.sidebar.button("선택 초기화"):
        st.session_state.selected_elements = []
        st.rerun()

else:
    st.sidebar.info("원소를 클릭하여 정보를 확인하세요.")
