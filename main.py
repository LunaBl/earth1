import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="우주의 신비",
    layout="wide",
)

# 글자와 버튼 스타일만 적용하는 CSS
custom_css = """
<style>
/* 모든 글자에 파랑-보라 그라데이션 적용 */
.stMarkdown h1 span, .stMarkdown p span {
    background: linear-gradient(45deg, #00BFFF, #6A5ACD, #8A2BE2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 10px rgba(135, 206, 250, 0.5);
}

/* 이모티콘에는 그라데이션 적용하지 않음 */
.stMarkdown h1, .stMarkdown p {
    -webkit-text-fill-color: initial;
    background: none;
    text-shadow: none;
}
.stMarkdown h1::before, .stMarkdown p::before {
    -webkit-text-fill-color: initial;
}

/* 버튼 스타일을 수정하여 더 잘 보이게 만듭니다 */
.stButton > button {
    background-color: #1A2A4A; /* 어두운 파란색 배경 */
    color: #E0FFFF !important; /* 글자색을 밝은 색으로 변경 */
    border: 2px solid #4682B4; /* 테두리 색상 */
    font-weight: bold;
    font-size: 1.2em;
    padding: 10px 25px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(70, 130, 180, 0.5); /* 은은한 그림자 */
    transition: all 0.3s ease;
    text-shadow: none;
}

/* 버튼에 마우스를 올렸을 때의 효과 */
.stButton > button:hover {
    background-color: #2A3A5A; /* 배경색을 더 진하게 */
    border-color: #87CEEB; /* 테두리색을 더 밝게 */
    box-shadow: 0 0 20px rgba(135, 206, 235, 0.8), 0 0 30px rgba(135, 206, 235, 0.5); /* 더 강한 빛 효과 */
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
    st.markdown("<h1>✨<span> 별의 신비</span></h1>", unsafe_allow_html=True)
    st.markdown("<div>", unsafe_allow_html=True)
    if st.button("🌌 별의 진화"):
        st.session_state.page = "star_evolution"
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<p>🚀<span> 우주의 광활함 속에서 빛나는 별들의 이야기를 탐험해 보세요.</span></p>", unsafe_allow_html=True)

# 별의 진화 페이지
elif st.session_state.page == "star_evolution":
    st.markdown("<h1>💫<span> 별의 진화 시뮬레이션</span></h1>", unsafe_allow_html=True)
    st.markdown("<p>🔭<span> 아래 슬라이더를 조절하여 별의 진화 과정이 어떻게 달라지는지 확인해 보세요.</span></p>", unsafe_allow_html=True)

    # --- 별의 속성 조절 버튼 (슬라이더) ---
    st.sidebar.title("⭐ 별의 속성")
    star_mass = st.sidebar.slider(
        "별의 질량 (태양 질량 단위)", 
        min_value=0.1, 
        max_value=20.0, 
        value=1.0, 
        step=0.1
    )
    star_temp = st.sidebar.slider(
        "표면 온도 (켈빈)", 
        min_value=2000, 
        max_value=50000, 
        value=5778, 
        step=1000
    )
    star_gravity = st.sidebar.slider(
        "중력 (g 단위)", 
        min_value=0.1, 
        max_value=1000.0, 
        value=1.0, 
        step=0.1
    )
    st.sidebar.markdown("---")

    # --- 애니메이션 및 결과 표시 ---
    st.subheader("🌠<span> 별의 진화 과정</span>")

    # 별의 질량에 따라 진화 경로를 결정
    if star_mass <= 8:
        st.markdown(f"<p><span>선택된 별의 질량은 태양의 {star_mass}배입니다. 이 별은 **저/중질량 별**의 진화 과정을 거칩니다.</span></p>", unsafe_allow_html=True)
        st.write("진화 단계: 성운 → 주계열성 → 적색 거성 → 행성상 성운 → 백색 왜성")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Low_to_intermediate-mass_star_evolution.svg/1280px-Low_to_intermediate-mass_star_evolution.svg.png", caption="저/중질량 별의 진화 과정")
    else:
        st.markdown(f"<p><span>선택된 별의 질량은 태양의 {star_mass}배입니다. 이 별은 **고질량 별**의 진화 과정을 거칩니다.</span></p>", unsafe_allow_html=True)
        st.write("진화 단계: 성운 → 주계열성 → 적색 초거성 → 초신성 폭발 → 중성자별 또는 블랙홀")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Massive_star_evolution_kor.svg/1280px-Massive_star_evolution_kor.svg.png", caption="고질량 별의 진화 과정")

    # 별의 속성에 따른 설명 추가
    st.subheader("ℹ️<span> 별의 현재 속성</span>")
    st.write(f"**질량:** 태양의 {star_mass}배")
    st.write(f"**온도:** {star_temp}K")
    st.write(f"**중력:** {star_gravity}g")

    st.markdown("---")

    if st.button("메인으로 돌아가기"):
        st.session_state.page = "main"
