import streamlit as st

st.set_page_config(page_title="Car Price Predictor", page_icon="🚘")

st.sidebar.title("Navigation")
st.sidebar.page_link("pages/login.py", label="🔐 Login")
st.sidebar.page_link("pages/predict.py", label="🚗 Predict Price")

st.title("🚘 Welcome to Car Price Predictor")
st.write(
    """
    This app demonstrates a production-grade **FastAPI + Streamlit + Redis + JWT** workflow.
    - Secure login with JWT  
    - Real-time car price prediction  
    - Caching and monitoring integrated
    """
)
