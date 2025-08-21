import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="우주의 신비",
    layout="wide",
)

# 글자 스타일만 적용하는 CSS
custom_css = """
<style>
/* 모든 글자에 밝은 파랑 그라데이션 적용 */
.stMarkdown h1, .stMarkdown p {
    background: linear-gradient(to right, #00BFFF, #87CEFA, #4682B4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 15px rgba(135, 206, 250, 0.7); /* 글자 그림자 추가 */
}

/* 버튼 스타일은 기본값으로 유지 */
.stButton>button {
    text-shadow: none;
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
    st.markdown("<h1>✨ 별의 신비</h1>", unsafe_allow_html=True)
    st.markdown("<div>", unsafe_allow_html=True)
    if st.button("🌌 별의 진화"):
        st.session_state.page = "star_evolution"
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<p>🚀 우주의 광활함 속에서 빛나는 별들의 이야기를 탐험해 보세요.</p>", unsafe_allow_html=True)

# 별의 진화 페이지
elif st.session_state.page == "star_evolution":
    st.markdown("<h1>💫 별의 진화</h1>", unsafe_allow_html=True)
    st.markdown("<p>🔭 별은 가스 구름에서 탄생하여, 수소와 헬륨을 연료로 삼아 빛을 내고, </br>결국에는 백색왜성, 중성자별, 또는 블랙홀이 되는 긴 여정을 거칩니다.</p>", unsafe_allow_html=True)
    if st.button("메인으로 돌아가기"):
        st.session_state.page = "main"
