import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import os
import matplotlib.ticker as mtick

#Loading dataset:
data = pd.read_csv('ChurnDataset.csv')
# st.title("Customer Churn Prediction ")

list = ['Payment method','Tenure','Tenure for each contract', 'Contract']
pageview = st.sidebar.radio('Select the page you want to view', list)

#Prepare the data:
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'],errors='coerce')
nan_cols = [i for i in data.columns if data[i].isnull().any()]
data.dropna(subset = ["TotalCharges"], inplace=True)
duplicateRows = data[data.duplicated()]
data = data.drop(['customerID'], axis=1) 

def cat_unique_col_values(data):
    for column in data:
        if data[column].dtypes=='object':
            print(f'{column}: {data[column].unique()}') 
data.replace('No internet service','No',inplace=True)
data.replace('No phone service','No',inplace=True)
# ax = sns.countplot(x="Churn", data=data, palette="Blues")

if pageview == 'Payment method':
    st.subheader("Payment method")
    ax = sns.countplot(x="PaymentMethod", data=data, palette="Blues")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    for p in ax.patches:
      percentage = '{:.1f}%'.format(100 * p.get_height()/len(data))
      x = p.get_x() + p.get_width()
      y = p.get_height()
      ax.annotate(percentage, (x, y),ha='right') 
    ax.figure


if pageview == 'Tenure':
    st.subheader("Tenure")
    import warnings
    warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 
    ax = sns.distplot(data['tenure'], hist=True, kde=False, bins=int(180/5), color = 'royalblue', hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
    ax.set_ylabel('no of Customers')
    ax.set_xlabel('Tenure (months)')
    ax.set_title('no of Customers by their tenure')
    ax.figure
    st.write('Tenure is the number of months the customer has stayed with the company.')

if pageview == 'contract':
    st.subheader("contract")
    fig, (ax1,ax2,ax3) = plt.subplots(nrows=1, ncols=3, sharey = True, figsize = (20,6))

    ax = sns.distplot(data[data['Contract']=='Month-to-month']['tenure'],
                       hist=True, kde=False,
                       bins=int(180/5), color = 'royalblue',
                       hist_kws={'edgecolor':'black'},
                       kde_kws={'linewidth': 4},
                     ax=ax1,)
    ax.set_ylabel('no of Customers')
    ax.set_xlabel('Tenure (months)')
    ax.set_title('Month to Month Contract')

    ax = sns.distplot(data[data['Contract']=='One year']['tenure'],
                       hist=True, kde=False,
                       bins=int(180/5), color = 'steelblue',
                       hist_kws={'edgecolor':'black'},
                       kde_kws={'linewidth': 4},
                     ax=ax2)
    ax.set_xlabel('Tenure (months)',size = 14)
    ax.set_title('One Year Contract',size = 14)

    ax = sns.distplot(data[data['Contract']=='Two year']['tenure'],
                       hist=True, kde=False,
                       bins=int(180/5), color = 'darkblue',
                       hist_kws={'edgecolor':'black'},
                       kde_kws={'linewidth': 4},
                     ax=ax3)

    ax.set_xlabel('Tenure (months)')
    ax.set_title('Two Year Contract')
    ax.figure
    
if pageview == 'Tenure for each contract':
    st.subheader("Tenure for each contract")
    #we can clearly see that month to month contract customers have low tenure and two year contract customrs have high tenure of around 70 months. So highest probability to churn customers are in month to month contract type.
    colors = ['royalblue','lightskyblue']
    contract_churn = data.groupby(['Contract','Churn']).size().unstack()

    ax = (contract_churn.T*100.0 / contract_churn.T.sum()).T.plot(kind='bar',width = 0.3,stacked = True,rot = 0, figsize = (10,6),color = colors)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.legend(loc='center right',prop={'size':14},title = 'Churn', bbox_to_anchor=(1.25, 0.5))
    ax.set_ylabel('percentage of Customers',size = 14)
    ax.set_title('Churn by Contract Type',size = 14)

    # Code to add the data labels on the stacked bar chart
    for p in ax.patches:
      width, height = p.get_width(), p.get_height()
      x, y = p.get_xy() 
      ax.annotate('{:.0f}%'.format(height), (p.get_x()+.25*width, p.get_y()+.4*height),color = 'black',weight = 'bold',size = 14)
    ax.figure
    
if pageview == 'Contract':
    st.subheader("Contract")
    # st.write(data)
    #Pie chart of percentages of senior citizens
    ax = sns.countplot(x="Contract", data=data, palette="Blues")
    for p in ax.patches:
      percentage = '{:.1f}%'.format(100 * p.get_height()/len(data))
      x = p.get_x() + p.get_width()
      y = p.get_height()
      ax.annotate(percentage, (x, y),ha='right') 
    ax.figure

