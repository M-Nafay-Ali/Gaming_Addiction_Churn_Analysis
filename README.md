# 🕹️ CHURN_HUNTER // Predictive Telemetry Terminal

An end-to-end Machine Learning and Data Science project engineered to analyze player behavioral metrics and predict churn probability within a gaming addiction dataset. This project moves beyond flat prototyping by implementing production-grade, type-safe preprocessing pipelines and an automated hyperparameter optimization architecture, culminating in a live, custom-themed web deployment.

🔗 **Live Predictive App:** [gamingaddictionchurnanalysis.streamlit.app](https://gamingaddictionchurnanalysis.streamlit.app/)

---

## 🚀 Key Architectural Features

* **Modular Production Pipelines:** Utilizes Scikit-Learn `Pipeline` and `ColumnTransformer` modules to partition and execute type-specific transformations (`StandardScaler` for numerical metrics, `OrdinalEncoder` for ranked tiers, and `OneHotEncoder` for nominal classifications) simultaneously, guaranteeing zero data leakage during cross-validation.
* **Automated Hyperparameter Tuning:** Implements an automated machine learning training loop that evaluates 5 distinct mathematical approaches simultaneously (`Linear Regression`, `Ridge`, `Random Forest`, `SVR`, and `XGBoost`). It conducts an exhaustive grid search (`GridSearchCV`) utilizing 3-fold cross-validation optimized against Mean Squared Error.
* **Statistical Discipline & Residual Audit:** Features validation set analysis using Out-of-Sample metrics ($R^2$ Score and Root Mean Squared Error) accompanied by structural error distribution modeling via Seaborn Kernel Density Estimation (KDE) to inspect predictive skew.
* **Cyberpunk/Arcade UI Deployment:** Built using a high-vibrancy Streamlit interface utilizing responsive CSS injection, custom container blocks, and runtime type-checking to dynamically match user inputs against the saved model's exact metadata layout.

---

## 📊 Dataset Features & Telemetry Monitored

The model processes multi-dimensional player profile metrics to evaluate retention risks:
* **Temporal Attributes:** `age`, `years_gaming`
* **Engagement Indicators:** `daily_playtime_hours`, `weekly_play_sessions`, `subscription_status`
* **Performance Indicators:** `gpa_or_performance_score`, `rank_tier`
* **Psychometric & Behavioral Profiles:** `stress_score`, `depression_indicator`, `mental_health_risk_score`, `behavioral_cluster`
* **Demographics & Hardware Environment:** `gender`, `country`, `occupation`, `income_level`, `platform`, `device_type`

---

## 🛠️ Repository & System Structure

```text
├── app.py                      # Interactive Cyberpunk Streamlit Web Application
├── final_churn_model.pkl       # Saved production-grade Random Forest Pipeline binary
├── requirements.txt            # Explicit software dependencies (scikit-learn v1.6.1)
└── gaming_churn_notebook.ipynb # Notebook containing Pipeline design, training loops, & EDA

---

---

> ### 🎮 DEVELOPER PANEL // CONNECT
> 
> * **GitHub Profile:** [@M-Nafay-Ali](https://github.com/M-Nafay-Ali)
> * **LinkedIn:** [https://www.linkedin.com/in/mohammed-nafay-ali-16519138a?utm_source=share_via&utm_content=profile&utm_medium=member_android]
> * **Live Deployment Terminal:** [CHURN_HUNTER App](https://gamingaddictionchurnanalysis.streamlit.app/)
>* **Email:-**englandengland271@gmail.com
