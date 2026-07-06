import streamlit as st

st.set_page_config(
    page_title="Predictive Maintenance",
    page_icon="⚙️",
    layout="wide"
)

st.title(
    "Explainable Predictive Maintenance Decision Support System"
)

st.markdown(
    """
    Welcome to the AI-powered Decision Support System for
    Remaining Useful Life (RUL) estimation of industrial equipment.

    This application combines Machine Learning, Deep Learning,
    Explainable AI, Uncertainty Estimation and Decision Intelligence
    to provide transparent maintenance recommendations.
    """
)

st.divider()

st.subheader("Backend Status")

st.success("✅ Backend Completed")

st.write("Available Modules")

st.markdown("""
- Random Forest
- XGBoost
- GRU
- Explainable AI
- Uncertainty Estimation
- Decision Intelligence
""")