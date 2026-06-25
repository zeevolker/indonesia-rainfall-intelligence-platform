import streamlit as st
from datetime import datetime

from utils.ui import (
    load_css,
    get_is_mobile
)

from services.nasa_power import (
    get_historical_rainfall
)
from utils.locations import (
    PROVINCES
)
from components.historical.historical_filters import (
    render_historical_filters
)
from components.historical.historical_kpi import (
    render_historical_kpis
)
from components.historical.historical_chart import (
    render_historical_chart
)
from components.historical.historical_table import (
    render_historical_table
)
from components.historical.historical_summary import (
    render_historical_summary
)
from components.historical.monthly_chart import (
    render_monthly_chart
)
from components.historical.comparison_filters import (
    render_comparison_filters
)

from components.historical.comparison_chart import (
    render_comparison_chart
)

from components.historical.comparison_summary import (
    render_comparison_summary
)

from utils.nasa_utils import (
    get_last_available_date
)

last_available = (
    get_last_available_date()
)

from services.national_history import (
    get_national_historical_rainfall
)

from components.shared.footer import (
    render_footer
)

from components.shared.loading import (
    spinner_loading
)

from services.historical_service import (
    load_history
)

from components.shared.page_header import (
    render_page_header
)

from components.shared.documentation import (
    render_documentation
)

st.set_page_config(
    page_title="Historical Analytics",
    layout="wide"
)

is_mobile = get_is_mobile(
    "HISTORY_WIDTH"
)

load_css()

render_page_header(
    title="📈 Historical Rainfall Analytics",
    subtitle="Historical Rainfall Intelligence Across Indonesia",
    metadata=f"""
Data Source: NASA POWER •
Historical Coverage Until:
{last_available.strftime('%d %B %Y')}
"""
)

province, start_date, end_date = (
    render_historical_filters()
)

with spinner_loading(
    "Retrieving historical rainfall data..."
):

    history_df = load_history(
        province,
        start_date,
        end_date
    )

st.subheader(
    "📊 Historical Overview"
)
render_historical_kpis(
    history_df
)

render_historical_summary(
    history_df
)

st.subheader(
    "📈 Historical Analytics"
)

render_historical_chart(
    history_df,
    is_mobile
)

render_monthly_chart(
    history_df,
    is_mobile
)

st.divider()



st.subheader(
    "🆚 Province Comparison"
)

province_1, province_2 = (
        render_comparison_filters()
    )

lat1, lon1 = PROVINCES[
    province_1
]

lat2, lon2 = PROVINCES[
    province_2
]

df1 = load_history(
    province_1,
    start_date,
    end_date
)

df2 = load_history(
    province_2,
    start_date,
    end_date
)

render_comparison_chart(
    df1,
    df2,
    province_1,
    province_2,
    is_mobile
)
    
render_comparison_summary(
    df1,
    df2,
    province_1,
    province_2
)


with st.expander(
    f"📊 View Historical Dataset ({len(history_df):,} Records)"
):

    render_historical_table(
        history_df,
        province
    )
    
render_documentation(
    "historical"
)
    
render_footer(
    "NASA POWER"
)