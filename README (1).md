
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

- **Source**: Online Retail dataset (2010–2011 transactions)
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

| File                          | Description                           |
|-------------------------------|----------------------------------------|
| `app.py` / `clustering_app.py`| Streamlit dashboard                    |
| `rfm_kmeans_model.pkl`        | Saved model + scaler + segment labels |
| `product_similarity_matrix.pkl` | Cosine similarity matrix              |
| `online_retail.csv`           | Original dataset                       |

---

## 📊 Libraries Used

- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `scikit-learn`
- `streamlit`
- `pickle`

---

## 🚀 How to Run

1. Clone the repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
streamlit run app.py
```

---

## ✅ Business Use Cases

- 🎯 Targeted Marketing
- 💬 Personalized Recommendations
- 🔁 Customer Retention
- 📊 Inventory & Pricing Strategies

---

## 🧠 Author

> 📘 Project by **[Your Name]**  
> Guided by **Shadiya, Nehlath Harmain, Nilofer Mubeen**
