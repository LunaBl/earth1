import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# 페이지 설정
st.set_page_config(
    page_title="우주의 신비",
    layout="wide",
)

# 텍스트 그라데이션을 적용하는 헬퍼 함수
def apply_gradient_text(text, level='h1'):
    """주어진 텍스트에 파란색-보라색 그라데이션을 적용하는 함수"""
    st.markdown(f"<{level}><span>{text}</span></{level}>", unsafe_allow_html=True)

# 글자와 버튼 스타일 CSS
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

# 별 진화 단계별 정보 정의
STAR_STAGES = {
    'main_sequence': {
        'name': '주계열성 (Main Sequence)', 'desc': '수소 핵융합을 통해 안정적으로 빛을 내는 단계입니다.',
        'temp': 5778, 'luminosity': 1.0, 'size': 100
    },
    'red_giant': {
        'name': '적색 거성', 'desc': '수소를 소진하고 헬륨 핵융합을 시작하며 크게 팽창합니다.',
        'temp': 3500, 'luminosity': 100, 'size': 500
    },
    'planetary_nebula': {
        'name': '행성상 성운 및 백색 왜성', 'desc': '외피를 날려보내고 중심핵만 남은 **백색 왜성**이 됩니다.',
        'temp': 100000, 'luminosity': 0.01, 'size': 50
    },
    'red_supergiant': {
        'name': '적색 초거성', 'desc': '수소를 소진하고 크게 팽창하여 적색 초거성이 됩니다.',
        'temp': 3500, 'luminosity': 10000, 'size': 1000
    },
    'supernova': {
        'name': '초신성 폭발', 'desc': '격렬한 **초신성 폭발**을 일으키고, 질량에 따라 중성자별 또는 블랙홀이 됩니다.'
    }
}

# 페이지 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "main"
    st.session_state.star_info = STAR_STAGES['main_sequence']

# 메인 페이지
def show_main_page():
    apply_gradient_text("별의 신비", level='h1')
    st.markdown("<div>", unsafe_allow_html=True)
    if st.button("🌌 별의 진화"):
        st.session_state.page = "star_evolution"
        st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<p>🚀<span> 우주의 광활함 속에서 빛나는 별들의 이야기를 탐험해 보세요.</span></p>", unsafe_allow_html=True)

# 별 진화 시뮬레이션 페이지
def show_star_evolution_page():
    apply_gradient_text("별의 진화 시뮬레이터", level='h1')
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
    apply_gradient_text("별의 진화 과정", level='h2')

    # 질량에 따른 초기 상태 및 진화 경로 변경
    if 'star_info' not in st.session_state:
        st.session_state.star_info = STAR_STAGES['main_sequence']
        if star_mass > 8:
            st.session_state.star_info = {'name': '고질량 별', 'desc': '태양보다 훨씬 뜨겁고 밝은 고질량 별입니다.'}
        else:
            st.session_state.star_info = {'name': '저/중질량 별', 'desc': '태양처럼 수소 핵융합을 하는 안정적인 별입니다.'}

    st.info(f"**현재 단계:** {st.session_state.star_info['name']}", icon="⭐")

    if st.button("🚀 진화 시작"):
        # 확률에 따른 진화 성공/실패 결정
        if random.randint(1, 100) > evolution_success_rate:
            st.error("💥 **진화 실패!** 이 별은 불안정하여 생을 마감했습니다.", icon="❗")
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Low_to_intermediate-mass_star_evolution.svg/1280px-Low_to_intermediate-mass_star_evolution.svg.png", caption="별의 진화가 실패하면 다양한 형태로 붕괴할 수 있습니다.")
        else:
            # 질량에 따른 진화 시뮬레이션
            if star_mass <= 8:
                stage = 'red_giant'
                st.session_state.star_info = STAR_STAGES[stage]
                st.info(f"**진화 단계:** {st.session_state.star_info['name']}", icon="💥")
                
                # 적색 거성 이미지 삽입
                st.image('red-giant-star.png', caption="적색 거성으로 진화한 별의 모습")
                st.markdown(f"<p><span>{st.session_state.star_info['desc']}</span></p>", unsafe_allow_html=True)
                st.write("---")

                stage = 'planetary_nebula'
                st.session_state.star_info = STAR_STAGES[stage]
                st.info(f"**진화 단계:** {st.session_state.star_info['name']}", icon="💫")
                st.markdown(f"<p><span>{st.session_state.star_info['desc']}</span></p>", unsafe_allow_html=True)
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Low_to_intermediate-mass_star_evolution.svg/1280px-Low_to_intermediate-mass_star_evolution.svg.png", caption="저/중질량 별의 진화 과정")
                
            else:
                stage = 'red_supergiant'
                st.session_state.star_info = STAR_STAGES[stage]
                st.info(f"**진화 단계:** {st.session_state.star_info['name']}", icon="💥")

                # Matplotlib으로 별 그리기 (고질량 별은 붉은색 원으로 유지)
                fig, ax = plt.subplots(figsize=(6, 6))
                ax.set_facecolor('black')
                ax.set_aspect('equal')
                ax.add_artist(plt.Circle((0, 0), st.session_state.star_info['size']/100, color='red'))
                ax.set_xlim(-15, 15)
                ax.set_ylim(-15, 15)
                plt.axis('off')
                st.pyplot(fig)
                
                st.markdown(f"<p><span>{st.session_state.star_info['desc']}</span></p>", unsafe_allow_html=True)
                st.write("---")

                stage = 'supernova'
                st.session_state.star_info = STAR_STAGES[stage]
                st.info(f"**진화 단계:** {st.session_state.star_info['name']}", icon="🔥")
                st.markdown(f"<p><span>{st.session_state.star_info['desc']}</span></p>", unsafe_allow_html=True)
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Massive_star_evolution_kor.svg/1280px-Massive_star_evolution_kor.svg.png", caption="고질량 별의 진화 과정")
    
    st.write("---")
    
    # 별의 현재 상태 정보
    apply_gradient_text("별의 현재 정보", level='h2')
    st.write(f"**질량:** 태양의 {star_mass}배")
    st.write(f"**진화 성공 확률:** {evolution_success_rate}%")
    
    current_info = st.session_state.star_info
    if 'size' in current_info:
        st.write(f"**상대적 크기:** {current_info['size']}배")
    if 'temp' in current_info:
        st.write(f"**표면 온도:** {current_info['temp']}K")
    if 'luminosity' in current_info:
        st.write(f"**광도:** 태양의 {current_info['luminosity']}배")

    st.markdown("---")
    if st.button("메인으로 돌아가기"):
        st.session_state.page = "main"
        st.session_state.star_info = {'name': '초기 상태', 'desc': ''} # 초기 상태로 리셋
        st.experimental_rerun()

# 페이지 렌더링
if st.session_state.page == "main":
    show_main_page()
elif st.session_state.page == "star_evolution":
    show_star_evolution_page()
