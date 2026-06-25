import pandas as pd
import requests

import streamlit as st

from config.cache import FORECAST_CACHE

@st.cache_data(
    ttl=FORECAST_CACHE
)
def get_forecast(
    lat,
    lon,
    forecast_days=7
):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        "&daily=precipitation_sum"
        f"&forecast_days={forecast_days}"
        "&timezone=Asia%2FBangkok"
    )

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame({
        "date": data["daily"]["time"],
        "rainfall": data["daily"]["precipitation_sum"]
    })

    df["date"] = pd.to_datetime(
        df["date"]
    )

    return df