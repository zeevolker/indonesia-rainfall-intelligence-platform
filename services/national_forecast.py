import pandas as pd

from services.forecast_service import (
    get_forecast
)

from utils.locations import (
    PROVINCES
)


def get_national_forecast():

    dfs = []

    for lat, lon in PROVINCES.values():

        df = get_forecast(
            lat,
            lon,
            7
        )

        dfs.append(df)

    national = (
        pd.concat(dfs)
        .groupby("date")
        ["rainfall"]
        .mean()
        .reset_index()
    )

    return national