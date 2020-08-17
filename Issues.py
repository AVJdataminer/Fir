import streamlit as st
import pandas as pd
import numpy as np
import re
import string
from collections import Counter
from gensim.summarization import keywords
import matplotlib.pyplot as plt

st.title('Job listing resume matcher')

#DATE_COLUMN = 'date/time'
DATA_URL = ('https://raw.githubusercontent.com/AVJdataminer/HireOne/master/data/job_descriptions.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")
