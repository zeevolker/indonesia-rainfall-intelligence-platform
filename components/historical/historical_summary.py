import streamlit as st

from utils.historical_statistics import (
    get_historical_stats
)


def render_historical_summary(df):

    stats = get_historical_stats(
        df
    )

    wettest = (
        stats["wettest_day"]
    )

    driest = (
        stats["driest_day"]
    )

    st.info(
        f"""
### 🧠 Historical Summary

🌧 Wettest day:

- {wettest['date'].strftime('%d %b %Y')} ({wettest['rainfall']:.2f} mm)

☀️ Driest day:

- {driest['date'].strftime('%d %b %Y')} ({driest['rainfall']:.2f} mm)

{stats['trend']} rainfall trend over the selected period.
        """
    )