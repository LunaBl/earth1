import streamlit as st

def set_page(page_name):
    """
    세션 상태를 업데이트하여 페이지를 전환합니다.
    """
    st.session_state.page = page_name

def main_page():
    """앱의 시작 화면을 렌더링합니다."""
    # CSS 스타일을 정의하여 그라데이션 효과를 만듭니다.
    st.markdown("""
        <style>
        .galaxy-gradient {
            background: linear-gradient(90deg, #64B5F6, #42A5F5, #2196F3, #1E88E5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3em;
            font-weight: bold;
            text-align: center;
        }
        .section-header {
            color: #FFFFFF;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)
        
    st.markdown("<h1 class='galaxy-gradient'>🌌 우주 시뮬레이터</h1>", unsafe_allow_html=True)
    st.write("환영합니다! 아래 버튼을 눌러 시뮬레이션을 시작하거나 설명을 확인하세요.")
    st.markdown("---")

    # 두 개의 컬럼으로 버튼 배치
    col1, col2 = st.columns(2)

    with col1:
        st.button(
            "🚀 중력 마이크로렌징 시뮬레이션 시작",
            key="start_simulation_button",
            on_click=set_page,
            args=('simulation',),
            use_container_width=True
        )

    with col2:
        st.button(
            "📚 시뮬레이션 설명 보기",
            key="view_explanation_button",
            on_click=set_page,
            args=('explanation',),
            use_container_width=True
        )

def explanation_page():
    """
    '시뮬레이션 설명 보기' 버튼을 눌렀을 때 나타나는 페이지입니다.
    """
    st.markdown("""
        <style>
        .galaxy-gradient {
            background: linear-gradient(90deg, #64B5F6, #42A5F5, #2196F3, #1E88E5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3em;
            font-weight: bold;
            text-align: center;
        }
        .section-header {
            color: #FFFFFF;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<h1 class='galaxy-gradient'>📚 시뮬레이션 설명</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-header'>중력 마이크로렌징이란?</h2>", unsafe_allow_html=True)
    st.write("중력 마이크로렌징은 먼 별빛이 그 앞을 지나가는 천체(렌즈 역할을 하는 별)의 중력에 의해 휘어지면서 밝기가 일시적으로 증가하는 현상입니다. 이 현상은 행성이나 어두운 천체(예: 블랙홀, 중성자별)를 탐지하는 데 사용됩니다.")
    st.write("이 시뮬레이션에서는 렌즈 별의 질량과 배경 별의 위치 변화에 따라 밝기 곡선이 어떻게 달라지는지 관찰할 수 있습니다.")
    
    st.markdown("---")
    
    if st.button("⬅️ 뒤로 가기"):
        set_page('main')

def simulation_page():
    """
    '시뮬레이션 시작' 버튼을 눌렀을 때 나타나는 페이지입니다.
    이곳에 시뮬레이션 코드를 추가하면 됩니다.
    """
    st.markdown("""
        <style>
        .galaxy-gradient {
            background: linear-gradient(90deg, #64B5F6, #42A5F5, #2196F3, #1E88E5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3em;
            font-weight: bold;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)
        
    st.markdown("<h1 class='galaxy-gradient'>🚀 시뮬레이션</h1>", unsafe_allow_html=True)
    st.write("시뮬레이션 페이지입니다. 여기에 시뮬레이션 관련 콘텐츠를 넣어주세요.")
    
    st.markdown("---")
    
    if st.button("⬅️ 뒤로 가기"):
        set_page('main')


# 페이지 라우팅 로직
if "page" not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "explanation":
    explanation_page()
elif st.session_state.page == "simulation":
    simulation_page()
