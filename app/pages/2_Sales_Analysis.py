# ============================================================
# Shopper Spectrum: Sales Analysis
# ============================================================

# Import Libraries

import streamlit as st
import plotly.express as px

from utils import (
    load_data,
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
# Page Header
# ============================================================

section_title("📈", "Sales Analysis")

st.write(
    """
    This page provides an overview of sales performance using
    revenue trends, order patterns, top-selling products,
    and country-wise sales analysis.
    """
)

st.divider()

# ============================================================
# Sales KPIs
# ============================================================

total_revenue = df["TotalPrice"].sum()

total_orders = df["InvoiceNo"].nunique()

total_quantity = df["Quantity"].sum()

average_order_value = total_revenue / total_orders

# ============================================================
# Sales Overview
# ============================================================

section_title("📊", "Sales Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Revenue",
        f"£{total_revenue/1_000_000:.2f} M"
    )

with col2:
    st.metric(
        "🛒 Orders",
        f"{total_orders:,}"
    )

with col3:
    st.metric(
        "📦 Quantity Sold",
        f"{total_quantity:,}"
    )

with col4:
    st.metric(
        "💵 Avg Order Value",
        f"£{average_order_value:.2f}"
    )

st.info(
    f"""
### 💡 Quick Insights

- 💰 Total revenue generated: **£{total_revenue:,.2f}**
- 🛒 Customers placed **{total_orders:,}** orders.
- 📦 More than **{total_quantity:,}** products were sold.
- 💵 Average revenue per order is **£{average_order_value:.2f}**.
"""
)

st.divider()

# ============================================================
# Monthly Revenue
# ============================================================

monthly_revenue = (
    df.groupby(df["InvoiceDate"].dt.to_period("M"))["TotalPrice"]
      .sum()
      .reset_index()
)

monthly_revenue["InvoiceDate"] = (
    monthly_revenue["InvoiceDate"].astype(str)
)

# ============================================================
# Monthly Orders
# ============================================================

monthly_orders = (
    df.groupby(df["InvoiceDate"].dt.to_period("M"))["InvoiceNo"]
      .nunique()
      .reset_index()
)

monthly_orders["InvoiceDate"] = (
    monthly_orders["InvoiceDate"].astype(str)
)

# ============================================================
# Top Products
# ============================================================

top_products = (
    df.groupby("Description")["TotalPrice"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

# ============================================================
# Top Countries
# ============================================================

top_countries = (
    df.groupby("Country")["TotalPrice"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

# ============================================================
# Sales Charts
# ============================================================

left, right = st.columns(2)

# ------------------------------------------------------------
# Monthly Revenue Trend
# ------------------------------------------------------------

with left:

    section_title("📈", "Monthly Revenue Trend")

    fig1 = px.line(
        monthly_revenue,
        x="InvoiceDate",
        y="TotalPrice",
        markers=True,
        template="plotly_dark"
    )

    fig1.update_traces(
        line=dict(width=3)
    )

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
# Monthly Orders Trend
# ------------------------------------------------------------

with right:

    section_title("📅", "Monthly Orders Trend")

    fig2 = px.line(
        monthly_orders,
        x="InvoiceDate",
        y="InvoiceNo",
        markers=True,
        template="plotly_dark"
    )

    fig2.update_traces(
        line=dict(width=3)
    )

    fig2.update_layout(
        height=430,
        xaxis_title="Month",
        yaxis_title="Orders",
        hovermode="x unified",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True)
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

left, right = st.columns(2)

# ------------------------------------------------------------
# Top Products by Revenue
# ------------------------------------------------------------

with left:

    section_title("📦", "Top 10 Products by Revenue")

    fig3 = px.bar(
        top_products,
        x="TotalPrice",
        y="Description",
        orientation="h",
        color="TotalPrice",
        color_continuous_scale="Viridis",
        template="plotly_dark"
    )

    fig3.update_traces(
        texttemplate="£%{x:,.0f}",
        textposition="outside"
    )

    fig3.update_layout(
        height=430,
        xaxis_title="Revenue (£)",
        yaxis_title="",
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )


# ------------------------------------------------------------
# Top Countries by Revenue
# ------------------------------------------------------------

with right:

    section_title("🌍", "Top 10 Countries by Revenue")

    fig4 = px.bar(
        top_countries,
        x="TotalPrice",
        y="Country",
        orientation="h",
        color="TotalPrice",
        color_continuous_scale="Blues",
        template="plotly_dark"
    )

    fig4.update_traces(
        texttemplate="£%{x:,.0f}",
        textposition="outside"
    )

    fig4.update_layout(
        height=430,
        xaxis_title="Revenue (£)",
        yaxis_title="",
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.divider()

# ============================================================
# Business Insights
# ============================================================

section_title("💡", "Business Insights")

st.success(
    f"""
### Key Findings

- 💰 Total revenue generated is **£{total_revenue:,.2f}**.
- 🛒 Customers placed **{total_orders:,}** unique orders.
- 📦 More than **{total_quantity:,}** items were sold.
- 🌍 Sales were generated across **{df['Country'].nunique()}** countries.
- 📈 Revenue and order trends reveal monthly variations that can help identify seasonal demand.
- ⭐ A small number of products contribute a significant share of total revenue, making them ideal candidates for focused inventory management and marketing campaigns.
"""
)

# ============================================================
# Sales Performance Summary
# ============================================================

section_title("📌", "Sales Performance Summary")

st.markdown(
"""
The sales analysis highlights overall business performance across revenue,
orders, products, and geographic markets.

The visualizations reveal monthly sales trends, identify the highest
revenue-generating products, and show the countries contributing most to
overall revenue.

These insights help stakeholders monitor business growth, evaluate product
performance, and support strategic decision-making through data-driven
analytics.
"""
)

st.divider()