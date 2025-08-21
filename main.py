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

body {
    font-family: 'Poppins', sans-serif;
    color: #00BFFF;
    background: #000;
}

/* 제목 스타일 */
.main-title, .star-title {
    font-size: 4rem;
    font-weight: 600;
    text-align: center;
    background: linear-gradient(90deg, #00BFFF, #1E90FF, #00BFFF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding-top: 50px;
    z-index: 2;
    position: relative;
}

/* 텍스트 스타일 */
.intro-text, .star-text {
    font-size: 1.2rem;
    text-align: center;
    color: #ADD8E6;
    margin-top: 20px;
    line-height: 1.6;
    z-index: 2;
    position: relative;
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
    margin: 20px auto;
    display: block;
    z-index: 2;
    position: relative;
}

.stButton>button:hover {
    background-color: #00BFFF !important;
    color: #000 !important;
    box-shadow: 0 0 20px #00BFFF;
    transform: scale(1.05);
}

.stMarkdown {
    z-index: 2;
    position: relative;
}

.button-container {
    display: flex;
    justify-content: center;
    margin-top: 40px;
    z-index: 2;
    position: relative;
}
</style>
"""

# 커스텀 CSS 적용
st.markdown(custom_css, unsafe_allow_html=True)

# 페이지 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "main"

# 배경 이미지
# st.image를 사용하여 이미지 표시 (상대 경로로 이미지 파일을 지정)
st.image("background.jpg", use_column_width=True)

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
