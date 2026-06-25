def get_monthly_rainfall(df):

    monthly = (
        df
        .set_index("date")
        .resample("ME")
        ["rainfall"]
        .sum()
        .reset_index()
    )

    monthly["month"] = (
        monthly["date"]
        .dt.strftime("%b %Y")
    )

    return monthly