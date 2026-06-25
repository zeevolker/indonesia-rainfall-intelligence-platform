import streamlit as st


def render_forecast_kpis(df):

    total_rain = round(
        df["rainfall"].sum(),
        2
    )

    avg_rain = round(
        df["rainfall"].mean(),
        2
    )

    wettest_day = df.loc[
        df["rainfall"].idxmax()
    ]

    rainy_days = (
        df["rainfall"] > 0
    ).sum()

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Expected Total Rainfall",
            f"{total_rain} mm"
        )

    with col2:

        st.metric(
            "Daily Average",
            f"{avg_rain} mm"
        )

    with col3:

        st.metric(
            "Rainy Days",
            f"{rainy_days}/{len(df)}"
        )

    with col4:

        st.metric(
            "Wettest Forecast Day",
            wettest_day["date"].strftime(
                "%d %b"
            )
        )