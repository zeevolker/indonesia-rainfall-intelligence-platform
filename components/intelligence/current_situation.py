import streamlit as st

from utils.national_intelligence import (
    get_current_situation
)


def render_current_situation(df):

    stats = (
        get_current_situation(df)
    )

    wettest = (
        stats["wettest"]
    )

    st.subheader(
        "🌧 Current Situation"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "National Average",
            f"{stats['average']} mm"
        )

    with col2:

        st.metric(
            "Above Average",
            stats["above_avg"]
        )

    with col3:

        st.metric(
            "Below Average",
            stats["below_avg"]
        )

    st.info(
        f"""
🌧 Highest rainfall activity is currently observed in
{wettest['province']}
with {wettest['rainfall']:.1f} mm.
"""
    )