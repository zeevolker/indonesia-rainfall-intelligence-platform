import streamlit as st


def render_historical_kpis(df):

    avg_rainfall = round(
        df["rainfall"].mean(),
        2
    )

    max_rainfall = round(
        df["rainfall"].max(),
        2
    )

    total_rainfall = round(
        df["rainfall"].sum(),
        2
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Average Rainfall",
            f"{avg_rainfall} mm"
        )

    with col2:

        st.metric(
            "Maximum Daily Rainfall",
            f"{max_rainfall} mm"
        )

    with col3:

        st.metric(
            "Total Rainfall",
            f"{total_rainfall} mm"
        )