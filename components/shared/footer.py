import streamlit as st


def render_footer(
    source
):

    st.divider()

    st.caption(
        f"""
Indonesia Rainfall Intelligence Platform •
Powered by {source}
"""
    )