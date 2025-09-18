import streamlit as st
from backend1 import extract_text_from_image, parse_lab_values, interpret_lab_values

st.title("📄 Smart Medical Report Simplifier")
st.write("Upload your lab report image and get an easy-to-understand summary.")

uploaded_file = st.file_uploader("Upload Report Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with st.spinner("🔍 Extracting text..."):
        text = extract_text_from_image(uploaded_file)
    
    st.subheader("📑 Extracted Text")
    st.write(text if text.strip() else "No text detected.")

    if text.strip():
        with st.spinner("✨ Parsing and interpreting results..."):
            lab_values = parse_lab_values(text)
            interpreted = interpret_lab_values(lab_values)
        
        st.subheader("✅ Simplified Report")
        for test, info in interpreted.items():
            st.markdown(f"**{test}: {info['status']}** → {info['explanation']}")
