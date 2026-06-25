import streamlit as st


def render_forecast_table(df):

    forecast = df.copy()

    forecast["day"] = (
        forecast["date"]
        .dt.strftime("%a")
    )

    forecast["date"] = (
        forecast["date"]
        .dt.strftime("%d %b %Y")
    )

    def category(value):

        if value < 2:
            return "🟢 Low"

        if value < 5:
            return "🟡 Moderate"

        if value < 10:
            return "🟠 High"

        return "🔴 Extreme"

    def outlook(value):

        if value == 0:
            return "Dry"

        if value < 2:
            return "Light Rain"

        if value < 5:
            return "Moderate Rain"

        if value < 10:
            return "Heavy Rain"

        return "Extreme Rain"

    forecast["category"] = (
        forecast["rainfall"]
        .apply(category)
    )

    forecast["outlook"] = (
        forecast["rainfall"]
        .apply(outlook)
    )

    st.subheader(
        "📅 Forecast Outlook"
    )

    st.dataframe(
        forecast[
            [
                "date",
                "day",
                "rainfall",
                "category",
                "outlook"
            ]
        ],
        use_container_width=True,
        hide_index=True,
        column_config={
            "date": "Date",
            "day": "Day",
            "rainfall": st.column_config.NumberColumn(
                "Forecast (mm)",
                format="%.1f"
            ),
            "category": "Intensity",
            "outlook": "Expected Condition"
        }
    )