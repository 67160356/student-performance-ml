import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# page config
st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)

# CSS
st.markdown("""
<style>
.big-font {
    font-size:40px !important;
    font-weight:bold;
}
.result-box {
    padding:20px;
    border-radius:10px;
    text-align:center;
    font-size:25px;
}
</style>
""", unsafe_allow_html=True)

# load model + dataset
model = pickle.load(open("model.pkl","rb"))
df = pd.read_csv("Student_performance_10k.csv")

# header
st.markdown("<p class='big-font'>🎓 Student Performance AI Dashboard</p>", unsafe_allow_html=True)
st.write("Predict student success using Machine Learning")

st.divider()

# layout
col1, col2 = st.columns(2)

# INPUT
with col1:

    st.subheader("📊 Student Scores")

    math = st.slider("Math Score",0,100,50)
    reading = st.slider("Reading Score",0,100,50)
    writing = st.slider("Writing Score",0,100,50)

    input_data = pd.DataFrame({
        "math_score":[math],
        "reading_score":[reading],
        "writing_score":[writing]
    })

    if st.button("🔮 Predict Result"):

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.markdown("<div class='result-box' style='background:#d4edda'>✅ PASS</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-box' style='background:#f8d7da'>❌ FAIL</div>", unsafe_allow_html=True)

# SCORE GRAPH
with col2:

    st.subheader("📈 Score Visualization")

    scores = [math, reading, writing]
    subjects = ["Math","Reading","Writing"]

    fig, ax = plt.subplots()

    ax.bar(subjects, scores)
    ax.set_ylim(0,100)
    ax.set_ylabel("Score")

    st.pyplot(fig)

st.divider()

# DATASET PREVIEW
st.subheader("📂 Dataset Preview")
st.dataframe(df.head())

st.divider()

# MODEL INFO
st.subheader("🤖 Model Info")

st.write("Model used: **Machine Learning Classifier**")
st.write("Features used:")
st.write("- Math Score")
st.write("- Reading Score")
st.write("- Writing Score")

st.caption("Built with Python • Scikit-learn • Streamlit")
