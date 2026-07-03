# ============================================================
# Shopper Spectrum: Utility Functions
# ============================================================

# Import Libraries

import streamlit as st
import pandas as pd

# ============================================================
# Load Dataset
# ============================================================

@st.cache_data
def load_data():
    """
    Load and preprocess the cleaned online retail dataset.
    """

    df = pd.read_csv("data/OnlineRetail_cleaned.csv")

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    return df


# ============================================================
# Section Title
# ============================================================

def section_title(icon, title):
    """
    Display a styled section heading.
    """

    st.markdown(f"## {icon} {title}")

# ============================================================
# Sidebar
# ============================================================

def sidebar():
    """
    Display the application sidebar.
    """

    with st.sidebar:

        st.markdown(
            "### 📂 Analytics Dashboard"
        )

        st.info(
            """
Navigate using the pages above.

Explore:

• 📊 Dataset Overview

• 📈 Sales Analysis

• 👥 Customer Segmentation

• 🤖 Customer Clustering

• 🛍️ Product Recommendation
"""
        )

        st.markdown("---")

        st.markdown("### 🛠️ Built With")

        st.markdown(
            """
- Python
- Pandas
- Plotly
- Scikit-learn
- Streamlit
"""
        )

# ============================================================
# Hero Banner
# ============================================================

def hero_banner():
    """
    Display the dashboard hero banner.
    """

    st.markdown(
        """
        <div style="
        background:linear-gradient(135deg,#2563EB,#1D4ED8);
        padding:22px;
        border-radius:20px;
        color:white;
        box-shadow:0px 8px 20px rgba(0,0,0,.25);
        ">

        <h1>🛍️ Shopper Spectrum</h1>

        <h3 style="color:#DBEAFE;">
        E-Commerce Customer Analytics Dashboard
        </h3>

        <p style="font-size:18px;">

        Transforming customer transaction data into meaningful
        business insights using Data Analytics,
        Machine Learning and Interactive Dashboards.

        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )