import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Page Configuration & Custom Cyberpunk/Arcade Theme Injection
st.set_page_config(
    page_title="CHURN_HUNTER // Terminal",
    page_icon="🎮",
    layout="wide"
)

# Custom neon/dark arcade styling
st.markdown("""
    <style>
    /* Main app background */
    .stApp {
        background: radial-gradient(circle, #120c1f 0%, #05030a 100%);
        color: #e0d5f5;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Neon titles and glowing headers */
    h1, h2, h3 {
        color: #00ffcc !important;
        text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc;
        font-family: 'Impact', sans-serif;
        letter-spacing: 2px;
    }
    
    /* Glowing sidebar panel */
    [data-testid="stSidebar"] {
        background-color: #0d0818 !important;
        border-right: 2px solid #ff007f;
        box-shadow: 5px 0px 15px rgba(255, 0, 127, 0.3);
    }
    
    /* Neon game-panel containers */
    .metric-card {
        background: rgba(20, 12, 35, 0.75);
        border: 2px solid #00ffcc;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
        text-align: center;
    }
    
    .danger-card {
        background: rgba(35, 10, 25, 0.8);
        border: 2px solid #ff007f;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.4);
        text-align: center;
    }
    
    /* Custom arcade button style */
    .stButton>button {
        background: linear-gradient(45deg, #ff007f, #7928ca) !important;
        color: white !important;
        border: 2px solid #00ffcc !important;
        box-shadow: 0 0 10px #ff007f;
        font-weight: bold !important;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px #00ffcc;
        color: #00ffcc !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Header and Intro
st.title("🕹️ CHURN_HUNTER // PREDICTIVE TERMINAL")
st.markdown("### `SYSTEM STATUS: ONLINE` // `TARGET: CHURN PROBABILITY MODEL`")
st.markdown("---")

# 3. Load Your Trained Pipeline Safely
@st.cache_resource
def load_pipeline():
    try:
        # Looks for the file in your GitHub repo directory
        return joblib.load("final_churn_model.pkl")
    except:
        return None

model_pipeline = load_pipeline()

# Inform user if the pickle binary is missing
if model_pipeline is None:
    st.error("⚠️ 'final_churn_model.pkl' not found! Make sure to upload the model file to your GitHub repository.")
    st.stop()

# 4. Interactive Sidebar Inputs (Gaming Variables)
st.sidebar.markdown("## ⚙️ PLAYER PROFILE VARIABLES")

# Numerical Input Sliders
age = st.sidebar.slider("Player Age", 13, 40, 22)
years_gaming = st.sidebar.slider("Years Gaming Experience", 1, 25, 9)
daily_playtime = st.sidebar.slider("Daily Playtime (Hours)", 0.5, 12.0, 6.0)
weekly_sessions = st.sidebar.slider("Weekly Play Sessions", 1, 15, 7)
gpa_score = st.sidebar.slider("GPA / Performance Score", 1.0, 4.0, 3.0)

# Categorical Dropdowns (Matches your preprocessing setup)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
country = st.sidebar.selectbox("Country", ["India", "USA", "Brazil", "South Korea", "Japan", "Other"])
preferred_genre = st.sidebar.selectbox("Preferred Genre", ["Sandbox", "RPG", "Strategy", "MMORPG", "FPS", "Other"])
behavioral_cluster = st.sidebar.selectbox("Behavioral Cluster", ["Casual", "Hardcore", "Social", "Achiever"])

occupation = st.sidebar.selectbox("Occupation", ["Student", "Employed", "Unemployed", "Streamer/Contest Creator"])
income_level = st.sidebar.selectbox("Income Level", ["Low", "Middle", "Upper-Middle", "High"])
platform = st.sidebar.selectbox("Platform", ["PC", "Mobile", "PC+Mobile", "Console", "PC+Console"])
device_type = st.sidebar.selectbox("Device Type", ["Laptop", "Mixed", "High-end PC", "Console", "Mobile"])
rank_tier = st.sidebar.selectbox("Rank Tier", ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Master"])
subscription_status = st.sidebar.selectbox("Subscription Status", ["Active", "Inactive"])

# Optional Extra Mental Health Indicators
stress_score = st.sidebar.slider("Stress Score", 0.0, 10.0, 5.0)
depression_indicator = st.sidebar.slider("Depression Indicator Value", 0.0, 10.0, 4.0)
mental_health_risk = st.sidebar.slider("Mental Health Risk Score", 0.0, 10.0, 5.0)

# 5. Preparing Data for the Prediction Pipeline
# Create a row matching the original structure layout of df
input_data = pd.DataFrame([{
    'age': age, 'years_gaming': years_gaming, 'daily_playtime_hours': daily_playtime,
    'weekly_play_sessions': weekly_sessions, 'gender': gender, 'country': country,
    'preferred_genre': preferred_genre, 'behavioral_cluster': behavioral_cluster,
    'occupation': occupation, 'income_level': income_level, 'platform': platform,
    'device_type': device_type, 'rank_tier': rank_tier, 'subscription_status': subscription_status,
    'gpa_or_performance_score': gpa_score, 'stress_score': stress_score, 
    'depression_indicator': depression_indicator, 'mental_health_risk_score': mental_health_risk
}])

# Fill in defaults for any training features not explicitly chosen in sliders
# to protect the input pipeline shape
for col in model_pipeline.feature_names_in_:
    if col not in input_data.columns:
        input_data[col] = 0.0

# Ensure strict matching column order
input_data = input_data[model_pipeline.feature_names_in_]

# 6. Main Terminal Console Interface Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📊 ACTIVE PROFILE MATRIX")
    st.dataframe(input_data[['age', 'years_gaming', 'daily_playtime_hours', 'preferred_genre', 'platform', 'rank_tier']])
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 EXECUTE QUANTUM CHURN PROJECTION"):
        # Run prediction directly via your pipeline
        prediction = model_pipeline.predict(input_data)[0]
        prediction_pct = float(prediction * 100)
        
        st.markdown("### 🖥️ CORE LOGGING COMPUTATION")
        if prediction_pct > 60.0:
            st.markdown(f"""
                <div class="danger-card">
                    <h2 style='color: #ff007f !important;'>🔴 HIGH RISK PROFILE DETECTED</h2>
                    <h1 style='color: #ff007f !important; font-size: 50px;'>{prediction_pct:.2f}%</h1>
                    <p>Player exhibits high probability of critical subscriber churn. Intervention recommended.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="metric-card">
                    <h2 style='color: #00ffcc !important;'>🟢 STABLE PLAYER PROFILE</h2>
                    <h1 style='color: #00ffcc !important; font-size: 50px;'>{prediction_pct:.2f}%</h1>
                    <p>Retention signals within green tolerance limits. Low churn variance expected.</p>
                </div>
            """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🎮 TELEMETRY STATS")
    st.markdown(f"""
        <div style='background: rgba(10, 5, 20, 0.6); padding: 15px; border-radius: 8px; border: 1px dashed #7928ca; margin-bottom: 10px;'>
            <span style='color: #ff007f;'>🎮 PLATFORM:</span> {platform}<br>
            <span style='color: #00ffcc;'>🏆 RANK TIER:</span> {rank_tier}<br>
            <span style='color: #7928ca;'>⏳ PLAYTIME:</span> {daily_playtime} Hrs/Day
        </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Pro-Tip: Adjust player profile values on the left panel dynamically, then hit execute to run immediate analytical regressions.")

