import requests
import streamlit as st

api_base_url = "http://127.0.0.1:8000/"

def login_user(username:str, password:str):
    url = f"{api_base_url}/auth/login"
    response = requests.post(url,params={"username": username, "password": password})
    if response.status_code == 200:
        data = response.json()
        st.session_state["access_token"] = data["access_token"]
        return True
    else:
        st.error("Invalid username or password")
        return False
    

def predict_price(features: dict):
    token = st.session_state.get("access_token", None)
    if not token:
        st.warning("Please login first.")
        return None
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{api_base_url}/predict/", json=features, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Prediction failed: {response.text}")
        return None