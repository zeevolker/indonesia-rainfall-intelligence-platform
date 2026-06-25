import requests
import streamlit as st

from config.cache import LIVE_CACHE

@st.cache_data(
    ttl=LIVE_CACHE
)
def get_rainfall(lat, lon):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        "&hourly=precipitation"
        "&forecast_days=1"
    )

    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    rainfall = sum(
        data["hourly"]["precipitation"]
    )

    return round(
        rainfall,
        2
    )