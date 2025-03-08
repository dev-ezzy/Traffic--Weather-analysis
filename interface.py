import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import datetime

# ========== 🌍 API Setup (Optional) ==========
# Dummy weather & traffic data (Replace with API calls)
def get_weather_data(location):
    """Simulate fetching live weather data"""
    return {
        "condition": np.random.choice(["Sunny", "Cloudy", "Rainy", "Windy", "Snow"]),
        "temperature": np.random.randint(5, 35),
        "wind_speed": np.random.randint(1, 30),
        "precipitation": np.random.randint(0, 100),
        "traffic_incidents": np.random.choice(["None", "Accident", "Heavy Traffic", "Road Closure"])
    }

# ========== 🎨 Dynamic Background Styling ==========
def set_background(weather_condition):
    """Set background based on weather conditions"""
    if weather_condition == "Sunny":
        bg_color = "#FFA500"  # Warm orange
        effect = "background: url('https://i.gifer.com/7DZn.gif'); background-size: cover;"  # Sun animation
    elif weather_condition == "Cloudy":
        bg_color = "#A9A9A9"  # Gray
        effect = "background: url('https://i.gifer.com/7tUn.gif'); background-size: cover;"  # Cloud animation
    elif weather_condition == "Rainy":
        bg_color = "#1E90FF"  # Blue
        effect = "background: url('https://i.gifer.com/3QE1.gif'); background-size: cover;"  # Rain animation
    elif weather_condition == "Windy":
        bg_color = "#87CEFA"  # Light blue
        effect = "background: url('https://i.gifer.com/2GU.gif'); background-size: cover;"  # Wind animation
    else:
        bg_color = "#F0F0F0"  # Default light gray
        effect = ""

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {bg_color};
            {effect}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ========== 📌 Streamlit App Layout ==========
st.set_page_config(page_title="Weather & Traffic Predictor", layout="wide")

# 🚦 LIVE WEATHER & TRAFFIC UPDATE
st.title("🌤️ Weather & Traffic Live Update 🚦")

# Fetch initial weather data
location = "Default City"  # Replace with user input
weather_data = get_weather_data(location)
set_background(weather_data["condition"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌦️ Current Weather")
    st.markdown(f"**Condition:** {weather_data['condition']}")  
    st.markdown(f"**Temperature:** {weather_data['temperature']}°C")  
    st.markdown(f"**Wind Speed:** {weather_data['wind_speed']} km/h")  
    st.markdown(f"**Precipitation:** {weather_data['precipitation']}%")  

with col2:
    st.subheader("🚦 Traffic Update")
    st.markdown(f"**Traffic Incidents:** {weather_data['traffic_incidents']}")  

# ========== 🗺️ User Inputs ==========
st.sidebar.title("📍 Travel Inputs")
travel_date = st.sidebar.date_input("Select Travel Date", datetime.date.today())
travel_time = st.sidebar.time_input("Select Travel Time", datetime.datetime.now().time())
travel_location = st.sidebar.text_input("Enter Location", "New York")

# ========== 📊 Interactive Weather Plot ==========
st.subheader("📊 Weather Trend Before Travel")

# Simulated weather data for past hours
time_range = pd.date_range(end=datetime.datetime.now(), periods=12, freq="H")
weather_df = pd.DataFrame({
    "Time": time_range,
    "Temperature": np.random.randint(5, 35, len(time_range)),
    "Wind Speed": np.random.randint(1, 30, len(time_range)),
    "Precipitation": np.random.randint(0, 100, len(time_range))
})
weather_df = weather_df.melt(id_vars=["Time"], var_name="Weather Variable", value_name="Value")

# Plot weather variables
fig = px.line(weather_df, x="Time", y="Value", color="Weather Variable", title="Weather Patterns Over Time")
st.plotly_chart(fig)

# ========== 🔍 Predict Weather & Traffic for User Input ==========
if st.sidebar.button("Get Forecast"):
    user_weather = get_weather_data(travel_location)
    set_background(user_weather["condition"])
    
    st.subheader(f"🌍 Forecast for {travel_location} on {travel_date} at {travel_time}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌦️ Predicted Weather")
        st.markdown(f"**Condition:** {user_weather['condition']}")  
        st.markdown(f"**Temperature:** {user_weather['temperature']}°C")  
        st.markdown(f"**Wind Speed:** {user_weather['wind_speed']} km/h")  
        st.markdown(f"**Precipitation:** {user_weather['precipitation']}%")  
    
    with col2:
        st.subheader("🚦 Traffic Prediction")
        st.markdown(f"**Traffic Incidents:** {user_weather['traffic_incidents']}")  

# ========== 🔗 Footer ==========
st.markdown("""
---
💡 *This is an interactive Weather & Traffic Forecasting app built using Streamlit.*  
Developed for a **Data Science Group Project** 🎯
""")
