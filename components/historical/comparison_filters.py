import streamlit as st

from utils.locations import (
    PROVINCES
)


def render_comparison_filters():

    provinces = sorted(
        PROVINCES.keys()
    )

    col1, col2 = st.columns(2)

    with col1:

        province_1 = st.selectbox(
            "Province A",
            provinces,
            key="province_a"
        )

    with col2:

        available = [
            p
            for p in provinces
            if p != province_1
        ]

        province_2 = st.selectbox(
            "Province B",
            available,
            key="province_b"
        )

    return (
        province_1,
        province_2
    )