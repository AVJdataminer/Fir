import datetime
import streamlit as st
from streamlit import caching
import pandas as pd
import altair as alt
import os
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline


st.title('Job listing resume matcher')

DATE_COLUMN = 'created_at'
DATA_URL = ('https://raw.githubusercontent.com/AVJdataminer/Fir/master/data/simple_all_repo_issues.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

st.subheader('Number of issues per day')
cnt = pd.DataFrame(data.groupby('created_at').size().rename('DA')).reset_index()
rolling_mean = cnt.DA.rolling(window=7).mean()
rolling_mean2 = cnt.DA.rolling(window=14).mean()
plt.figure(figsize=(20,10))
plt.plot(cnt.created_at, cnt.DA, label='All Issues')
plt.plot(cnt.created_at, rolling_mean, label='Created Issues 7 Day SMA', color='orange')
plt.plot(cnt.created_at, rolling_mean2, label='Created Issues 14 Day SMA', color='magenta')
plt.legend(loc='upper left')
plt.show()
