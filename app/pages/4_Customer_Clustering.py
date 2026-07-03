import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from utils import (
    section_title,
    sidebar
)

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
[data-testid="stSidebarNav"]::before {
    content: "🛍️ Shopper Spectrum";
    display: block;
    text-align: center;
    font-size: 26px;
    font-weight: 800;
    color: black;
    padding: 20px 10px;
    margin-bottom: 10px;
    border-bottom: 1px solid rgba(128,128,128,0.2);
}
</style>
""", unsafe_allow_html=True)

sidebar()

# Load dataset
rfm = pd.read_csv("data/customer_segments.csv")

# Load model
kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# ============================================================
# Customer Cluster Prediction
# ============================================================

section_title("🤖", "Customer Cluster Prediction")

st.write(
    """
Enter a customer's **Recency**, **Frequency**, and **Monetary**
values to predict which customer cluster they belong to using
the trained K-Means model.
"""
)

col1, col2, col3 = st.columns(3)

with col1:

    recency = st.number_input(
        "Recency (days)",
        min_value=0,
        value=30
    )

with col2:

    frequency = st.number_input(
        "Frequency",
        min_value=1,
        value=5
    )

with col3:

    monetary = st.number_input(
        "Monetary (£)",
        min_value=0.0,
        value=1000.0
    )

predict = st.button(
    "🔍 Predict Cluster",
    use_container_width=True
)

if predict:

    customer = pd.DataFrame({
        "Recency": [recency],
        "Frequency": [frequency],
        "Monetary": [monetary]
    })

    customer_scaled = scaler.transform(customer)

    cluster = kmeans.predict(customer_scaled)[0]

    cluster_labels = {
        0: "Occasional",
        1: "At-Risk",
        2: "High-Value",
        3: "Regular"
    }

    prediction = cluster_labels[cluster]
    
    st.success(
        f"### 🎯 Predicted Customer Segment: **{prediction}**"
    )

    if prediction == "High-Value":

        st.info(
            """
🟢 **High-Value Customer**

• Recent purchaser

• Frequent buyer

• High spender

Recommended Action:
Reward with loyalty programs and premium offers.
"""
        )

    elif prediction == "Regular":

        st.info(
            """
🔵 **Regular Customer**

• Purchases consistently

• Moderate spending

Recommended Action:
Cross-sell and upsell related products.
"""
        )

    elif prediction == "Occasional":

        st.info(
            """
🟠 **Occasional Customer**

• Shops occasionally

• Lower purchase frequency

Recommended Action:
Increase engagement through promotions and email campaigns.
"""
        )

    else:

        st.info(
            """
🔴 **At-Risk Customer**

• Long time since last purchase

• Low activity

Recommended Action:
Launch win-back campaigns and personalized discounts.
"""
        )

# ============================================================
# Cluster Interpretation
# ============================================================

st.divider()

section_title("💡", "Cluster Interpretation")

st.info(
"""
### 📊 Understanding the Clusters

🟢 **High-Value**
- Recent purchasers
- Purchase very frequently
- Highest spending customers
- Focus on retention and VIP rewards.

---

🔵 **Regular**
- Purchase consistently
- Moderate-to-high spending
- Strong potential to become High-Value customers.
- Encourage with loyalty programs and personalized offers.

---

🟠 **Occasional**
- Shop infrequently
- Low purchase frequency
- Moderate spending
- Increase engagement through promotions and reminders.

---

🔴 **At-Risk**
- Long time since last purchase
- Very low purchase frequency
- Lowest spending
- Re-engage with win-back campaigns and special discounts.
"""
)

st.divider()