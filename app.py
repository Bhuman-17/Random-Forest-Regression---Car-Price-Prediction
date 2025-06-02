import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("random_forest_regressor_pipeline.joblib")

# App title and description
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")
st.title("🚗 Car Selling Price Predictor")
st.markdown("### By **Bhuman Wadekar**")
st.markdown(
    """
    Fill in the car details below and click **Predict** to estimate the car's selling price.  
    The model uses a trained **Random Forest Regressor** under the hood.  
    """
)

with st.form("car_form"):
    st.subheader("🔧 Car Specifications")

    col1, col2 = st.columns(2)
    with col1:
        brand = st.selectbox("🚘 Brand", ['Maruti', 'Hyundai', 'Honda', 'Toyota', 'Ford', 'Renault', 'Volkswagen'])
        fuel_type = st.selectbox("⛽ Fuel Type", ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
        seller_type = st.selectbox("🧑‍💼 Seller Type", ['Dealer', 'Individual', 'Trustmark Dealer'])
        transmission_type = st.radio("🔁 Transmission", ['Manual', 'Automatic'])

    with col2:
        vehicle_age = st.slider("📆 Vehicle Age (years)", 0, 25, 4)
        km_driven = st.number_input("🛣️ Kilometres Driven", 1000, 300000, 40000, step=1000)
        mileage = st.number_input("📏 Mileage (kmpl)", 5.0, 40.0, 20.5, step=0.1)
        engine = st.number_input("🏎️ Engine (CC)", 600, 5000, 1197)
        max_power = st.number_input("⚡ Max Power (bhp)", 30.0, 300.0, 82.0, step=1.0)
        seats = st.select_slider("💺 Number of Seats", options=[2, 4, 5, 6, 7, 8, 9, 10], value=5)

    submit = st.form_submit_button("🔍 Predict Selling Price")

if submit:
    new_data = pd.DataFrame([{
        'brand': brand,
        'vehicle_age': vehicle_age,
        'km_driven': km_driven,
        'seller_type': seller_type,
        'fuel_type': fuel_type,
        'transmission_type': transmission_type,
        'mileage': mileage,
        'engine': engine,
        'max_power': max_power,
        'seats': seats
    }])

    predicted_price = model.predict(new_data)[0]
    st.markdown("---")
    st.success(f"💰 **Estimated Selling Price:** ₹{predicted_price:,.2f}")
    st.markdown("---")
    st.balloons()


