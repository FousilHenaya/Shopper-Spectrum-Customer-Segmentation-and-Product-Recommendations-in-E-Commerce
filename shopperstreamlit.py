import streamlit as st
import pickle
import numpy as np


# --- Load Saved KMeans Model, Scaler, and Segment Map ---
with open("rfm_kmeans_model.pkl", "rb") as f:
    model_data = pickle.load(f)

kmeans = model_data["model"]
scaler = model_data["scaler"]
segment_map = model_data["segment_map"]  # Optional


# ---- Load Product Similarity Matrix ----
with open("product_similarity_matrix.pkl", "rb") as f:
    similarity_matrix = pickle.load(f)

# ---- Recommendation Function ----
def get_similar_products(product_name, similarity_matrix, top_n=5):
    if product_name not in similarity_matrix.columns:
        return []
    similar_scores = similarity_matrix[product_name].sort_values(ascending=False)
    top_similar = similar_scores.iloc[1:top_n+1]
    return top_similar

# ---- Sidebar Navigation ----
st.sidebar.title("📺 HOME")
page = st.sidebar.radio("Go to", ["CLUSTERING", "RECOMMENDATION"])

# ---- Recommendation Page ----
if page == "RECOMMENDATION":
    st.title("🎯 PRODUCT RECOMMENDER")
    
    product_input = st.text_input("Enter Product Name", placeholder="E.g. GREEN VINTAGE SPOT BEAKER").strip().upper()
    
    if st.button("RECOMMEND"):
        if product_input:
            recommendations = get_similar_products(product_input, similarity_matrix)
            if isinstance(recommendations, list) or recommendations.empty:
                st.warning("❌ Product not found. Try a valid name.")
            else:
                st.markdown("**Recommended Products:**")
                for product, score in recommendations.items():
                    st.write(f"- {product}")
        else:
            st.warning("Please enter a product name.")

#--------------CLUSTERING PAGE---------------

if page == "CLUSTERING":
    

    st.title("🎯CUSTOMER SEGMENTATION")
    
    st.markdown("Enter customer RFM values to predict their segment.")
    
    # --- Input Fields ---
    recency = st.number_input("📅 Recency (days since last purchase):", min_value=0, step=1)
    frequency = st.number_input("🔁 Frequency (number of purchases):", min_value=0, step=1)
    monetary = st.number_input("💰 Monetary (total spend):", min_value=0.0, step=1.0)
    
    if st.button("Predict Segment"):
        # Prepare and transform input
        input_data = np.array([[recency, frequency, monetary]])
        input_log = np.log1p(input_data)         # Apply same log transform
        input_scaled = scaler.transform(input_log)
    
        # Predict cluster
        cluster_id = kmeans.predict(input_scaled)[0]
    
        # Get segment label
        segment = segment_map.get(cluster_id, f"Cluster {cluster_id}")
    
        st.success(f"🧾 Predicted Segment: **{segment}**")
    
