import streamlit as st
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 Student Performance AI Dashboard")
st.write("Predict student success based on exam scores")

st.divider()

# Layout
col1, col2 = st.columns(2)

# Input section
with col1:

    st.subheader("📊 Student Scores")

    math = st.slider("Math Score", 0, 100, 50)
    reading = st.slider("Reading Score", 0, 100, 50)
    writing = st.slider("Writing Score", 0, 100, 50)

    if st.button("🔮 Predict Result"):

        total = math + reading + writing

        # Rule 1: Writing must be at least 50
        if writing < 50:
            st.error("❌ FAIL (Writing Score must be at least 50)")

        # Rule 2: Total score must be >=150
        elif total >= 150:
            st.success("✅ PASS")

        else:
            st.error("❌ FAIL")

# Visualization section
with col2:

    st.subheader("📈 Score Visualization")

    scores = [math, reading, writing]
    subjects = ["Math", "Reading", "Writing"]

    fig, ax = plt.subplots()

    ax.bar(subjects, scores)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Score")

    st.pyplot(fig)

st.divider()

st.caption("Built with Streamlit • Student Performance Prediction")
