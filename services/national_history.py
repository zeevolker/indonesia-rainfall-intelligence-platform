import pandas as pd

import streamlit as st

from services.nasa_power import (
    get_historical_rainfall
)

from utils.locations import (
    PROVINCES
)

from config.cache import (
    HISTORICAL_CACHE
)

@st.cache_data(
    ttl=HISTORICAL_CACHE
)
def get_national_historical_rainfall(
    start_date,
    end_date
):

    province_data = []

    total = len(
        PROVINCES
    )

    for province, (
        lat,
        lon
    ) in PROVINCES.items():

        try:

            df = (
                get_historical_rainfall(
                    lat,
                    lon,
                    start_date,
                    end_date
                )
            )

            province_data.append(
                df
            )

        except Exception:

            continue

    if not province_data:

        return pd.DataFrame(
            columns=[
                "date",
                "rainfall"
            ]
        )

    combined = pd.concat(
        province_data
    )

    national_df = (
        combined
        .groupby(
            "date",
            as_index=False
        )
        ["rainfall"]
        .mean()
    )

    return national_df