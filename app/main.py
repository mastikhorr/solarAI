
import streamlit as st
from app.image_analysis import analyze_image
from app.roi_estimator import estimate_roi

st.title("☀️ Solar Industry AI Assistant")
uploaded_file = st.file_uploader("Upload a rooftop satellite image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    analysis = analyze_image(uploaded_file)
    roi_report = estimate_roi(analysis)
    st.subheader("Solar Panel Recommendation")
    st.json(analysis)
    st.subheader("ROI Estimate")
    st.json(roi_report)
