import streamlit as st
import requests

def get_weather(city_name):
    api_key = 'xx'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data


def main():
    st.title('Weather Dashboard')

    # Get user input for city name
    city_name = st.text_input('Enter City Name')

    # Display weather data when button is clicked
    if st.button('Get Weather'):
        weather_data = get_weather(city_name)
        if weather_data:
            st.write(f"**Location:** {weather_data['name']}, {weather_data['sys']['country']}")
            st.write(f"**Temperature:** {weather_data['main']['temp']}°C")
            st.write(f"**Weather:** {weather_data['weather'][0]['main']}")
            st.write(f"**Description:** {weather_data['weather'][0]['description']}")
            st.write(f"**Wind Speed:** {weather_data['wind']['speed']} m/s")
            st.write(f"**Humidity:** {weather_data['main']['humidity']}%")
        else:
            st.write('City not found. Please enter a valid city name.')


if __name__ == '__main__':
    main()
