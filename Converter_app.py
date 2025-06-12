import streamlit as st
import requests

st.title("💱 Currency Converter App")

from_currency = st.selectbox("From Currency", ["USD", "INR", "EUR", "GBP", "JPY"])
to_currency = st.selectbox("To Currency", ["USD", "INR", "EUR", "GBP", "JPY"])
amount = st.number_input("Enter amount", min_value=0.0, value=1.0)

if st.button("Convert"):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()
    result = data["rates"][to_currency]
    st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
