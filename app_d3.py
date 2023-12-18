import streamlit as st

# 显示标题
st.header('st.button')

# 设置按钮
if st.button('say hello'):
    st.write('why hello there')

else:
    st.write('hello')