import altair as alt
import streamlit as st

from config.theme import (
    PRIMARY,
    PRIMARY_LIGHT,
    LOW,
    MODERATE,
    HIGH,
    EXTREME
)

def render_forecast_chart(
    df,
    province,
    forecast_days,
    is_mobile=False
):

    forecast = df.copy()

    # Legend Category
    forecast["category"] = forecast["rainfall"].apply(
        lambda x:
            "Low (<2 mm)"
            if x < 2
            else "Moderate (2–5 mm)"
            if x < 5
            else "High (5–10 mm)"
            if x < 10
            else "Extreme (>10 mm)"
    )

    # Tooltip Category
    forecast["intensity"] = forecast["rainfall"].apply(
        lambda x:
            "Low"
            if x < 2
            else "Moderate"
            if x < 5
            else "High"
            if x < 10
            else "Extreme"
    )

    # Area
    area = (
        alt.Chart(forecast)
        .mark_area(
            color=PRIMARY_LIGHT,
            opacity=0.35
        )
        .encode(
            x=alt.X(
                "date:T",
                title="Date"
            ),
            y=alt.Y(
                "rainfall:Q",
                title="Forecast Rainfall (mm)"
            )
        )
    )

    # Line
    line = (
        alt.Chart(forecast)
        .mark_line(
            color=PRIMARY,
            strokeWidth=3
        )
        .encode(
            x="date:T",
            y="rainfall:Q"
        )
    )

    # Points
    points = (
        alt.Chart(forecast)
        .mark_circle(
            size=110
        )
        .encode(
            x="date:T",
            y="rainfall:Q",
            color=alt.Color(
                "category:N",
                title="Rainfall Intensity",
                scale=alt.Scale(
                    domain=[
                        "Low (<2 mm)",
                        "Moderate (2–5 mm)",
                        "High (5–10 mm)",
                        "Extreme (>10 mm)"
                    ],
                    range=[
                        LOW,
                        MODERATE,
                        HIGH,
                        EXTREME
                    ]
                ),
                legend=None
                if is_mobile
                else alt.Legend(
                    title="Rainfall Intensity"
                )
            ),
            tooltip=[
                alt.Tooltip(
                    "date:T",
                    title="Date"
                ),
                alt.Tooltip(
                    "rainfall:Q",
                    title="Forecast Rainfall",
                    format=".1f"
                ),
                alt.Tooltip(
                    "intensity:N",
                    title="Intensity"
                )
            ]
        )
    )

    chart = (
        area +
        line +
        points
    ).properties(
        title=f"{forecast_days}-Day Rainfall Forecast • {province}",
        height=300 if is_mobile else 420
    ).interactive()

    st.altair_chart(
        chart,
        use_container_width=True
    )

    # Mobile Legend
    if is_mobile:

        st.markdown(
            """
<div style="
display:flex;
justify-content:center;
align-items:center;
gap:16px;
margin-top:8px;
margin-bottom:4px;
font-size:0.82rem;
white-space:nowrap;
overflow-x:auto;
">

<span>🟢 Low</span>

<span>🟡 Moderate</span>

<span>🟠 High</span>

<span>🔴 Extreme</span>

</div>
""",
            unsafe_allow_html=True
        )