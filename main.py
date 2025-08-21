import streamlit as st

# 페이지 함수 정의
def main_page():
    st.title("메인 페이지")
    st.write("환영합니다! 아래 버튼을 눌러 별의 진화에 대해 알아보세요.")

    if st.button("별의 진화"):
        st.session_state.page = "star_evolution"

def star_evolution_page():
    st.title("⭐ 별의 진화")
    st.write("별은 일생 동안 다양한 단계를 거치며 변화합니다. 별의 진화는 별의 질량에 따라 크게 달라집니다.")
    
    st.subheader("저질량 별의 진화")
    st.write("성운 → 주계열성 → 적색 거성 → 행성상 성운 → 백색 왜성")
    
    st.subheader("고질량 별의 진화")
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
