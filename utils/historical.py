import pandas as pd


def monthly_rainfall(df):

    monthly = (
        df
        .set_index("date")
        .resample("ME")
        ["rainfall"]
        .mean()
        .reset_index()
    )

    return monthly