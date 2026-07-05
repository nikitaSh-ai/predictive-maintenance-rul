# Explainable Predictive Maintenance Decision Support System for Remaining Useful Life Estimation Using Machine Learning

## Overview

This project presents an AI based Predictive Maintenance Decision Support System for estimating the Remaining Useful Life (RUL) of industrial equipment using the NASA C-MAPSS FD001 dataset.

The system combines machine learning, deep learning, Explainable AI (XAI), uncertainty estimation, and decision intelligence to provide not only accurate Remaining Useful Life predictions but also transparent explanations and actionable maintenance recommendations.

Unlike conventional predictive maintenance models that only estimate RUL, this project also estimates prediction confidence, explains model decisions, and generates maintenance recommendations through an integrated Decision Intelligence Engine.

---

## Key Features

- Remaining Useful Life (RUL) prediction
- Random Forest baseline model
- XGBoost baseline model
- GRU deep learning model
- Model comparison using MAE, RMSE, and R²
- Explainable AI using SHAP and Captum Integrated Gradients
- Prediction uncertainty estimation using Monte Carlo Dropout
- Decision Intelligence Engine
- Health Score estimation
- Risk Level assessment
- Maintenance Priority recommendation
- AI generated maintenance reports





---

## Project Architecture

```text
NASA C-MAPSS FD001 Dataset
            │
            ▼
Data Preprocessing
• Engine-level Train / Validation / Test Split
• Remaining Useful Life (RUL) Generation
• Feature Selection
• Feature Scaling
• Sequence Generation
            │
            ▼
Machine Learning Models
• Random Forest
• XGBoost
• GRU (Primary Model)
            │
            ▼
Model Evaluation
• MAE
• RMSE
• R² Score
            │
            ▼
Explainable AI
• SHAP (Random Forest)
• XGBoost Feature Importance
• Captum Integrated Gradients (GRU)
            │
            ▼
Uncertainty Estimation
• Monte Carlo Dropout
• Prediction Interval
• Decision Confidence
            │
            ▼
Decision Intelligence Engine
• Health Score
• Risk Level
• Maintenance Priority
• Inspection Targets
• AI Reasoning
• Maintenance Recommendation
            │
            ▼
Decision Report
• TXT Report
• JSON Report
```

---

## Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn, XGBoost |
| Deep Learning | PyTorch |
| Explainable AI | SHAP, Captum |
| Data Processing | NumPy, Pandas |
| Visualization | Matplotlib |
| Model Persistence | Joblib |
| Dataset | NASA C-MAPSS FD001 |





---

## Project Structure

```text
Project_Restart/
│
├── DATA/
│   ├── raw/
│   ├── processed/
│   └── sequences/
│
├── models/
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│   └── best_gru.pth
│
├── results/
│   ├── metrics/
│   ├── plots/
│   ├── predictions/
│   ├── explainability/
│   └── reports/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── explainability/
│   ├── uncertainty/
│   └── recommendation/
│
├── README.md
├── requirements.txt
└── .gitignore
```




---

## Model Performance

| Model | MAE | RMSE | R² |
|------|------:|------:|------:|
| Random Forest | 15.4379 | 18.5739 | 0.8042 |
| XGBoost | 13.4806 | 16.7643 | 0.8398 |
| GRU | **9.9226** | **13.1468** | **0.9019** |

The GRU model achieved the best predictive performance and was selected as the primary model for the Decision Intelligence Engine.






---

## Current Backend Capabilities

- End-to-end Remaining Useful Life prediction pipeline
- Automated preprocessing and sequence generation
- Multiple baseline model comparison
- Explainable AI using SHAP and Captum
- Prediction uncertainty estimation
- Decision confidence estimation
- Health score calculation
- Maintenance priority generation
- AI-based maintenance recommendations
- Automatic TXT and JSON report generation



---

## Future Work

- Develop an interactive Streamlit dashboard.
- Deploy the application for real-time inference.
- Extend the framework to additional NASA C-MAPSS subsets.
- Investigate Transformer-based architectures for Remaining Useful Life prediction.
- Integrate real industrial sensor streams.



---

## Author

**Nikita Sharma,Krishna Yadav,Deepika,Divyanshi Chippa**

B.Tech Computer Science and Engineering

Independent AI/ML Research Project