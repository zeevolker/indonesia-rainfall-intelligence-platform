import streamlit as st

from utils.national_intelligence import (
    generate_executive_summary
)


def render_executive_summary(
    df,
    historical_df
):

    summary = (
        generate_executive_summary(
            df,
            historical_df
        )
    )

    st.info(
        summary
    )