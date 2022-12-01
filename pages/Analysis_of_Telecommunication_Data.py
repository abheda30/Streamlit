import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

# loading Dataset 
df = pd.read_csv('ChurnDataset.csv')
st.title("Analysis of Telecommunication Data")

list = ['Dataset','Prevailing Customers Statistics','Left Customers Statistics','Total Customers Statistics', 'Gender Statistics']

pageview = st.sidebar.radio('Select the page you want to view', list)

if pageview == 'Dataset':
    st.write(df)
    
if pageview == 'Prevailing Customers Statistics':
    st.subheader("Churn Value = No.of Customers within the Company ")
    df['Churn'].replace(['Yes', 'No'],
                        [0, 1], inplace=True)
    f1 = st.radio("Select one among these:", ['gender','InternetService', 'Contract'])
    f2 = st.selectbox("Selected Column:", ['Churn'])
    
    if f1 == 'gender':
        dfe = df.groupby([f1]).sum()
        dfe = dfe.sort_values(by=[f1],ascending=False)
        dfe = dfe.reset_index()
        fige = px.bar(dfe, x=f1, y=f2, color=f1, title="Bar chart of "+f1+" and "+f2)
        st.plotly_chart(fige)
    
    if f1 == 'InternetService':
        dfe = df.groupby([f1]).sum()
        dfe=dfe.sort_values(by=[f1],ascending=False)
        dfe = dfe.reset_index()
        fige = px.bar(dfe, x=f1, y=f2, color=f1, title="Bar chart of "+f1+" and "+f2)
        st.plotly_chart(fige)
     
    if f1 == 'Contract':
        dfe = df.groupby([f1]).sum()
        dfe = dfe.sort_values(by=[f1],ascending=False)
        dfe = dfe.reset_index()
        fige = px.bar(dfe, x=f1, y=f2, color=f1,title="Bar chart of "+f1+" and "+f2)
        st.plotly_chart(fige)


if pageview == 'Total Customers Statistics':
    st.subheader("Churn Value = Total no.of Customers ")
    f1 = st.radio("Select one among these:", ['gender','InternetService', 'Contract'])
    f2 = st.selectbox("Selected Column:", ['Churn'])
    
    if f1 == 'gender':
        dfe = df.groupby([f1]).count()
        dfe = dfe.sort_values(by=[f1],ascending=False)
        dfe = dfe.reset_index()
        fige = px.bar(dfe, x=f1, y=f2, color=f1, title="Bar chart of "+f1+" and "+f2)
        st.plotly_chart(fige)
    
    if f1 == 'InternetService':
        dfe = df.groupby([f1]).count()
        dfe = dfe.sort_values(by=[f1],ascending=False)
        dfe = dfe.reset_index()
        fige = px.bar(dfe, x=f1, y=f2, color=f1, title="Bar chart of "+f1+" and "+f2)
        st.plotly_chart(fige)
     
    if f1 == 'Contract':
        dfe = df.groupby([f1]).count()
        dfe = dfe.sort_values(by=[f1],ascending=False)
        dfe = dfe.reset_index()
        fige = px.bar(dfe, x=f1, y=f2, color=f1,title="Bar chart of "+f1+" and "+f2)
        st.plotly_chart(fige)

df['Partner'].replace(['No', 'Yes'],
                        [0, 1], inplace=True)
df['Dependents'].replace(['No', 'Yes'],
                        [0, 1], inplace=True)

if pageview == 'Gender Statistics':
    st.subheader("Total no.of Partners, Dependents and Senior Citizens w.r.t Gender")
    f1 = st.radio("Selected Column:", ['gender'])
    f2 = st.selectbox("Select a feature on which you want to evaluate the statistics:", ['Partner','Dependents', 'SeniorCitizen'])
    
    if f1 == 'gender':
        dfe = df.groupby([f1]).sum()
        dfe = dfe.sort_values(by=[f1],ascending=False)
        dfe = dfe.reset_index()
        fige = px.bar(dfe, x=f1, y=f2, color=f1, title="Bar chart of "+f1+" and "+f2)
        st.plotly_chart(fige)

if pageview == 'Left Customers Statistics':
    st.subheader("Churn Value = No.of Customers left the Company ")
    df['Churn'].replace(['No', 'Yes'],
                        [0, 1], inplace=True)
    f1 = st.radio("Select one among these:", ['gender','InternetService', 'Contract'])
    f2 = st.selectbox("Selected Column:", ['Churn'])
    
    if f1 == 'gender':
        dfe = df.groupby([f1]).sum()
        dfe = dfe.sort_values(by=[f1],ascending=False)
        dfe = dfe.reset_index()
        fige = px.bar(dfe, x=f1, y=f2, color=f1, title="Bar chart of "+f1+" and "+f2)
        st.plotly_chart(fige)
    
    if f1 == 'InternetService':
        dfe = df.groupby([f1]).sum()
        dfe=dfe.sort_values(by=[f1],ascending=False)
        dfe = dfe.reset_index()
        fige = px.bar(dfe, x=f1, y=f2, color=f1, title="Bar chart of "+f1+" and "+f2)
        st.plotly_chart(fige)
     
    if f1 == 'Contract':
        dfe = df.groupby([f1]).sum()
        dfe = dfe.sort_values(by=[f1],ascending=False)
        dfe = dfe.reset_index()
        fige = px.bar(dfe, x=f1, y=f2, color=f1,title="Bar chart of "+f1+" and "+f2)
        st.plotly_chart(fige)