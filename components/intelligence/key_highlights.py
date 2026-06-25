import streamlit as st

from utils.national_intelligence import (
    get_key_highlights
)


def render_key_highlights(df):

    highlights = (
        get_key_highlights(df)
    )

    wettest = (
        highlights["wettest"]
    )

    driest = (
        highlights["driest"]
    )

    st.subheader(
        "📌 Key Highlights"
    )

    col1, col2, col3, col4 = (
        st.columns(4)
    )

    with col1:

        st.metric(
            "Wettest Province",
            wettest["province"]
        )

    with col2:

        st.metric(
            "Driest Province",
            driest["province"]
        )

    with col3:

        st.metric(
            "National Average",
            f"{highlights['average']} mm"
        )

    with col4:

        st.metric(
            "High Activity Provinces",
            highlights["high_count"]
        )