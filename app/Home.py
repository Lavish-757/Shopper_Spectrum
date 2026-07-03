# ============================================================
# Shopper Spectrum: E-Commerce Customer Analytics Dashboard
# Home Page
# ============================================================

# Import Libraries

import streamlit as st
import plotly.express as px

from utils import (
    load_data,
    hero_banner,
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
# Load Dataset
# ============================================================

df = load_data()

# ============================================================
# Dashboard KPIs
# ============================================================

customers = df["CustomerID"].nunique()
orders = df["InvoiceNo"].nunique()
products = df["StockCode"].nunique()
countries = df["Country"].nunique()
revenue = df["TotalPrice"].sum()

# ============================================================
# Monthly Revenue
# ============================================================

monthly_sales = (
    df.groupby(df["InvoiceDate"].dt.to_period("M"))["TotalPrice"]
      .sum()
      .reset_index()
)

monthly_sales["InvoiceDate"] = (
    monthly_sales["InvoiceDate"].astype(str)
)

# ============================================================
# Top Countries
# ============================================================

country_sales = (
    df.groupby("Country")["TotalPrice"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

# ============================================================
# Hero Banner
# ============================================================

hero_banner()

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# Dashboard Overview
# ============================================================

section_title("📊", "Dashboard Overview")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("👥 Customers", f"{customers:,}")

with col2:
    st.metric("🛒 Orders", f"{orders:,}")

with col3:
    st.metric("📦 Products", f"{products:,}")

with col4:
    st.metric("💰 Revenue", f"£{revenue/1_000_000:.2f} M")

with col5:
    st.metric("🌍 Markets", countries)


st.info(
    f"""
### 💡 Quick Insights

- 👥 **{customers:,}** unique customers
- 🛒 **{orders:,}** completed orders
- 📦 **{products:,}** unique products
- 🌍 Business operations across **{countries}** countries
- 💰 Total revenue exceeds **£{revenue/1_000_000:.2f} Million**
"""
)

st.divider()

# ============================================================
# Dashboard Charts
# ============================================================

left, right = st.columns(2)

# ------------------------------------------------------------
# Monthly Revenue Trend
# ------------------------------------------------------------

with left:

    section_title("📈", "Monthly Revenue Trend")

    fig1 = px.line(
        monthly_sales,
        x="InvoiceDate",
        y="TotalPrice",
        markers=True,
        template="plotly_dark"
    )

    fig1.update_traces(line=dict(width=3))

    fig1.update_layout(
        height=430,
        xaxis_title="Month",
        yaxis_title="Revenue (£)",
        hovermode="x unified",

        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True)
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

# ------------------------------------------------------------
# Top Countries
# ------------------------------------------------------------

with right:

    section_title("🌍", "Top Countries by Revenue")

    fig2 = px.bar(
        country_sales,
        x="TotalPrice",
        y="Country",
        orientation="h",
        color="TotalPrice",
        color_continuous_scale="Blues",
        template="plotly_dark"
    )

    fig2.update_traces(
        texttemplate="£%{x:,.0f}",
        textposition="outside"
    )

    fig2.update_layout(
        height=430,
        xaxis_title="Revenue (£)",
        yaxis_title="",
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

# ============================================================
# Executive Summary
# ============================================================

section_title("💡", "Executive Summary")

st.success(
    """
This dashboard provides an end-to-end analysis of customer purchasing behaviour using data analytics and machine learning.

It enables businesses to:

• Understand customer purchasing patterns

• Identify high-value customer segments

• Analyze sales trends

• Recommend related products

• Support data-driven decision making
"""
)
st.divider()

# ============================================================
# Footer
# ============================================================

st.markdown(
"""
<div style="text-align:center;padding:15px">

### 🛍️ Shopper Spectrum

End-to-End Customer Analytics Dashboard

Built using Python • Pandas • Plotly • Scikit-learn • Streamlit

</div>
""",
unsafe_allow_html=True
)