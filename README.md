# 🛍️ Shopper Spectrum

### End-to-End E-Commerce Customer Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Dashboard-FF4B4B?logo=streamlit)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?logo=github)

---

## 🚀 Live Demo

🔗 **Streamlit App:**  
*(Add your deployed app link here)*

## 💻 GitHub Repository

🔗 *(Add your GitHub repository link here)*

---

# 📌 Project Overview

**Shopper Spectrum** is an end-to-end Data Analytics and Machine Learning project that transforms raw e-commerce transaction data into meaningful business insights.

The dashboard helps businesses understand customer purchasing behaviour, identify valuable customer segments, analyze sales trends, and recommend similar products using machine learning.

The complete solution is deployed as an interactive **Streamlit web application**.

---

# 🎯 Business Problem

E-commerce companies generate millions of transaction records every year. Without proper analysis, businesses often struggle to:

- Identify high-value customers
- Detect customers at risk of churn
- Understand purchasing behaviour
- Discover sales trends
- Recommend relevant products
- Support data-driven marketing decisions

This project addresses these challenges using data analytics and machine learning techniques.

---

# 📊 Dataset

**Dataset:** Online Retail Dataset

The dataset contains transactional records from a UK-based online retail company between December 2010 and December 2011.

It includes information about:

- Invoice Number
- Product Description
- Quantity Purchased
- Unit Price
- Customer ID
- Country
- Invoice Date

The dataset is widely used for customer analytics, recommendation systems, and market basket analysis.

---

# ✨ Dashboard Features

## 🏠 Home

- Executive Dashboard
- Business KPIs
- Monthly Revenue Trend
- Top Countries by Revenue
- Executive Summary

---

## 📊 Dataset Overview

- Dataset Statistics
- Missing Value Analysis
- Customer Overview
- Product Overview
- Country Distribution

---

## 📈 Sales Analysis

- Monthly Revenue
- Monthly Orders
- Top Selling Products
- Revenue by Country
- Sales Insights

---

## 👥 Customer Segmentation

Business-oriented customer segmentation using **RFM Analysis**.

### Customer Segments

- 🟢 High-Value
- 🔵 Regular
- 🟠 Occasional
- 🔴 At-Risk

Features include:

- Segment Distribution
- Average RFM Metrics
- Segment Summary
- Business Recommendations

---

## 🤖 Customer Clustering

Machine Learning-based customer clustering using **K-Means Clustering**.

### Features

- Cluster Distribution
- Cluster Characteristics
- Interactive Customer Prediction
- Business Interpretation

Users can enter:

- Recency
- Frequency
- Monetary

to predict a customer's cluster in real time.

---

## 🛍️ Product Recommendation

Item-Based Collaborative Filtering recommendation system.

### Features

- Product Selection
- Top 5 Similar Product Recommendations
- Cosine Similarity
- Interactive Recommendation Engine

---

# 🤖 Machine Learning Pipeline

## Customer Segmentation

- RFM Analysis

## Customer Clustering

- StandardScaler
- K-Means Clustering

## Product Recommendation

- Customer–Product Matrix
- Cosine Similarity
- Item-Based Collaborative Filtering

---

# 📂 Project Structure

```text
Shopper_Spectrum/
│
├── app/
│   ├── app.py
│   ├── utils.py
│   └── pages/
│       ├── 1_Dataset_Overview.py
│       ├── 2_Sales_Analysis.py
│       ├── 3_Customer_Segmentation.py
│       ├── 4_Customer_Clustering.py
│       └── 5_Product_Recommendation.py
│
├── data/
|   ├── customer_product_matrix.csv
│   ├── customer_segments.csv
│   ├── OnlineRetail_cleaned.csv
│   ├── OnlineRetail.csv
│   └── rfm_table.csv
│
├── models/
│   ├── kmeans_model.pkl
│   ├── product_similarity.pkl
│   └── scaler.pkl
│
├── notebooks/
|   ├── 01_Data_Loading_Exploration.ipynb
|   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Exploratory_Data_Analysis.ipynb
│   ├── 04_Customer_Segmentation.ipynb
│   ├── 05_KMeans_Customer_Clustering.ipynb
│   └── 06_Product_Recommendation_System.ipynb
│
├── README.md
│
└── requirements.txt
```

---

# 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Plotly |
| Machine Learning | Scikit-learn |
| Recommendation System | Cosine Similarity |
| Dashboard | Streamlit |
| Model Serialization | Joblib |
| Version Control | Git & GitHub |

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Shopper_Spectrum.git
```

### Navigate to the project

```bash
cd Shopper_Spectrum
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app/app.py
```

---

# 📈 Key Business Insights

- 💰 Generated more than **£8.9 Million** in total revenue.
- 🌍 Customers from **37 countries**, with the UK contributing the majority of sales.
- 👥 RFM Analysis identifies high-value and at-risk customers for targeted marketing.
- 🤖 K-Means clustering discovers hidden customer groups based on purchasing behaviour.
- 🛍️ Item-based collaborative filtering recommends similar products to improve cross-selling opportunities.
- 📊 Interactive dashboards support data-driven business decision-making.

---

# 🚀 Future Enhancements

- Customer Lifetime Value Prediction
- Sales Forecasting
- Hybrid Recommendation System
- Product Images
- Advanced Dashboard Filters
- Cloud Database Integration

---

# 🎯 Skills Demonstrated

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- RFM Analysis
- Customer Segmentation
- K-Means Clustering
- Recommendation Systems
- Interactive Dashboard Development
- Machine Learning Deployment

---

# 👨‍💻 Author

## Lavish Gupta

**Aspiring Data Analyst | Data Science Enthusiast**

- 💼 LinkedIn: *(Add your LinkedIn profile)*
- 💻 GitHub: *(Add your GitHub profile)*
- 📧 Email: *(Add your email)*

---