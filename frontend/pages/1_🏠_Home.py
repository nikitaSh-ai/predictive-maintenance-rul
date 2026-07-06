import streamlit as st

st.title("🏠 Home")

st.markdown(
    """
    ## Explainable Predictive Maintenance Decision Support System

    Welcome to the dashboard.

    This system estimates the Remaining Useful Life (RUL) of industrial engines
    using Machine Learning and Deep Learning while providing Explainable AI,
    Uncertainty Estimation and Decision Intelligence.
    """
)

st.divider()

st.subheader("Project Modules")

col1, col2 = st.columns(2)

with col1:

    st.success("✅ Random Forest")

    st.success("✅ XGBoost")

    st.success("✅ GRU")

with col2:

    st.success("✅ Explainable AI")

    st.success("✅ Uncertainty")

    st.success("✅ Decision Intelligence")




st.divider()

st.subheader("Project Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Primary Model",
        value="GRU"
    )

with col2:
    st.metric(
        label="Best R² Score",
        value="0.9019"
    )

with col3:
    st.metric(
        label="Backend Status",
        value="Complete ✅"
    )





st.divider()

st.subheader("AI Pipeline")

st.code(
"""
NASA C-MAPSS Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Random Forest / XGBoost / GRU
        │
        ▼
Explainable AI
(SHAP / Captum)
        │
        ▼
Uncertainty Estimation
        │
        ▼
Decision Intelligence Engine
        │
        ▼
Maintenance Recommendation
""",
language="text"
)



