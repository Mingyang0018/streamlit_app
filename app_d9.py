# 显示折线图line_chart

import streamlit as st
import pandas as pd
import numpy as np

# 显示标题
st.header('line chart')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
# 显示折线图
st.line_chart(chart_data)