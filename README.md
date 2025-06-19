
# 🛒 Shopper Spectrum: Customer Segmentation and Product Recommendations in E-Commerce

This project analyzes e-commerce customer behavior using **RFM segmentation** and builds an **item-based collaborative filtering recommendation system**. It also features an interactive **Streamlit dashboard** for real-time predictions.

---

## 📌 Problem Statement

E-commerce companies handle massive transaction data daily. Understanding customer purchasing behavior is crucial for:
- Targeted marketing
- Customer retention
- Personalized product recommendations

This project segments customers based on RFM metrics and recommends products using collaborative filtering.

---

## 🎯 Objectives

- Perform **RFM-based clustering** of customers  
- Build an **item-based recommender system**  
- Develop a **Streamlit web app** with:
  - Product recommendation
  - Customer segment prediction

---

## 📂 Dataset

- **Features**:
  - `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`

---

## 🧪 Project Workflow

### 1️⃣ Data Preprocessing
- Removed missing `CustomerID`
- Excluded cancelled/invalid orders
- Calculated `TotalAmount`

### 2️⃣ RFM Feature Engineering
- `Recency`: Days since last purchase
- `Frequency`: Number of invoices
- `Monetary`: Total spend

### 3️⃣ Clustering (KMeans)
- Applied log transformation + scaling
- Used **Elbow Method** & **Silhouette Score**
- Assigned labels:
  - **High-Value**
  - **Regular**
  - **Occasional**
  - **At-Risk**

### 4️⃣ Recommendation System
- Built Customer–Product matrix
- Used **cosine similarity** between products
- Suggested top 5 similar products

---

## 📈 Streamlit App Features

### 🧍 Customer Segmentation
- Input: Recency, Frequency, Monetary
- Output: Predicted Segment (e.g., High-Value)

### 📦 Product Recommendation
- Input: Product Name
- Output: Top 5 similar products

---

## 📁 Files Included

| File                            | Description                            |
|------------------------------  -|----------------------------------------|
| `SHOPPERSPECTRUM.ipynb`         | Streamlit dashboard                    |
| `shopperstreamlit.py`           | Streamlit dashboard                    |
| `rfm_kmeans_model.pkl`          | Saved model + scaler + segment labels  |
| `product_similarity_matrix.pkl` | Cosine similarity matrix               |
| `online_retail.csv`             | Original dataset                       |


---

## 📊 Libraries Used

- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `scikit-learn`
- `streamlit`
- `pickle`

---


## ✅ Business Use Cases

- 🎯 Targeted Marketing
- 💬 Personalized Recommendations
- 🔁 Customer Retention
- 📊 Inventory & Pricing Strategies

---
![image](https://github.com/user-attachments/assets/5b15089b-e79f-428e-9f84-28005c7e1bfc)
![image](https://github.com/user-attachments/assets/1b397548-185d-49d1-82e5-53661af39cdd)


