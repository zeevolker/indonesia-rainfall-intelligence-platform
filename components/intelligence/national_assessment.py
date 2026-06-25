import streamlit as st

from utils.national_intelligence import (
    generate_national_assessment
)


def render_assessment(df):

    status, summary = (
        generate_national_assessment(
            df
        )
    )

    st.info(
        f"""
### 🇮🇩 National Assessment

{status}

{summary}
"""
    )