# ============================================================
# Shopper Spectrum: Dataset Overview
# ============================================================

# Import Libraries

import streamlit as st
import pandas as pd

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
# Page Title
# ============================================================

section_title("📊", "Dataset Overview")

st.write(
    """
    This page provides an overview of the cleaned e-commerce dataset,
    including its size, structure, data types, missing values,
    and summary statistics.
    """
)

st.divider()

# ============================================================
# Dataset Summary
# ============================================================

rows = df.shape[0]
columns = df.shape[1]
customers = df["CustomerID"].nunique()
countries = df["Country"].nunique()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📄 Rows", f"{rows:,}")

with col2:
    st.metric("📑 Columns", columns)

with col3:
    st.metric("👥 Customers", f"{customers:,}")

with col4:
    st.metric("🌍 Countries", countries)

st.divider()

# ============================================================
# Dataset Preview
# ============================================================

section_title("👀", "Dataset Preview")

st.success("✅ Showing first 10 records.")

st.dataframe(
    df.head(10),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ============================================================
# Dataset Information
# ============================================================

section_title("ℹ️", "Dataset Dictionary")

info_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Missing Values": df.isnull().sum().values
})

st.dataframe(
    info_df,
    use_container_width=True
)

st.divider()

# ============================================================
# Missing Values
# ============================================================

section_title("❌", "Missing Values")

st.success("✅ No missing values found in the cleaned dataset.")

missing = df.isnull().sum()

st.dataframe(
    missing.rename("Missing Values"),
    use_container_width=True
)

st.divider()

# ============================================================
# Summary Statistics
# ============================================================

section_title("📈", "Summary Statistics")

st.dataframe(
    df.describe().round(2),
    use_container_width=True
)

st.divider()

# ============================================================
# Key Insights
# ============================================================

section_title("💡", "Key Insights")

st.success(f"""
### Dataset Highlights

- 📄 The dataset contains **{rows:,}** records.
- 👥 Transactions belong to **{customers:,}** unique customers.
- 🌍 Customers are spread across **{countries}** countries.
- 📦 The dataset is fully cleaned and ready for analysis.
- 📊 This dataset powers the sales analysis, customer segmentation, and product recommendation modules.
""")

st.divider()