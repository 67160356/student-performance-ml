import streamlit as st
import pickle
import pandas as pd

# load model
model = pickle.load(open("model.pkl","rb"))

st.title("🎓 Student Performance Prediction")

st.write("Predict if a student will pass based on exam scores")

math = st.slider("Math Score",0,100,50)
reading = st.slider("Reading Score",0,100,50)
writing = st.slider("Writing Score",0,100,50)

input_data = pd.DataFrame({
    "math_score":[math],
    "reading_score":[reading],
    "writing_score":[writing]
})

if st.button("Predict"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Student will PASS")
    else:
        st.error("❌ Student may FAIL")
