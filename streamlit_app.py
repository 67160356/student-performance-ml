import streamlit as st
import pickle
import pandas as pd

# page config
st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="centered"
)

# CSS styling
st.markdown("""
<style>
.big-title {
    text-align:center;
    font-size:40px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.result-pass {
    background-color:#d4edda;
    padding:20px;
    border-radius:10px;
    font-size:20px;
}

.result-fail {
    background-color:#f8d7da;
    padding:20px;
    border-radius:10px;
    font-size:20px;
}
</style>
""", unsafe_allow_html=True)

# load model
model = pickle.load(open("model.pkl","rb"))

# title
st.markdown('<p class="big-title">🎓 Student Performance AI</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Predict if a student will pass based on exam scores</p>', unsafe_allow_html=True)

# sliders
math = st.slider("📊 Math Score",0,100,50)
reading = st.slider("📚 Reading Score",0,100,50)
writing = st.slider("✏️ Writing Score",0,100,50)

st.write("")

# input dataframe
input_data = pd.DataFrame({
    "math_score":[math],
    "reading_score":[reading],
    "writing_score":[writing]
})

# predict button
if st.button("🔮 Predict Result"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.markdown('<div class="result-pass">✅ Student will PASS</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-fail">❌ Student may FAIL</div>', unsafe_allow_html=True)

# footer
st.write("")
st.caption("Machine Learning Model • Streamlit Web App")
