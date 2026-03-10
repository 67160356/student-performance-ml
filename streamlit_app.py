import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Performance AI", layout="wide")

st.title("🎓 Student Performance AI Dashboard")
st.write("Predict student success using simple score rules")

st.divider()

col1, col2 = st.columns(2)

# INPUT
with col1:

    st.subheader("📊 Student Scores")

    math = st.slider("Math Score",0,100,50)
    reading = st.slider("Reading Score",0,100,50)
    writing = st.slider("Writing Score",0,100,50)

    if st.button("🔮 Predict Result"):

        total = math + reading + writing

        if total >= 150:
            st.success("✅ PASS")
        else:
            st.error("❌ FAIL")

# GRAPH
with col2:

    st.subheader("📈 Score Visualization")

    scores = [math, reading, writing]
    subjects = ["Math","Reading","Writing"]

    fig, ax = plt.subplots()

    ax.bar(subjects, scores)
    ax.set_ylim(0,100)
    ax.set_ylabel("Score")

    st.pyplot(fig)
