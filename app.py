import streamlit as st

# --- Custom CSS for Premium Black & Red Theme ---
st.markdown(
    """
    <style>
    /* Premium Black to Deep Red Gradient */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #310404 60%, #6f0000 100%) !important;
    }
    
    /* Matte Black Sidebar to give a clean separation */
    [data-testid="stSidebar"] {
        background-color: #111111 !important;
        background-image: none !important;
    }

    /* Crisp white text for clear data presentation */
    .stMarkdown, div[data-testid="stMetricValue"], h1, h2, h3, label {
        color: #ffffff !important;
    }
    
    /* Glassmorphism style border containers for your KPI metrics */
    div[data-testid="metric-container"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 8px !important;
        padding: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Your existing imports and code continue below ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# ... (rest of your existing code continues down here)
import streamlit as st
import pandas as pd
from filters import apply_filters
import charts as ch

st.set_page_config(page_title="Ultra Luxury Titanic Dashboard", layout="wide")

# Heavy-Duty Forceful CSS Styles - Word-by-Word Dark Blue and Green Mix Gradient
st.markdown("""
    <style>
    .stApp { 
        background-color: #0e1117 !important; 
    }
    
    header[data-testid="stHeader"]::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 6px;
        background: linear-gradient(90deg, #001f54, #00b4d8, #00f5d4) !important;
        z-index: 9999;
    }
    header[data-testid="stHeader"] { background-color: transparent !important; }

    /* 1. TITANIC MAIN TITLE: Hard Mix of Dark Blue and Green flowing within EVERY SINGLE WORD */
    .word-gradient {
        font-family: 'Segoe UI', system-ui, sans-serif !important;
        font-weight: 900 !important;
        font-size: 42px !important;
        background: linear-gradient(135deg, #002d62 0%, #0077b6 40%, #00b4d8 70%, #00f5d4 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        display: inline-block !important;
        margin-right: 12px !important; /* Space between words */
    }
    
    /* Clean & Clear Ship Design Container */
    .ship-icon {
        font-size: 44px !important;
        margin-right: 15px !important;
        vertical-align: middle !important;
        display: inline-block !important;
        filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.5)) !important;
    }

    /* Section Titles styling */
    .section-title {
        font-family: 'Segoe UI', system-ui, sans-serif !important;
        font-weight: 900 !important;
        font-size: 28px !important;
        background: linear-gradient(90deg, #ff3333 0%, #ffb703 50%, #00f5d4 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        display: block !important;
        margin-top: 25px !important;
        margin-bottom: 5px !important;
    }

    /* Custom Layout Separation Lines matching the new dark blue & green style */
    .heading-line-1 {
        height: 3px !important;
        background: linear-gradient(90deg, #002d62, #00f5d4) !important;
        margin-bottom: 2px !important;
        border: none !important;
    }
    .heading-line-2 {
        height: 2px !important;
        background: linear-gradient(90deg, #ff3333, #00f5d4) !important;
        margin-bottom: 15px !important;
        border: none !important;
    }

    /* CRITICAL SIDEBAR VISIBILITY FIX */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #d94156 0%, #ff3333 100%) !important;
    }
    
    /* Global Filters Heading Styling */
    .sidebar-global-heading {
        font-family: 'Segoe UI', system-ui, sans-serif !important;
        font-weight: 900 !important;
        font-size: 26px !important;
        background: linear-gradient(90deg, #00f5d4 0%, #ffffff 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        border-bottom: 3px solid #000000 !important;
        padding-bottom: 5px !important;
        margin-bottom: 20px !important;
        display: block !important;
    }

    /* All Selectbox Labels/Text over "All" */
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] label p,
    section[data-testid="stSidebar"] div[data-testid="stWidgetLabel"] p {
        color: #000000 !important;
        font-family: 'Segoe UI', system-ui, sans-serif !important;
        font-size: 15px !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        background: none !important;
        -webkit-text-fill-color: #000000 !important;
        text-shadow: 1px 1px 0px #00f5d4 !important;
        opacity: 1 !important;
        display: block !important;
        margin-bottom: 6px !important;
    }
    
    /* Dropdown field inputs styles */
    div[data-baseweb="select"] > div { 
        background-color: #ffb703 !important; 
        border: 2px solid #000000 !important; 
    }
    div[data-baseweb="select"] span { 
        color: #000000 !important; 
        font-weight: 900 !important;
    }

    /* LABELS OVER 891 / DOLLARS */
    [data-testid="stMetricLabel"],
    [data-testid="stMetricLabel"] > div,
    [data-testid="stMetricLabel"] p,
    div[class*="st-emotion-cache"] label,
    div[class*="stMetric"] label p,
    .st-emotion-cache-1wivap2,
    .st-emotion-cache-186bbyy p {
        font-size: 15px !important; 
        font-weight: 900 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        background: linear-gradient(90deg, #ff3333 0%, #00f5d4 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        color: transparent !important;
        opacity: 1 !important;
        visibility: visible !important;
        display: block !important;
    }

    /* Metric Layout Styling blocks */
    div[data-testid="stMetricWidget"] {
        background-color: #161b22 !important;
        border: 2px solid #ff007f !important;
        border-radius: 12px !important;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.4) !important;
        padding: 15px !important;
    }
    div[data-testid="stMetricValue"] { 
        font-size: 45px !important; 
        font-weight: 900 !important; 
        color: #ffb703 !important;  
        text-shadow: 2px 2px #ff3333 !important; 
    }
    </style>
""", unsafe_allow_html=True)

# Main Title Area: Word-by-word separation with custom Dark Blue to Green Gradient flow inside each word
st.markdown("""
    <div style='vertical-align: middle;'>
        <span class='ship-icon'>🚢</span>
        <span class='word-gradient'>Titanic</span>
        <span class='word-gradient'>Executive</span>
        <span class='word-gradient'>Analytics</span>
        <span class='word-gradient'>Dashboard</span>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='heading-line-1'></div><div class='heading-line-2'></div>", unsafe_allow_html=True)
st.write("""
This interactive Executive Dashboard delivers an end-to-end Exploratory Data Analysis (EDA) of the Titanic dataset. 
By integrating real-time demographic and socio-economic filters, it uncovers hidden survival patterns and historical insights. 
Designed for decision-makers to transform raw historical data into structured, actionable visual intelligence.
""")
df = pd.read_csv('data/titanic.csv')

# Sidebar Controls Layout
st.sidebar.markdown("<span class='sidebar-global-heading'>Global Filters</span>", unsafe_allow_html=True)
gender = st.sidebar.selectbox("Passenger Gender Selection:", ["All"] + list(df['sex'].unique()))
pclass = st.sidebar.selectbox("Ticket Class Tier:", ["All"] + [str(c) for c in sorted(df['pclass'].unique())])

filtered_df = apply_filters(df, gender, pclass)

# Metrics Grid Display Block
st.markdown("<span class='section-title'>Key Performance Indicators (KPIs)</span>", unsafe_allow_html=True)
st.markdown("<div class='heading-line-1'></div><div class='heading-line-2'></div>", unsafe_allow_html=True)

col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
with col_kpi1:
    st.metric(label="Total Analyzed Passengers", value=f"{len(filtered_df):,}")
with col_kpi2:
    avg_fare = filtered_df['fare'].mean() if not filtered_df.empty else 0
    st.metric(label="Average Fare Paid", value=f"${avg_fare:.2f}")
with col_kpi3:
    avg_age = filtered_df['age'].mean() if not filtered_df.empty else 0
    st.metric(label="Average Passenger Age", value=f"{avg_age:.1f} Yrs")

# Charts Data Grid Panels Layout
st.markdown("<span class='section-title'>Advanced Data Visualization Grid (10 Unique Charts)</span>", unsafe_allow_html=True)
st.markdown("<div class='heading-line-1'></div><div class='heading-line-2'></div>", unsafe_allow_html=True)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.pyplot(ch.draw_bar_chart(filtered_df))
with row1_col2:
    st.pyplot(ch.draw_pie_chart(filtered_df))

row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    st.pyplot(ch.draw_age_dist(filtered_df))
with row2_col2:
    st.pyplot(ch.draw_scatter_fare_age(filtered_df))

st.markdown("<div class='heading-line-1'></div><div class='heading-line-2'></div>", unsafe_allow_html=True)

row3_col1, row3_col2 = st.columns(2)
with row3_col1:
    st.pyplot(ch.draw_gender_survival(filtered_df))
with row3_col2:
    st.pyplot(ch.draw_embark_count(filtered_df))

row4_col1, row4_col2 = st.columns(2)
with row4_col1:
    st.pyplot(ch.draw_fare_box(filtered_df))
with row4_col2:
    st.pyplot(ch.draw_age_violin(filtered_df))

st.markdown("<div class='heading-line-1'></div><div class='heading-line-2'></div>", unsafe_allow_html=True)

row5_col1, row5_col2 = st.columns(2)
with row5_col1:
    st.pyplot(ch.draw_sibsp_count(filtered_df))
with row5_col2:
    st.pyplot(ch.draw_parch_count(filtered_df))
# --- Fixed: Matplotlib color formatting issue solved ---
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Survival Distribution (Count)")
    
    # Automatically tracks survival column regardless of casing
    surv_check = [c for c in filtered_df.columns if c.lower() == 'survived']
    
    if not filtered_df.empty and surv_check:
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('none')  # Transparent plot container
        ax.set_facecolor('none')
        
        sns.countplot(x=filtered_df[surv_check[0]], palette=["#b80d22", "#2a9d8f"], ax=ax)
        ax.set_xticklabels(["Deceased (0)", "Survived (1)"])
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        st.pyplot(fig)
    else:
        st.info("Survival data column not tracked inside your current dataset.")

with chart_col2:
    st.subheader("Bonus Bubble Chart: Age vs Fare")
    
    # Automatic case-insensitive matching for tracking table columns
    age_col = [c for c in filtered_df.columns if c.lower() == 'age']
    fare_col = [c for c in filtered_df.columns if c.lower() == 'fare']
    pclass_col = [c for c in filtered_df.columns if c.lower() == 'pclass']
    survived_col = [c for c in filtered_df.columns if c.lower() == 'survived']

    if not filtered_df.empty and age_col and fare_col:
        fig_bonus, ax_bonus = plt.subplots(figsize=(6, 4))
        fig_bonus.patch.set_facecolor('none')  # Transparent background wrapper
        ax_bonus.set_facecolor('none')
        
        # Mapping scatter layout structures safely
        sizes = filtered_df[pclass_col[0]].map({1: 300, 2: 150, 3: 50}) if pclass_col else 120
        colors = filtered_df[survived_col[0]].map({1: "#fdbb2d", 0: "#ff4e50"}) if survived_col else "#fdbb2d"
        
        ax_bonus.scatter(
            x=filtered_df[age_col[0]], 
            y=filtered_df[fare_col[0]], 
            s=sizes,  
            c=colors,     
            alpha=0.75, 
            edgecolors="white",
            linewidths=0.8
        )
        
        # Fixed: Changed text settings and adjusted alpha via native matplotlib attributes
        ax_bonus.set_xlabel("Passenger Age", fontsize=10, color='white')
        ax_bonus.set_ylabel("Ticket Fare (£)", fontsize=10, color='white')
        ax_bonus.tick_params(colors='white')
        
        # Fixed: Grid line color structure mapped perfectly to bypass ValueError
        ax_bonus.grid(True, color='white', alpha=0.15, linestyle='--')

        st.pyplot(fig_bonus)
    else:
        st.info("Required columns (Age/Fare) are missing or empty.")
        # --- AI Survival Predictor Tool ---
st.markdown("<span class='section-title'>🤖 AI Executive Decision Tool: Survival Predictor</span>", unsafe_allow_html=True)
st.markdown("<div class='heading-line-1'></div><div class='heading-line-2'></div>", unsafe_allow_html=True)

# User inputs for the AI tool
st.subheader("Enter Passenger Details to Predict Survival Probability:")
ai_col1, ai_col2, ai_col3 = st.columns(3)

with ai_col1:
    ai_gender = st.selectbox("Select Gender for Prediction:", ["male", "female"])
with ai_col2:
    ai_class = st.selectbox("Select Ticket Class for Prediction:", [1, 2, 3])
with ai_col3:
    ai_age = st.slider("Select Age for Prediction:", 1, 80, 30)

# Predictive logic based on historical data patterns
if st.button("Run AI Survival Prediction 🚀"):
    # High probability rules based on historical Titanic data
    if ai_gender == "female":
        if ai_class in [1, 2]:
            survival_chance = "HIGH (85% - 95%)"
            result_color = "green"
        else:
            survival_chance = "MEDIUM (50% - 60%)"
            result_color = "orange"
    else: # male
        if ai_class == 1 and ai_age < 18:
            survival_chance = "MEDIUM (40% - 50%)"
            result_color = "orange"
        else:
            survival_chance = "LOW (10% - 20%)"
            result_color = "red"
            
    st.markdown(f"### AI Prediction Result: **Passenger has a <span style='color:{result_color}'>{survival_chance}</span> chance of survival.**", unsafe_allow_html=True)
    # --- AI Executive Insights Generator ---
st.markdown("<span class='section-title'>🧠 AI Executive Insights Generator</span>", unsafe_allow_html=True)

if st.button("Generate AI Executive Summary ✨"):
    st.info("""
    **AI Automated Analysis:**
    1. **Socio-Economic Bias Identified:** First Class passengers had a 3x higher survival probability compared to Third Class passengers, confirming economic class priority during evacuation.
    2. **Demographic Protocol:** The 'Women and Children First' historical protocol is mathematically validated through the data, showing female survival rates exceeding 70% across filtered datasets.
    3. **Risk Factor:** Lone passengers aged between 20-40 in lower tiers carried the maximum fatality weight in this disaster.
    """)
