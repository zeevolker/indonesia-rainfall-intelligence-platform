import requests

import pandas as pd

import streamlit as st

from config.cache import HISTORICAL_CACHE

@st.cache_data(
    ttl=HISTORICAL_CACHE
)
def get_historical_rainfall(
    lat,
    lon,
    start_date,
    end_date
):

    url = (
        "https://power.larc.nasa.gov/api/temporal/daily/point"
        f"?parameters=PRECTOTCORR"
        f"&community=AG"
        f"&longitude={lon}"
        f"&latitude={lat}"
        f"&start={start_date}"
        f"&end={end_date}"
        f"&format=JSON"
    )

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    rainfall = (
        data["properties"]
        ["parameter"]
        ["PRECTOTCORR"]
    )

    df = pd.DataFrame(
        rainfall.items(),
        columns=[
            "date",
            "rainfall"
        ]
    )

    df["date"] = pd.to_datetime(
        df["date"]
    )

    df = df[
        df["rainfall"] > -999
    ].copy()

    df = (
        df.sort_values(
            "date"
        )
        .reset_index(drop=True)
    )

    return df