import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# sample 1
# 滑条
st.subheader('slider')

age = st.slider('how old are you?', 0, 135, 25)
st.write('you are', age, 'years old')

# sample 2
# 范围滑条
st.subheader('range slider')

values = st.slider('select a range', 0.0, 100.0, (25.0, 75.0))
st.write('values: ', values)

# sample 3
# 范围时间滑条
st.subheader('range time slider')
appointment = st.slider('schedule your appointment:',
                        value=(time(12, 00), time(13, 00)))

st.write('you have appointment at: ', appointment)

# sample 4
# 时间滑条
st.subheader('datetime slider')

start_time = st.slider(
    'when do you start?',
    value=datetime(2021, 1, 1, 11, 00),
    format='MM/DD/YY - hh:mm'
)

st.write('start time: ', start_time)
