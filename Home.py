import streamlit as st

from utils.ui import (
    load_css,
    get_is_mobile
)

from components.shared.feature_card import (
    render_feature_card
)

from components.shared.footer import (
    render_footer
)

from components.shared.page_header import (
    render_page_header
)

st.set_page_config(
    page_title="Indonesia Rainfall Intelligence Platform",
    layout="wide"
)
        
is_mobile = get_is_mobile(
    "HOME_WIDTH"
)

load_css()

render_page_header(
    title="🌧 Indonesia Rainfall Intelligence Platform",
    subtitle="""
Real-time monitoring,
historical analytics,
and national rainfall intelligence.
"""
)

st.subheader(
    "📊 Platform Overview"
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Provinces Covered",
        "38"
    )

with col2:

    st.metric(
        "Data Sources",
        "2"
    )

with col3:

    st.metric(
        "Core Modules",
        "3"
    )

with col4:

    st.metric(
        "Update Frequency",
        "5 Min"
    )
    
st.divider()

st.subheader(
    "🚀 Available Modules"
)

col1, col2, col3 = st.columns(3)

with col1:

    render_feature_card(
        "🌧",
        "Live Monitoring",
        "Monitor rainfall conditions across Indonesia using real-time Open-Meteo data.",
        [
            "National KPI",
            "Interactive Map",
            "Province Ranking",
            "Rainfall Analytics"
        ]
    )

with col2:

    render_feature_card(
        "📈",
        "Historical Analytics",
        "Analyze historical rainfall patterns using NASA POWER.",
        [
            "Historical KPI",
            "Daily Trend",
            "Monthly Trend",
            "Province Comparison"
        ]
    )

with col3:

    render_feature_card(
        "🧠",
        "National Intelligence",
        "Transform rainfall data into actionable insights.",
        [
            "Intelligence Score",
            "Executive Summary",
            "National Assessment",
            "Key Highlights"
        ]
    )
    
st.divider()

st.subheader(
    "🛰 Data Sources"
)

col1, col2 = st.columns(2)

with col1:

    st.success(
        """
### Open-Meteo

Used for real-time rainfall
monitoring across Indonesia.

Update Frequency:
Every 5 minutes.
"""
    )

with col2:

    st.success(
        """
### NASA POWER

Used for historical rainfall
analysis and climatology.

Coverage:
Multi-year archive.
"""
    )
    
st.divider()

st.subheader(
    "🎯 Platform Vision"
)

st.info(
    """
Indonesia Rainfall Intelligence Platform
integrates real-time monitoring,
historical analytics, and national
rainfall intelligence into a single
decision-support platform.
"""
)

render_footer(
    "Open-Meteo & NASA POWER"
)