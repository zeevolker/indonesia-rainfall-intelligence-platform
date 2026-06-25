import streamlit as st

from streamlit_js_eval import (
    streamlit_js_eval
)


def load_css():

    with open(
        "assets/styles.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


def get_is_mobile(
    key
):

    screen_width = streamlit_js_eval(
        js_expressions="window.innerWidth",
        key=key
    )

    return (
        screen_width is not None
        and screen_width < 768
    )