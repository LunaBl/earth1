import streamlit as st

# 페이지 함수 정의
def main_page():
    # CSS 스타일을 정의하여 그라데이션 효과를 만듭니다.
    # 은하수 느낌을 위해 여러 푸른색을 조합합니다.
    st.markdown("""
        <style>
        .galaxy-gradient {
            background: linear-gradient(90deg, #1A237E, #283593, #00BCD4, #00A9E0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3em;
            font-weight: bold;
            text-align: center;
        }
        .galaxy-sub-gradient {
            background: linear-gradient(90deg, #64B5F6, #42A5F5, #2196F3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2em;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='galaxy-gradient'>메인 페이지</h1>", unsafe_allow_html=True)
    st.write("🌌 환영합니다! 아래 버튼을 눌러 별의 진화에 대해 알아보세요.")

    if st.button("별의 진화"):
        st.session_state.page = "star_evolution"

def star_evolution_page():
    # 페이지 전환 후에도 스타일이 유지되도록 다시 마크다운을 호출합니다.
    st.markdown("""
        <style>
        .galaxy-gradient {
            background: linear-gradient(90deg, #1A237E, #283593, #00BCD4, #00A9E0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3em;
            font-weight: bold;
            text-align: center;
        }
        .galaxy-sub-gradient {
            background: linear-gradient(90deg, #64B5F6, #42A5F5, #2196F3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2em;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)
        
    st.markdown("<h1 class='galaxy-gradient'>⭐ 별의 진화</h1>", unsafe_allow_html=True)
    st.write("별은 일생 동안 다양한 단계를 거치며 변화합니다. 별의 진화는 별의 질량에 따라 크게 달라집니다.")
    
    st.markdown("<h2 class='galaxy-sub-gradient'>저질량 별의 진화</h2>", unsafe_allow_html=True)
    st.write("성운 → 주계열성 → 적색 거성 → 행성상 성운 → 백색 왜성")
    
    st.markdown("<h2 class='galaxy-sub-gradient'>고질량 별의 진화</h2>", unsafe_allow_html=True)
    st.write("성운 → 주계열성 → 초거성 → 초신성 폭발 → 중성자별 또는 블랙홀")
    
    if st.button("뒤로가기"):
        st.session_state.page = "main"

# 페이지 라우팅 로직
if "page" not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "star_evolution":
    star_evolution_page()
