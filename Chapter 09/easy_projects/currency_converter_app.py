import requests
import streamlit as st

def convert_currency(amount, from_currency, to_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    data = response.json()
    if data['result'] == 'success':
        return data['conversion_result']
    else:
        return "Error: " + data['error-type']

st.title("Currency Converter")

api_key = 'xxx'

amount = st.text_input("Amount to convert", "1")
from_currency = st.text_input("From Currency (e.g., USD)", "USD")
to_currency = st.text_input("To Currency (e.g., EUR)", "EUR")

if st.button('Convert'):

    result = convert_currency(amount, from_currency.upper(), to_currency.upper(), api_key)
    if isinstance(result, str) and result.startswith("Error"):
        st.error(result)
    else:
        st.success(f"{amount} {from_currency} is {result} {to_currency}")
