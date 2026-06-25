import streamlit as st

from utils.intelligence import (
    rainfall_status_label
)

from utils.statistics import (
    get_summary_stats
)

def render_kpis(df):

    stats = get_summary_stats(df)

    wettest = (
        stats["wettest"]
        .iloc[0]
    )

    driest_count = len(
        stats["driest"]
    )

    status = rainfall_status_label(
        stats["average"]
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        st.metric(
            "Today's Avg Rainfall",
            f"{stats['average']} mm"
        )

    with col2:

        st.metric(
            "Wettest Province",
            wettest["province"]
        )

    with col3:

        st.metric(
            "Driest Provinces",
            f"{driest_count}"
        )

    with col4:

        st.metric(
            "Total Provinces",
            stats["total_provinces"]
        )

    with col5:

        
        st.metric(
            "National Status",
            status
        )