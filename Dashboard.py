import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.markdown("# Statistics of users by services")
st.sidebar.markdown("# Services")

telecom_cust = pd.read_csv('ChurnDataset.csv', index_col='customerID')

services = ['PhoneService','MultipleLines','InternetService','OnlineSecurity',
           'OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']

fig, axes = plt.subplots(nrows = 3,ncols = 3,figsize = (15,12))
for i, item in enumerate(services):
    if i < 3:
        ax = telecom_cust[item].value_counts().plot(kind = 'bar',ax=axes[i,0],rot = 0)
        
    elif i >=3 and i < 6:
        ax = telecom_cust[item].value_counts().plot(kind = 'bar',ax=axes[i-3,1],rot = 0)
        
    elif i < 9:
        ax = telecom_cust[item].value_counts().plot(kind = 'bar',ax=axes[i-6,2],rot = 0)
    ax.set_title(item)

st.pyplot(fig)
st.markdown("# Paperless Billing users")
paperless_billing_chart = alt.Chart(telecom_cust).mark_bar().encode(
   x=alt.X('PaperlessBilling:N',axis=alt.Axis(title='Responses')),
   y=alt.Y('count():Q',axis=alt.Axis(title='No. of Users')),
   color=alt.Color('PaperlessBilling')      
).properties(
    width=800,
    height=400
)

st.write(paperless_billing_chart)

st.markdown("# Payment mode")
payment_chart = alt.Chart(telecom_cust).mark_bar().encode(
   x=alt.X('PaymentMethod:N',axis=alt.Axis(title='Responses')),
   y=alt.Y('count():Q',axis=alt.Axis(title='No. of Users')),
   color=alt.Color('PaymentMethod')      
).properties(
    width=800,
    height=400
)

st.write(payment_chart)
