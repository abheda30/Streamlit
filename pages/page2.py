import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

# loading Dataset 
df1 = pd.read_csv('ChurnDataset.csv')
st.title("Analysis of Telecommunications Services Data")

st.markdown("Contract Dashboard")
