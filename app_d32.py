# 显示上传文件组件
import os
os.system('pip3 install streamlit-file-uploader')
os.system('pip3 install ydata_profiling')

import streamlit as st
import pandas as pd
import ydata_profiling
from streamlit_ydata_profiling import st_profile_report

# 设置页面布局
st.set_page_config(layout="wide")

# 设置标题
st.title('生成数据分析报告')
# 设置上传文件组件
st.subheader('上传CSV')
uploaded_file = st.file_uploader('')

# 根据是否选择了文件显示消息
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('数据表')
    st.write(df)
    report = ydata_profiling.ProfileReport(df, title='Profile Report', explorative=True)
    st.subheader('数据分析报告')
    # st.write(report)
    st_profile_report(report, navbar=True)
else:
    st.write('No file uploaded.')
    st.info('Upload a csv file.')
