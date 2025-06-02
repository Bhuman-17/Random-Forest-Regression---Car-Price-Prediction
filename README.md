###🚗 Car Price Prediction App

A Streamlit web application that predicts the **selling price of a car** based on specifications like brand, mileage, fuel type, engine power, etc. The prediction is powered by a trained **Random Forest Regressor**.
##⚙️ Features

- Interactive UI using **Streamlit**
- Input car details using sliders and dropdowns
- Predict selling price instantly
- Built using `scikit-learn`, `joblib`, `pandas`, and `numpy`

---

## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/car-price-prediction-app.git
cd car-price-prediction-app
pip install -r requirements.txt
🚀 Run the App
bash
Copy
Edit
streamlit run app.py
📥 Input Features
brand: Car manufacturer (e.g., Maruti, Honda)

vehicle_age: Age of the vehicle in years

km_driven: Total distance driven

seller_type: Dealer / Individual

fuel_type: Petrol / Diesel / CNG / etc.

transmission_type: Manual / Automatic

mileage: kmpl

engine: Engine capacity in CC

max_power: Maximum BHP

seats: Number of seats

🧠 Model
Type: RandomForestRegressor

Training done on a dataset with car listings and prices

Model saved as random_forest_regressor_pipeline.joblib

# Streamlit App link : https://bhuman-17-random-forest-regression---car-price-predi-app-1tytbr.streamlit.app/
