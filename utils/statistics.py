def get_summary_stats(df):

    avg_rainfall = round(
        df["rainfall"].mean(),
        2
    )

    max_rainfall = (
        df["rainfall"]
        .max()
    )

    min_rainfall = (
        df["rainfall"]
        .min()
    )

    wettest_provinces = df[
        df["rainfall"]
        == max_rainfall
    ]

    driest_provinces = df[
        df["rainfall"]
        == min_rainfall
    ]

    return {
        "average": avg_rainfall,
        "wettest": wettest_provinces,
        "driest": driest_provinces,
        "total_provinces": len(df),
        "max_rainfall": max_rainfall,
        "min_rainfall": min_rainfall
    }