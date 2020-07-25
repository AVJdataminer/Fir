#streamlit run https://raw.githubusercontent.com/AVJdataminer/Fir/master/job.py
        
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

if st.checkbox('Show job listings data'):
    st.subheader('Job Listings')
    st.write(data)
        
from PIL import Image
from PIL import Image
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/AVJdataminer/HireOne/master/data/Binoy_Dutt_Resume.jpg'
image = Image.open(urlopen(url))
st.image(image, caption='Sunrise by the mountains',use_column_width=True)

"""##Step 3. Matching job listings to resumes with cosine similarity"""
df = pd.read_csv('https://raw.githubusercontent.com/AVJdataminer/HireOne/master/data/job_descriptions.csv', encoding = 'unicode_escape')
def clean_text(text):
    text = text.replace('\n', ' ')                # remove newline
    text = text.replace(':', ' ')
    return text
df['description'] = df.apply(lambda x: clean_text(x['jobOrResumeDescription']), axis=1)
jd = df['description'].tolist()
"""Build model to tag each job description as a seperate document."""

import gensim
import gensim.downloader as api
from gensim import models
# Create the tagged document needed for Doc2Vec
def create_tagged_document(list_of_list_of_words):
    for i, list_of_words in enumerate(list_of_list_of_words):
        yield gensim.models.doc2vec.TaggedDocument(list_of_words, [i])

train_data = list(create_tagged_document(jd))
"""Train the model on the job descriptions for matching later."""

# Init the Doc2Vec model
model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=40)

# Build the Volabulary
model.build_vocab(train_data)

# Train the Doc2Vec model
model.train(train_data, total_examples=model.corpus_count, epochs=model.epochs)
"""Let's look at an example of how it converts a list of words to a vector."""

example_str = str(model.infer_vector(['data', 'science','python']))
st.write("Here's an example of the vectors generated from the list ['data', 'science','python']:")
st.write(example_str)
