import streamlit as st
import pandas as pd
import numpy as np
import re
import string
import matplotlib.pyplot as plt
import altair as alt

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
hist_values = np.histogram(data[DATE_COLUMN].dt.day, bins=7, range=(0,7))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('day', 0, 7, 1)
filtered_data = data[data[DATE_COLUMN].dt.day == hour_to_filter]
