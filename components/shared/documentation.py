import streamlit as st

from utils.documentation import (
    DOCUMENTATION
)


def render_documentation(page):

    docs = DOCUMENTATION[page]

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        with st.expander(
            "📖 Methodology"
        ):

            st.markdown(
                docs["methodology"]
            )

    with col2:

        with st.expander(
            "ℹ Definitions"
        ):

            st.markdown(
                docs["definitions"]
            )