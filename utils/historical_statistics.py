def get_historical_stats(df):

    wettest_day = df.loc[
        df["rainfall"].idxmax()
    ]

    driest_day = df.loc[
        df["rainfall"].idxmin()
    ]

    first_half = (
        df.head(
            len(df) // 2
        )["rainfall"]
        .mean()
    )

    second_half = (
        df.tail(
            len(df) // 2
        )["rainfall"]
        .mean()
    )

    if second_half > first_half:

        trend = "📈 Increasing"

    elif second_half < first_half:

        trend = "📉 Decreasing"

    else:

        trend = "➡️ Stable"

    return {
        "wettest_day": wettest_day,
        "driest_day": driest_day,
        "trend": trend
    }