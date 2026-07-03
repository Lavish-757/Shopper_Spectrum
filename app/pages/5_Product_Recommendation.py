import streamlit as st
import joblib
import pandas as pd

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

# Load customer-product matrix
customer_product_matrix = pd.read_csv(
    "data/customer_product_matrix.csv",
    index_col=0
)

# Load similarity matrix
product_similarity = joblib.load(
    "models/product_similarity.pkl"
)

section_title("📦", "Product Recommender")

st.write(
    """
Select a product from the list below to receive **5 similar product recommendations**
based on historical customer purchasing behaviour using an
**Item-Based Collaborative Filtering** recommendation system.
"""
)

products = customer_product_matrix.columns.tolist()

product_name = st.selectbox(
    "Select Product",
    sorted(products)
)

recommend = st.button(
    "🔍 Get Recommendations",
    use_container_width=True
)

if recommend:

    product_index = products.index(product_name)

    similarity_scores = list(
    enumerate(product_similarity.iloc[product_index].values)
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in similarity_scores[1:6]:

        recommendations.append(products[index])

    st.divider()

    section_title("📦", "Recommended Products")

    for i, product in enumerate(recommendations, start=1):

        st.container(border=True).markdown(
            f"**{i}. {product}**"
        )

st.divider()