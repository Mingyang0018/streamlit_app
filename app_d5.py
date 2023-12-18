import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# 显示Markdown文本
st.write('Hello, *world!* :sunglasses:')

# 显示数字
st.write(12345)

# 显示数据框dataframe
df = pd.DataFrame(np.ones((3, 3)), columns=['a', 'b', 'c'])
# st.write(df)
st.write('bellow is a dataframe:', df, 'above is a dataframe.')

# 显示图表
df02 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df02).mark_circle().encode(
    x='a',
    y='b',
    size='c',
    color='c',
    tooltip=['a', 'b', 'c']
)

# st.write(c)
st.write('bellow is a chart:', c, 'above is a chart.')