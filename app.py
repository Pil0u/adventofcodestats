import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

import random
from datetime import date,datetime


st.title('Advent of Code - Stats')

@st.cache
def fetch_percentages(_cache_key):
    return [random.randrange(0,100) for _ in range(0,date.today().day)]

previous_hour = datetime.now().replace(minute=0, second=0)
percentages = fetch_percentages(int(previous_hour.timestamp()))

st.header("Data last fetched at %s\n" % previous_hour.strftime("%H:%M:%S"))

df = pd.DataFrame(
        dict([('Day %d' % i, percentage) for i, percentage in enumerate(percentages, start=1)]),
        index=[0],
    )

st.dataframe(df.style.background_gradient(cmap='RdYlGn', axis=1))
