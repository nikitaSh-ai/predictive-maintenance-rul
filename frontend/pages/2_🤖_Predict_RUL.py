import streamlit as st

st.title("🤖 Predict Remaining Useful Life")

st.markdown(
    """
    Upload engine sensor data to estimate the Remaining Useful Life (RUL)
    and generate an AI-powered maintenance recommendation.
    """
)

st.divider()

st.subheader("Input Data")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

predict_button = st.button(
    "Predict RUL"
)