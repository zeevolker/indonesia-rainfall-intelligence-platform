import streamlit as st

from utils.national_intelligence import (
    compare_to_historical
)


def render_historical_context(
    current_df,
    historical_df
):

    result = (
        compare_to_historical(
            current_df,
            historical_df
        )
    )

    # st.subheader(
    #     "📈 Historical Context"
    # )

    st.info(
        f"""
### National Historical Comparison

{result['status']}

Current National Average:
{result['current_avg']} mm

Historical Average:
{result['historical_avg']} mm

Difference:
{result['diff_pct']}%
"""
    )