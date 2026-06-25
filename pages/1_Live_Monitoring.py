import pandas as pd
import streamlit as st

from datetime import datetime

from streamlit_autorefresh import st_autorefresh

from utils.ui import (
    load_css,
    get_is_mobile
)

from services.openmeteo import get_rainfall
from utils.locations import PROVINCES

from components.live.kpi import render_kpis
from components.live.map import render_map
from utils.rainfall import (
    rainfall_category
)
from components.live.province_detail import (
    render_province_detail
)
from components.live.leaderboard import (
    render_leaderboard
)
from components.live.charts import (
    render_top3_cards,
    render_national_summary,
    render_wettest_chart,
    render_driest_chart,
    render_category_chart
)

from components.shared.footer import (
    render_footer
)

from components.shared.loading import (
    create_progress_loading,
    update_progress_loading,
    finish_progress_loading
)

from components.shared.page_header import (
    render_page_header
)

from components.shared.documentation import (
    render_documentation
)

st.set_page_config(
    page_title="Indonesia Rainfall Intelligence Platform",
    layout="wide"
)

is_mobile = get_is_mobile(
    "LIVE_WIDTH"
)

load_css()

#####################
# Auto refresh 5 menit
st_autorefresh(
    interval=300000,
    key="refresh"
)

#####################
render_page_header(
    title="🌧️ Indonesia Rainfall Intelligence Platform",
    subtitle="Real-Time Rainfall Monitoring Across Indonesia",
    metadata=f"Last Updated: {datetime.now().strftime('%d %B %Y %H:%M:%S')}"
)

data = []

###################
progress, status = (
    create_progress_loading()
)

with st.spinner("Loading rainfall data..."):

    total = len(PROVINCES)

    for i, (province, coords) in enumerate(
        PROVINCES.items()
    ):

        update_progress_loading(
            progress,
            status,
            i + 1,
            total,
            province
        )

        lat, lon = coords

        rain = get_rainfall(
            lat,
            lon
        )

        data.append({
            "province": province,
            "lat": lat,
            "lon": lon,
            "rainfall": rain
        })
        
finish_progress_loading(
    progress,
    status
)

df = pd.DataFrame(data)

df["category"] = (
    df["rainfall"]
    .apply(rainfall_category)
)

df = (
    df.sort_values(
        "rainfall",
        ascending=False
    )
    .reset_index(drop=True)
)

df["rank"] = (
    df.index + 1
)
#####################
render_kpis(df)
#####################
render_top3_cards(df)
#####################
render_national_summary(df)
#####################
st.info(
    """
    🌧 Dashboard displays today's accumulated precipitation
    across Indonesian provinces based on Open-Meteo data.
    Values are refreshed every 5 minutes.
    """
)
#####################
st.subheader(
    "🔍 Province Search"
)

province_options = [
    "All Provinces"
] + sorted(
    df["province"].tolist()
)

selected_province = st.selectbox(
    "Select Province",
    province_options
)

if selected_province == "All Provinces":

    st.info(
        "📍 Showing rainfall conditions across all Indonesian provinces."
    )

else:

    province_data = df[
        df["province"]
        == selected_province
    ].iloc[0]

    render_province_detail(
        province_data
    )

st.divider()
#####################
render_map(
    df,
    selected_province,
    is_mobile
)

st.divider()
#####################
st.subheader(
    "📈 Rainfall Analytics"
)

col1, col2 = st.columns(2)

with col1:
    render_wettest_chart(df)

with col2:
    render_driest_chart(df)


render_category_chart(df)

render_leaderboard(
    df,
    datetime.now()
)

render_documentation(
    "live"
)

render_footer(
    "Open-Meteo"
)