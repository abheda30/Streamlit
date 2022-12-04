import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os
import warnings

st.set_option('deprecation.showPyplotGlobalUse', False)

#from google.colab import drive
#drive.mount('/content/gdrive')

# Commented out IPython magic to ensure Python compatibility.
# %cd '/content/gdrive/MyDrive/'

st.set_page_config(page_title="Churn Dashboard",page_icon=":pie_chart:")

df = pd.read_csv('ChurnDataset.csv')
df.head()

df.head()

df.info()

df.isnull().sum()



df= df.drop(['customerID'], axis=1)

list = ['Churn','Senior Citizen','Dependents', 'Partner','Payment Method']

pageview = st.sidebar.radio('Select the page you want to view', list)

if pageview == 'Churn':
    st.subheader("Overall Churn")
    j = sns.countplot(x="Churn", data=df, palette="Accent_r")
    for p in j.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height()/len(df))
        x = p.get_x() + p.get_width()
        y = p.get_height()
        j.annotate(percentage, (x, y),ha='right')
    j.figure

if pageview == 'Partner':
  st.subheader("Churn for Partner")
  j = sns.countplot(x="Partner", data=df, palette="autumn_r")
  for p in j.patches:

    percentage = '{:.1f}%'.format(100 * p.get_height()/len(df))
    x = p.get_x() + p.get_width()
    y = p.get_height()
    j.annotate(percentage, (x, y),ha='right')
  j.figure



if pageview == 'Dependents':
    st.subheader("Churn for Dependents")
    j = sns.countplot(x="Dependents", data=df, palette="afmhot_r")
    for p in j.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height()/len(df))
        x = p.get_x() + p.get_width()
        y = p.get_height()
        j.annotate(percentage, (x, y),ha='right')
    j.figure

import matplotlib.ticker as mtick

if pageview == 'Senior Citizen':
    st.subheader("Churn for Senior Citizen")
    j = (df['SeniorCitizen'].value_counts()*100.0 /len(df)).plot.pie(autopct='%.1f%%', labels = ['No', 'Yes'],figsize =(5,5),colors=['royalblue','lightskyblue'], fontsize = 12 ) 
    if pageview == 'Senior Citizen':  
        j.set_title('percentage of Senior Citizens', fontsize = 12)
    j.figure

if pageview == 'Payment Method':
    st.subheader("Churn for Payment Method") 
    j = sns.countplot(x="PaymentMethod", data=df, palette="cubehelix")
    j.set_xticklabels(j.get_xticklabels(), rotation=45)

    for p in j.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height()/len(df))
        x = p.get_x() + p.get_width()
        y = p.get_height()
        j.annotate(percentage, (x, y),ha='right') 
    j.figure
