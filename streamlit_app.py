import streamlit as st

st.title("Student Pass Prediction")

gender = st.selectbox("Gender",["male","female"])

if st.button("Predict"):
    st.write("Prediction result here")
