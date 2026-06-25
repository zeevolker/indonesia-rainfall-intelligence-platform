import altair as alt
import streamlit as st

from utils.monthly_statistics import (
    get_monthly_rainfall
)


def render_monthly_chart(
    df,
    is_mobile=False
):

    monthly_df = (
        get_monthly_rainfall(df)
    )

    chart = (
        alt.Chart(monthly_df)
        .mark_area(
            opacity=0.6,
            interpolate="monotone"
        )
        .encode(
            x=alt.X(
                "month:N",
                sort=None,
                title="Month"
            ),
            y=alt.Y(
                "rainfall:Q",
                title="Total Rainfall (mm)"
            ),
            tooltip=[
                alt.Tooltip(
                    "month:N",
                    title="Month"
                ),
                alt.Tooltip(
                    "rainfall:Q",
                    title="Total Rainfall",
                    format=".1f"
                )
            ]
        )
        .properties(
            title="Monthly Rainfall Seasonality",
            height=300 if is_mobile else 420
        )
    )

    st.altair_chart(
        chart,
        use_container_width=True
    )