import streamlit as st

from utils.national_intelligence import (
    calculate_intelligence_score
)


def render_intelligence_hero(df):

    score, status = (
        calculate_intelligence_score(
            df
        )
    )
    
    st.subheader(
        "🎯 National Intelligence Score"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "National Intelligence Score",
            f"{score}/100"
        )

    with col2:

        st.metric(
            "Current Status",
            status
        )