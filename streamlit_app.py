if st.button("🔮 Predict Result"):

    total = math + reading + writing

    if total >= 150:
        st.markdown("<div class='result-box' style='background:#d4edda'>✅ PASS</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result-box' style='background:#f8d7da'>❌ FAIL</div>", unsafe_allow_html=True)
