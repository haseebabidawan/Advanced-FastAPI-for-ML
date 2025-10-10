import streamlit as st
from utils.api_client import predict_price

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

# Ensure user is logged in
if "access_token" not in st.session_state:
    st.warning("⚠️ Please log in first!")
    st.stop()

st.title("🚗 Car Price Predictor")
st.markdown("Fill in the car details below to estimate its market value:")

col1, col2, col3 = st.columns(3)

with col1:
    company = st.text_input("🏢 Company Name", "Toyota")
    year = st.number_input("📅 Manufacture Year", min_value=1990, max_value=2025, value=2018)
    owner = st.selectbox("👤 Owner Type", ["First", "Second", "Third", "Fourth & Above"])
    fuel = st.selectbox("⛽ Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
    
with col2:
    seller_type = st.selectbox("🏷️ Seller Type", ["Dealer", "Individual", "Trustmark Dealer"])
    transmission = st.selectbox("⚙️ Transmission", ["Manual", "Automatic"])
    km_driven = st.number_input("🛣️ Kilometers Driven", min_value=0.0, value=35000.0, step=100.0)
    mileage_mpg = st.number_input("⛽ Mileage (mpg)", min_value=1.0, value=15.5, step=0.5)

with col3:
    engine_cc = st.number_input("🔩 Engine (CC)", min_value=500.0, value=1498.0, step=50.0)
    max_power_bhp = st.number_input("⚡ Max Power (BHP)", min_value=20.0, value=118.0, step=5.0)
    torque_nm = st.number_input("🔧 Torque (Nm)", min_value=50.0, value=145.0, step=5.0)
    seats = st.number_input("💺 Seats", min_value=2.0, max_value=9.0, value=5.0)

st.divider()

if st.button("🔍 Predict Price"):
    features = {
        "company": company,
        "year": int(year),
        "owner": owner,
        "fuel": fuel,
        "seller_type": seller_type,
        "transmission": transmission,
        "km_driven": float(km_driven),
        "mileage_mpg": float(mileage_mpg),
        "engine_cc": float(engine_cc),
        "max_power_bhp": float(max_power_bhp),
        "torque_nm": float(torque_nm),
        "seats": float(seats)
    }

    with st.spinner("Predicting car price... 🧠"):
        result = predict_price(features)

    if result:
        st.success(f"💰 **Predicted Car Price:** {result['Predicted_price']} lakhs")
        st.balloons()
