import streamlit as st
import pandas as pd
import joblib
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title="Marvellous Infosystems Dashboard", page_icon="📊")

st.title("📊 Customer Dashboard")
st.caption("Customer churn Predictions")

st.write("Machine Learning Application Dashboard")

python_image = Image.open('python.png')


model = joblib.load("Marvellous_ML_Customer_Churn.pkl")

st.subheader("Enter customer details")

#age = st.number_input("Customer Age",min_value=1)
age = st.slider("Customer Age", min_value=0, max_value=100, value=25)
tenure = st.slider("Tenure (Months)", min_value=1, max_value=60, value=5)
charges = st.slider("Monthly Charges", min_value=100, max_value=10000, value=500)
calls = st.slider("Support calls",min_value=0, max_value=300, value=2)

#tenure = st.number_input("Tenure (Months)",min_value=0)
#charges = st.number_input("Monthly Charges",min_value=0)
#calls = st.number_input("Support calls",min_value=0)

if st.button("Predict Churn"):
    new_customer = pd.DataFrame({
    "Age" : [age],
    "Tenure" : [tenure],
    "MonthlyCharges" : [charges],
    "SupportCalls" : [calls]
    })

    prediction = model.predict(new_customer)[0]

    if prediction == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is unlikely to churn")

# ---- KPIs ----

k1,k2,k3,k4 = st.columns(4)
k1.metric("Age", age)
k2.metric("Tenure", tenure)
k3.metric("Monthly charges", charges)
k4.metric("Support calls", calls)


st.divider()

