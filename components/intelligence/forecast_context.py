import streamlit as st


def render_forecast_context(df):

    avg = df["rainfall"].mean()

    rainy_days = (
        df["rainfall"] > 0
    ).sum()

    wettest = df.loc[
        df["rainfall"].idxmax()
    ]

    if avg < 2:

        outlook = "Low"

    elif avg < 5:

        outlook = "Moderate"

    elif avg < 10:

        outlook = "High"

    else:

        outlook = "Extreme"

    st.subheader(
        "🔮 Forecast Outlook"
    )

    st.info(
        f"""
### Upcoming Rainfall

Average forecast rainfall is
**{avg:.1f} mm/day**.

Rain is expected on
**{rainy_days} day(s)**.

The highest rainfall is forecast on
**{wettest['date'].strftime('%A')}**
with **{wettest['rainfall']:.1f} mm**.

Overall outlook:
**{outlook} rainfall activity**.
"""
    )