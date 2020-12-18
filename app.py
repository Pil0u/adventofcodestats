import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

st.title('Advent of Code - Stats')

percentages = [90,35,70,10,100]

df = pd.DataFrame(
        dict([('Day %d' % i, percentage) for i, percentage in enumerate(percentages, start=1)]),
        index=[0],
    )

st.table(df.style.background_gradient(cmap='RdYlGn', axis=1))
