# ============================================================
# Shopper Spectrum: Customer Segmentation
# ============================================================

# Import Libraries

import streamlit as st
import pandas as pd
import plotly.express as px

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

# ============================================================
# Load Customer Segmentation Data
# ============================================================

rfm = pd.read_csv("data/customer_segments.csv")

# ============================================================
# Page Header
# ============================================================

section_title("👥", "Customer Segmentation")

st.write(
    """
This page analyzes customers using **RFM (Recency, Frequency, Monetary) Analysis**.

Customers are grouped into meaningful business segments based on their purchasing behaviour,
helping businesses design targeted marketing strategies and improve customer retention.
"""
)

st.divider()

# ============================================================
# Segment KPIs
# ============================================================

total_customers = len(rfm)

segments = rfm["Customer_Segment"].nunique()

best_segment = (
    rfm["Customer_Segment"]
       .value_counts()
       .idxmax()
)

avg_rfm = rfm["RFM_Score"].mean()

section_title("📊", "Segment Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Customers",
        f"{total_customers:,}"
    )

with col2:
    st.metric(
        "📌 Segments",
        segments
    )

with col3:
    st.metric(
        "🏆 Largest Segment",
        best_segment
    )

with col4:
    st.metric(
        "⭐ Avg RFM Score",
        f"{avg_rfm:.2f}"
    )

st.divider()

# ============================================================
# Customer Segment Distribution
# ============================================================

section_title("🍩", "Customer Segment Distribution")

st.caption(
    "Distribution of customers across the identified RFM segments."
)

st.write("")

segment_counts = (
    rfm["Customer_Segment"]
    .value_counts()
    .reset_index()
)

segment_counts.columns = [
    "Customer_Segment",
    "Customers"
]

fig = px.pie(
    segment_counts,
    names="Customer_Segment",
    values="Customers",
    hole=0.55,
    color="Customer_Segment",
    color_discrete_map={
        "High-Value": "#2ca02c",
        "Regular": "#1f77b4",
        "Occasional": "#ff7f0e",
        "At-Risk": "#d62728"
    }
)

fig.update_traces(

    textposition="inside",

    textinfo="percent+label",

    hovertemplate=
    "<b>%{label}</b><br>"
    "Customers: %{value}<br>"
    "Percentage: %{percent}<extra></extra>"
)

fig.update_layout(

    height=500,

    showlegend=True,

    legend_title="Customer Segment",

    margin=dict(
        l=20,
        r=20,
        t=20,
        b=20
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ============================================================
# Average RFM Values by Segment
# ============================================================

section_title("📊", "Average RFM Values by Segment")

segment_summary = (
    rfm.groupby("Customer_Segment")[
        ["Recency", "Frequency", "Monetary"]
    ]
    .mean()
    .round(2)
    .reset_index()
)

col1, col2, col3 = st.columns(3)

# -----------------------------
# Average Recency
# -----------------------------
with col1:

    fig1 = px.bar(
        segment_summary,
        x="Customer_Segment",
        y="Recency",
        color="Customer_Segment",
        template="plotly_dark"
    )

    fig1.update_traces(
        texttemplate="%{y:.0f}",
        textposition="outside"
    )

    fig1.update_layout(
        title="Average Recency",
        height=380,
        showlegend=False,
        xaxis_title="",
        yaxis_title="Days"
    )

    st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# Average Frequency
# -----------------------------
with col2:

    fig2 = px.bar(
        segment_summary,
        x="Customer_Segment",
        y="Frequency",
        color="Customer_Segment",
        template="plotly_dark"
    )

    fig2.update_traces(
        texttemplate="%{y:.1f}",
        textposition="outside"
    )

    fig2.update_layout(
        title="Average Frequency",
        height=380,
        showlegend=False,
        xaxis_title="",
        yaxis_title="Purchases"
    )

    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Average Monetary
# -----------------------------
with col3:

    fig3 = px.bar(
        segment_summary,
        x="Customer_Segment",
        y="Monetary",
        color="Customer_Segment",
        template="plotly_dark"
    )

    fig3.update_traces(
        texttemplate="£%{y:,.0f}",
        textposition="outside"
    )

    fig3.update_layout(
        title="Average Monetary",
        height=380,
        showlegend=False,
        xaxis_title="",
        yaxis_title="Revenue (£)"
    )

    st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ============================================================
# Segment Summary
# ============================================================

section_title("📋", "Segment Summary")

segment_summary = (
    rfm.groupby("Customer_Segment")
       .agg(
           Customers=("Customer_Segment", "count"),
           Avg_Recency=("Recency", "mean"),
           Avg_Frequency=("Frequency", "mean"),
           Avg_Monetary=("Monetary", "mean")
       )
       .round(2)
       .reset_index()
)

st.dataframe(
    segment_summary,
    use_container_width=True,
    hide_index=True
)

# ============================================================
# Business Recommendations
# ============================================================

st.divider()

section_title("💡", "Business Recommendations")

st.success(
"""
### 📌 Recommended Business Actions

🟢 **High-Value Customers**

- Reward with exclusive loyalty programs.
- Offer premium memberships and early product access.
- Focus on long-term retention.

---

🔵 **Regular Customers**

- Encourage higher spending through bundle offers.
- Recommend complementary products.
- Send personalized promotions.

---

🟠 **Occasional Customers**

- Increase purchase frequency with limited-time discounts.
- Use email campaigns and personalized recommendations.
- Promote seasonal offers.

---

🔴 **At-Risk Customers**

- Launch win-back campaigns.
- Offer special discounts and incentives.
- Re-engage with personalized emails before churn.
"""
)

st.divider()