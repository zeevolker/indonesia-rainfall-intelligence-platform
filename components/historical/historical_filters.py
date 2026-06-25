import streamlit as st

from datetime import (
    date,
    timedelta
)

from utils.locations import (
    PROVINCES
)

from utils.nasa_utils import (
    get_last_available_date
)

last_available = (
    get_last_available_date()
)

default_start_date = (
    date.today()
    - timedelta(days=365)
)


def render_historical_filters():

    province_options = [
        "All Provinces"
    ] + sorted(
        PROVINCES.keys()
    )

    province = st.selectbox(
        "Province",
        province_options
    )

    col1, col2 = st.columns(2)

    with col1:

        start_date = st.date_input(
            "Start Date",
            default_start_date
        )

    with col2:

        end_date = st.date_input(
            "End Date",
            last_available,
            max_value=last_available
        )

    if start_date > end_date:

        st.error(
            "Start Date must be earlier than End Date."
        )

        st.stop()

    return (
        province,
        start_date,
        end_date
    )