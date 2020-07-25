#streamlit run https://raw.githubusercontent.com/AVJdataminer/Fir/master/job.py
        
import streamlit as st
import pandas as pd
import numpy as np

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

if st.checkbox('Show job listings data'):
    st.subheader('Job Listings')
    st.write(data)
        
from PIL import Image
from PIL import Image
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/AVJdataminer/HireOne/master/data/Binoy_Dutt_Resume.jpg'
image = Image.open(urlopen(url))

st.image(image, caption='Sunrise by the mountains',use_column_width=True)
