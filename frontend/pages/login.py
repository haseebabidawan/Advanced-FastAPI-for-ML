import streamlit as st
from utils.api_client import login_user

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("🔐 Login to Car Price Predictor")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if login_user(username, password):
        st.success("✅ Logged in successfully!")
        st.switch_page("pages/predict.py")
