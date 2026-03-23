import streamlit as st

# 폰트 적용
st.markdown("""
<style>
@font-face {
    font-family: 'NanumGothic';
    src: url('../fonts/NanumGothic-Regular.ttf') format('truetype');
}
body {
    font-family: 'NanumGothic', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.title("자기소개")

st.header("이름")
st.write("여기에 이름을 입력하세요.")

st.header("소개")
st.write("여기에 간단한 소개를 입력하세요.")

st.header("경력")
st.write("여기에 경력을 입력하세요.")

st.header("관심사")
st.write("여기에 관심사를 입력하세요.")