import streamlit as st

from utils.ui import (
    load_css,
    get_is_mobile
)

from components.shared.page_header import (
    render_page_header
)

from components.shared.footer import (
    render_footer
)

from components.shared.loading import (
    spinner_loading
)

from components.forecast.filters import (
    render_forecast_filters
)

from services.forecast_service import (
    get_forecast
)

from utils.locations import (
    PROVINCES
)

from components.forecast.forecast_kpi import (
    render_forecast_kpis
)

from components.forecast.forecast_summary import (
    render_forecast_summary
)

from components.forecast.forecast_chart import (
    render_forecast_chart
)

from components.forecast.forecast_table import (
    render_forecast_table
)

from components.forecast.forecast_intelligence import (
    render_forecast_intelligence
)

from components.shared.documentation import (
    render_documentation
)

st.set_page_config(
    page_title="Forecast Analytics",
    layout="wide"
)

load_css()

is_mobile = get_is_mobile(
    "FORECAST_WIDTH"
)

render_page_header(
    title="🔮 Forecast Analytics",
    subtitle="Rainfall Forecast Across Indonesia"
)

province, forecast_days = (
    render_forecast_filters()
)

lat, lon = PROVINCES[
    province
]

with spinner_loading(
    "Loading rainfall forecast..."
):

    forecast_df = get_forecast(
        lat,
        lon,
        forecast_days
    )

st.subheader(
    "📊 Forecast Overview"
)

render_forecast_kpis(
    forecast_df
)

render_forecast_summary(
    forecast_df
)

render_forecast_intelligence(
    forecast_df
)

st.subheader(
    "📈 Forecast Trend"
)

render_forecast_chart(
    forecast_df,
    province,
    forecast_days,
    is_mobile
)

render_forecast_table(
    forecast_df
)

render_documentation(
    "forecast"
)

render_footer(
    "Open-Meteo Forecast API"
)