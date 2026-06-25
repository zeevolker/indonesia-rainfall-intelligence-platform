import streamlit as st


def render_forecast_intelligence(df):

    total_days = len(df)

    rainy_days = (
        df["rainfall"] > 0
    ).sum()

    extreme_days = (
        df["rainfall"] >= 10
    ).sum()

    avg_rain = df["rainfall"].mean()

    trend = (
        "increasing"
        if df["rainfall"].iloc[-1]
        > df["rainfall"].iloc[0]
        else "decreasing"
    )

    if avg_rain < 2:

        risk = "Low"

        color = "🟢"

    elif avg_rain < 5:

        risk = "Moderate"

        color = "🟡"

    elif avg_rain < 10:

        risk = "High"

        color = "🟠"

    else:

        risk = "Extreme"

        color = "🔴"

    st.subheader(
        "🧠 Forecast Intelligence"
    )

    st.success(
        f"""
### National Forecast Assessment

• Rainfall is expected on **{rainy_days} of {total_days} forecast days**.

• The overall rainfall trend appears **{trend}** throughout the selected period.

• **{extreme_days} day(s)** are forecast to experience **extreme rainfall (≥10 mm)**.

• Overall rainfall risk is assessed as **{color} {risk}**.

### Recommendation

- Monitor weather updates during periods of heavier rainfall.
- Prepare for localized flooding if multiple consecutive high-rainfall days occur.
- Outdoor activities should be planned around the forecast trend.
"""
    )