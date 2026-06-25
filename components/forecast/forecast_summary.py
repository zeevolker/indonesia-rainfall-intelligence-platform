import streamlit as st


def render_forecast_summary(df):

    total_days = len(df)

    rainy_days = (
        df["rainfall"] > 0
    ).sum()

    dry_days = total_days - rainy_days

    avg_rain = round(
        df["rainfall"].mean(),
        1
    )

    wettest_day = df.loc[
        df["rainfall"].idxmax()
    ]

    highest = wettest_day["rainfall"]

    if avg_rain < 2:

        activity = "Low"

    elif avg_rain < 5:

        activity = "Moderate"

    elif avg_rain < 10:

        activity = "High"

    else:

        activity = "Extreme"

    st.info(
        f"""
### 📖 Forecast Summary

Forecast rainfall activity is expected to remain **{activity.lower()}**
over the next **{total_days} days**.

Rain is forecast on **{rainy_days}** day(s),
while **{dry_days}** day(s) are expected to remain dry.

The highest rainfall is expected on
**{wettest_day['date'].strftime('%A, %d %B')}**
with approximately **{highest:.1f} mm** of precipitation.

The average daily rainfall during this forecast period
is projected to reach **{avg_rain:.1f} mm/day**.
"""
    )