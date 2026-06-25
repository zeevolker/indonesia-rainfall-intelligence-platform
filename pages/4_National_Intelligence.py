import streamlit as st

from datetime import date

from utils.ui import (
    load_css,
    get_is_mobile
)

from services.national_live import (
    get_national_live_data
)

from components.intelligence.national_assessment import (
    render_assessment
)

from components.intelligence.current_situation import (
    render_current_situation
)

from components.intelligence.historical_context import (
    render_historical_context
)

from components.intelligence.key_highlights import (
    render_key_highlights
)

from services.national_history import (
    get_national_historical_rainfall
)

from components.intelligence.executive_summary import (
    render_executive_summary
)

from components.intelligence.intelligence_hero import (
    render_intelligence_hero
)

from components.shared.footer import (
    render_footer
)

from components.shared.loading import (
    create_status_loading,
    update_status_loading,
    finish_status_loading
)

from components.shared.page_header import (
    render_page_header
)

from services.national_forecast import (
    get_national_forecast
)

from components.intelligence.forecast_context import (
    render_forecast_context
)

from components.shared.documentation import (
    render_documentation
)

st.set_page_config(
    page_title="National Intelligence",
    layout="wide"
)
        
is_mobile = get_is_mobile(
    "INTEL_WIDTH"
)

load_css()

status = create_status_loading()

update_status_loading(
    status,
    "🔄 Collecting real-time rainfall data..."
)

df = get_national_live_data()

update_status_loading(
    status,
    "🧠 Analyzing rainfall patterns..."
)

current_year = (
    date.today().year - 1
)

historical_df = (
    get_national_historical_rainfall(
        f"{current_year}0101",
        f"{current_year}1231"
    )
)

forecast_df = (
    get_national_forecast()
)

finish_status_loading(
    status
)

render_page_header(
    title="🧠 National Rainfall Intelligence",
    subtitle="""
Integrated rainfall intelligence
across Indonesia.
"""
)

render_intelligence_hero(
    df
)

render_executive_summary(
    df,
    historical_df
)

render_assessment(
    df
)

render_current_situation(
    df
)

render_historical_context(
    df,
    historical_df
)

render_forecast_context(
    forecast_df
)

render_key_highlights(
    df
)

render_documentation(
    "intelligence"
)

render_footer(
    "Open-Meteo & NASA POWER"
)