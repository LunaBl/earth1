import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="우주의 신비",
    layout="wide",
)

# CSS 스타일을 하나의 문자열로 정의
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

/* 전체 페이지 기본 스타일 */
body {
    font-family: 'Poppins', sans-serif;
    color: #ADD8E6;
}

/* 가장 바깥쪽 컨테이너에 배경색 적용 및 컨텐츠가 위에 오도록 설정 */
.stApp {
    background-color: #000;
    position: relative;
    overflow: hidden;
    color: white; /* 텍스트 색상을 기본적으로 흰색으로 설정하여 보이게 함 */
}

/* 별 반짝임 효과 (CSS 애니메이션) */
.stApp::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: transparent url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4' viewBox='0 0 4 4'%3E%3Cpath fill='%23ffffff' d='M1 0h1v1H1V0zm1 1h1v1H2V1zM0 2h1v1H0V2zm2 2h1v1H2V4z'/%3E%3C/svg%3E") repeat;
    opacity: 0.6;
    animation: star-glow 6s ease-in-out infinite;
    z-index: -1;
}

@keyframes star-glow {
    0% { opacity: 0.2; }
    50% { opacity: 0.8; }
    100% { opacity: 0.2; }
}

/* 모든 글자에 은하 그라데이션 적용 */
.stMarkdown, h1, h2, h3 {
    background: linear-gradient(45deg, #00BFFF, #1E90FF, #00BFFF, #87CEFA, #4682B4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 10px rgba(0, 191, 255, 0.5), 0 0 20px rgba(0, 191, 255, 0.3);
}

/* 제목 스타일 (추가적인 크기/위치 조정) */
.main-title, .star-title {
    font-size: 4rem;
    font-weight: 600;
    text-align: center;
    padding-top: 50px;
    position: relative;
    z-index: 10; /* 글자가 배경보다 위에 오도록 z-index 설정 */
}

/* 텍스트 스타일 */
.intro-text, .star-text {
    font-size: 1.2rem;
    text-align: center;
    margin-top: 20px;
    line-height: 1.6;
    position: relative;
    z-index: 10;
}

/* 버튼 컨테이너: 버튼을 중앙으로 정렬 */
.button-container {
    display: flex;
    justify-content: center;
    margin-top: 40px;
    position: relative;
    z-index: 10;
}

/* 버튼 스타일 */
.stButton>button {
    background-color: transparent !important;
    border: 2px solid #00BFFF !important;
    color: #00BFFF !important;
    font-size: 1.2rem;
    font-weight: 600;
    padding: 10px 30px;
    border-radius: 5px;
    transition: all 0.3s ease-in-out;
    cursor: pointer;
    text-shadow: 0 0 10px #00BFFF;
    display: block;
}

.stButton>button:hover {
    background-color: #00BFFF !important;
    color: #000 !important;
    box-shadow: 0 0 20px #00BFFF;
    transform: scale(1.05);
}
</style>
"""

# 커스텀 CSS 적용
st.markdown(custom_css, unsafe_allow_html=True)

# 페이지 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "main"

# 메인 페이지
if st.session_state.page == "main":
    st.markdown("<h1 class='main-title'>별의 신비</h1>", unsafe_allow_html=True)
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    if st.button("별의 진화"):
        st.session_state.page = "star_evolution"
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<p class='intro-text'>우주의 광활함 속에서 빛나는 별들의 이야기를 탐험해 보세요.</p>", unsafe_allow_html=True)

# 별의 진화 페이지
elif st.session_state.page == "star_evolution":
    st.markdown("<h1 class='star-title'>별의 진화</h1>", unsafe_allow_html=True)
    st.markdown("<p class='star-text'>별은 가스 구름에서 탄생하여, 수소와 헬륨을 연료로 삼아 빛을 내고, </br>결국에는 백색왜성, 중성자별, 또는 블랙홀이 되는 긴 여정을 거칩니다.</p>", unsafe_allow_html=True)
    if st.button("메인으로 돌아가기"):
        st.session_state.page = "main"
