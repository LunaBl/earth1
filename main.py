import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# 페이지 설정
st.set_page_config(
    page_title="우주의 신비",
    layout="wide",
)

# 글자와 버튼 스타일만 적용하는 CSS
custom_css = """
<style>
/* 글자 부분에만 그라데이션 적용 */
.stMarkdown h1 span, .stMarkdown p span, .stMarkdown h2 span, .stMarkdown h3 span {
    background: linear-gradient(45deg, #00BFFF, #6A5ACD, #8A2BE2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 10px rgba(135, 206, 250, 0.5);
}

/* 이모티콘은 그라데이션 적용하지 않음 (부모 태그의 기본 스타일) */
.stMarkdown h1, .stMarkdown p, .stMarkdown h2, .stMarkdown h3 {
    -webkit-text-fill-color: initial;
    background: none;
    text-shadow: none;
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
    st.markdown("<h1>💫<span> 별의 진화 시뮬레이터</span></h1>", unsafe_allow_html=True)
    st.markdown("<p>🔭<span> 별의 질량과 진화 성공 확률을 조절하고, '진화 시작' 버튼을 눌러 그 운명을 확인해 보세요.</span></p>", unsafe_allow_html=True)

    # --- 별의 속성 조절 ---
    st.sidebar.markdown("<h2>⭐<span> 별의 속성</span></h2>", unsafe_allow_html=True)
    star_mass = st.sidebar.slider(
        "별의 질량 (태양 질량 단위)", 
        min_value=0.5, 
        max_value=30.0, 
        value=1.0, 
        step=0.1
    )
    
    evolution_success_rate = st.sidebar.slider(
        "진화 성공 확률 (%)", 
        min_value=0, 
        max_value=100, 
        value=100, 
        step=1
    )

    # --- 시뮬레이션 ---
    st.markdown("<h2>🌠<span> 별의 진화 과정</span></h2>", unsafe_allow_html=True)

    # 별의 상태를 저장할 딕셔너리
    star_state = {
        'size': 100,
        'color': '#FFFF00',
        'phase': '주계열성 (Main Sequence)',
        'temp': 5778,
        'luminosity': 1.0,
        'desc': '수소 핵융합을 통해 안정적으로 빛을 내는 단계입니다.'
    }

    # 질량에 따라 별의 초기 상태 및 진화 경로 변경
    if star_mass > 8:
        star_state['phase'] = '고질량 별'
        star_state['temp'] = 20000
        star_state['luminosity'] = 1000
        star_state['desc'] = '태양보다 훨씬 뜨겁고 밝은 고질량 별입니다.'
    else:
        star_state['phase'] = '저/중질량 별'
        star_state['temp'] = 5778
        star_state['luminosity'] = 1.0
        star_state['desc'] = '태양처럼 수소 핵융합을 하는 안정적인 별입니다.'
        
    st.info(f"**현재 단계:** {star_state['phase']}", icon="⭐")

    # --- 애니메이션 및 결과 표시 ---
    if st.button("🚀 진화 시작"):
        # 확률에 따른 진화 성공/실패 결정
        if random.randint(1, 100) > evolution_success_rate:
            st.error("💥 **진화 실패!** 이 별은 불안정하여 생을 마감했습니다.", icon="❗")
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Low_to_intermediate-mass_star_evolution.svg/1280px-Low_to_intermediate-mass_star_evolution.svg.png", caption="별의 진화가 실패하면 다양한 형태로 붕괴할 수 있습니다.")
        else:
            # 질량에 따른 진화 시뮬레이션
            if star_mass <= 8:
                star_state['phase'] = '적색 거성'
                star_state['temp'] = 3500
                star_state['size'] = 500
                star_state['luminosity'] = 100
                star_state['desc'] = '수소를 소진하고 헬륨 핵융합을 시작하며 크게 팽창합니다.'
                st.info(f"**진화 단계:** {star_state['phase']}", icon="💥")
                
                # ➡️➡️➡️ 여기에 정확한 파일 이름과 확장자를 넣어주세요!
                st.image('red-giant-star.png', caption="적색 거성으로 진화한 별의 모습")
                st.markdown(f"<p><span>{star_state['desc']}</span></p>", unsafe_allow_html=True)
                st.write("---")

                star_state['phase'] = '행성상 성운 및 백색 왜성'
                star_state['temp'] = 100000
                star_state['size'] = 50
                star_state['luminosity'] = 0.01
                st.info(f"**진화 단계:** {star_state['phase']}", icon="💫")
                st.markdown(f"<p><span>외피를 날려보내고 중심핵만 남은 **백색 왜성**이 됩니다.</span></p>", unsafe_allow_html=True)
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Low_to_intermediate-mass_star_evolution.svg/1280px-Low_to_intermediate-mass_star_evolution.svg.png", caption="저/중질량 별의 진화 과정")
                
            else:
                star_state['phase'] = '적색 초거성'
                star_state['temp'] = 3500
                star_state['size'] = 1000
                star_state['luminosity'] = 10000
                star_state['desc'] = '수소를 소진하고 크게 팽창하여 적색 초거성이 됩니다.'
                st.info(f"**진화 단계:** {star_state['phase']}", icon="💥")

                # Matplotlib으로 별 그리기 (고질량 별은 붉은색 원으로 유지)
                fig, ax = plt.subplots(figsize=(6, 6))
                ax.set_facecolor('black')
                ax.set_aspect('equal')
                ax.add_artist(plt.Circle((0, 0), star_state['size']/100, color='red')) # 붉은색 원으로 수정
                ax.set_xlim(-15, 15)
                ax.set_ylim(-15, 15)
                plt.axis('off')
                st.pyplot(fig)
                
                st.markdown(f"<p><span>{star_state['desc']}</span></p>", unsafe_allow_html=True)
                st.write("---")

                star_state['phase'] = '초신성 폭발'
                st.info(f"**진화 단계:** {star_state['phase']}", icon="🔥")
                st.markdown(f"<p><span>격렬한 **초신성 폭발**을 일으키고, 질량에 따라 중성자별 또는 블랙홀이 됩니다.</span></p>", unsafe_allow_html=True)
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Massive_star_evolution_kor.svg/1280px-Massive_star_evolution_kor.svg.png", caption="고질량 별의 진화 과정")
    
    st.write("---")
    
    # 별의 현재 상태 정보
    st.markdown("<h2>ℹ️<span> 별의 현재 정보</span></h2>", unsafe_allow_html=True)
    st.write(f"**질량:** 태양의 {star_mass}배")
    st.write(f"**진화 성공 확률:** {evolution_success_rate}%")
    st.write(f"**상대적 크기:** {star_state['size']}배")
    st.write(f"**표면 온도:** {star_state['temp']}K")
    st.write(f"**광도:** 태양의 {star_state['luminosity']}배")

    st.markdown("---")
    if st.button("메인으로 돌아가기"):
        st.session_state.page = "main"
