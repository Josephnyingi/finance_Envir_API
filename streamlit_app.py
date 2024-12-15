import streamlit as st
import requests
import pandas as pd

# Set up the app
st.set_page_config(page_title="Liquidity & Environmental Risk API", layout="wide")

st.title("Liquidity & Environmental Risk Data API Showcase")

# Sidebar Navigation
menu = st.sidebar.radio("Navigate", ["Upload Liquidity Risk Data", "Link Environmental Risk Data", "Generate Correlation Analysis"])

BASE_URL = "https://api.example.com/v1"  # Replace with your API base URL

# Upload Liquidity Risk Data
if menu == "Upload Liquidity Risk Data":
    st.subheader("Upload Liquidity Risk Data")
    risk_level = st.selectbox("Risk Level", ["Low", "Medium", "High"])
    risk_value = st.number_input("Risk Value", value=0.0, format="%.2f")
    timestamp = st.text_input("Timestamp (YYYY-MM-DDTHH:MM:SSZ)", value="2024-12-10T14:30:00Z")
    
    if st.button("Upload"):
        payload = {
            "riskLevel": risk_level,
            "riskValue": risk_value,
            "timestamp": timestamp
        }
        response = requests.post(f"{BASE_URL}/liquidity-risk/upload", json=payload)
        if response.status_code == 200:
            st.success("Data uploaded successfully!")
            st.json(response.json())
        else:
            st.error("Failed to upload data.")

# Link Environmental Risk Data
elif menu == "Link Environmental Risk Data":
    st.subheader("Link Environmental Risk Data")
    disaster_likelihood = st.slider("Disaster Likelihood", 0.0, 1.0, 0.5)
    ecosystem_vulnerability = st.slider("Ecosystem Vulnerability", 0.0, 1.0, 0.5)
    geo_position = st.text_input("Geo-Position (e.g., Lat: 1.2921, Long: 36.8219)", "Lat: 1.2921, Long: 36.8219")
    data_source = st.text_input("Data Source", "Satellite")
    timestamp = st.text_input("Timestamp (YYYY-MM-DDTHH:MM:SSZ)", "2024-12-10T14:30:00Z")
    
    if st.button("Link Data"):
        payload = {
            "disasterLikelihood": disaster_likelihood,
            "ecosystemVulnerability": ecosystem_vulnerability,
            "geoPosition": geo_position,
            "dataSource": data_source,
            "timestamp": timestamp
        }
        response = requests.post(f"{BASE_URL}/environmental-risk-data/link", json=payload)
        if response.status_code == 200:
            st.success("Environmental risk data linked successfully!")
            st.json(response.json())
        else:
            st.error("Failed to link data.")

# Generate Correlation Analysis
elif menu == "Generate Correlation Analysis":
    st.subheader("Generate Correlation Analysis")
    financial_risk_id = st.number_input("Financial Risk ID", value=0, step=1)
    environmental_risk_id = st.number_input("Environmental Risk ID", value=0, step=1)
    correlation_type = st.selectbox("Correlation Type", ["Pearson", "Spearman"])
    
    if st.button("Generate Analysis"):
        payload = {
            "financialRiskId": financial_risk_id,
            "environmentalRiskId": environmental_risk_id,
            "correlationType": correlation_type
        }
        response = requests.post(f"{BASE_URL}/correlation-analysis/generate", json=payload)
        if response.status_code == 200:
            st.success("Correlation analysis generated successfully!")
            st.json(response.json())
        else:
            st.error("Failed to generate correlation analysis.")
