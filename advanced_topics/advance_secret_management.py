import streamlit as st
import requests

# Access secrets
api_key = st.secrets["weather_api_key"]

# Use the secret to make an API request
def get_weather_data(api_key, city):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    return response.json()

city = st.text_input("Enter a city name", value="London")
if city:
    weather_data = get_weather_data(api_key, city)
    st.write(weather_data)
