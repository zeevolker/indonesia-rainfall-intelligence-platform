import streamlit as st

from utils.locations import (
    PROVINCES
)

from config.app import (
    FORECAST_OPTIONS,
    DEFAULT_FORECAST_DAYS
)

def render_forecast_filters():

    col1, col2 = st.columns(2)

    with col1:

        province = st.selectbox(
            "Province",
            sorted(
                PROVINCES.keys()
            )
        )

    with col2:

        forecast_days = st.selectbox(
            "Forecast Days",
            FORECAST_OPTIONS,
            index=FORECAST_OPTIONS.index(
                DEFAULT_FORECAST_DAYS
            )
        )

    return (
        province,
        forecast_days
    )