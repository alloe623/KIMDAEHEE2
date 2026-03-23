import streamlit as st
import pandas as pd

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

st.title("데이터 시각화")

st.write("간단한 데이터를 다양한 차트로 시각화합니다.")

# 데이터 1: 산점도
st.header("산점도")
data1 = {
    'x': [1, 2, 3, 4],
    'y': [10, 20, 30, 40],
    'label': ['A', 'B', 'C', 'D']
}
df1 = pd.DataFrame(data1)
st.scatter_chart(df1, x='x', y='y', color='label')

# 데이터 2: 막대 그래프
st.header("막대 그래프")
data2 = {
    'category': ['사과', '바나나', '체리', '대추'],
    'value': [23, 45, 56, 78]
}
df2 = pd.DataFrame(data2)
st.bar_chart(df2, x='category', y='value')

# 데이터 3: 선 그래프
st.header("선 그래프")
data3 = {
    'time': [1, 2, 3, 4, 5],
    'value': [10, 15, 25, 30, 50]
}
df3 = pd.DataFrame(data3)
st.line_chart(df3, x='time', y='value')

# 데이터 4: 영역 그래프
st.header("영역 그래프")
data4 = {
    'x': [1, 2, 3, 4, 5],
    'y1': [10, 20, 30, 20, 10],
    'y2': [5, 15, 25, 35, 45]
}
df4 = pd.DataFrame(data4)
st.area_chart(df4, x='x', y=['y1', 'y2'])