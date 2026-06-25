import altair as alt
import streamlit as st

from utils.statistics import (
    get_summary_stats
)
from utils.intelligence import (
    rainfall_status,
    rainfall_alert
)

def render_wettest_chart(df):

    top5 = (
        df.sort_values(
            "rainfall",
            ascending=False
        )
        .head(5)
    )

    chart = (
        alt.Chart(top5)
        .mark_bar()
        .encode(
            x=alt.X(
                "rainfall:Q",
                title="Rainfall (mm)"
            ),
            y=alt.Y(
                "province:N",
                sort="-x",
                title=None
            ),
            tooltip=[
                "province",
                "rainfall"
            ]
        )
        .properties(
            title="🏆 Top 5 Wettest Provinces",
            height=300
        )
    )

    st.altair_chart(
        chart,
        use_container_width=True
    )


def render_driest_chart(df):

    bottom5 = (
        df.sort_values(
            "rainfall",
            ascending=True
        )
        .head(5)
    )

    chart = (
        alt.Chart(bottom5)
        .mark_bar()
        .encode(
            x=alt.X(
                "rainfall:Q",
                title="Rainfall (mm)"
            ),
            y=alt.Y(
                "province:N",
                sort="x",
                title=None
            ),
            tooltip=[
                "province",
                "rainfall"
            ]
        )
        .properties(
            title="☀️ Top 5 Driest Provinces",
            height=300
        )
    )

    st.altair_chart(
        chart,
        use_container_width=True
    )


def render_category_chart(df):

    category_counts = (
        df["category"]
        .value_counts()
        .reset_index()
    )

    category_counts.columns = [
        "category",
        "count"
    ]

    chart = (
        alt.Chart(category_counts)
        .mark_bar()
        .encode(
            x=alt.X(
                "category:N",
                title="Category"
            ),
            y=alt.Y(
                "count:Q",
                title="Number of Provinces"
            ),
            tooltip=[
                "category",
                "count"
            ]
        )
        .properties(
            title="📊 Rainfall Category Distribution",
            height=300
        )
    )

    st.altair_chart(
        chart,
        use_container_width=True
    )

def render_national_summary(df):

    stats = get_summary_stats(df)

    wettest = (
        stats["wettest"]
        .iloc[0]
    )

    driest = stats["driest"]

    average = stats["average"]

    extreme_count = (
        df["category"]
        .str.contains(
            "Extreme",
            case=False
        )
        .sum()
    )

    high_count = (
        df["category"]
        .str.contains(
            "High",
            case=False
        )
        .sum()
    )

    status = rainfall_status(
        average
    )

    alert_active, alert_text = rainfall_alert(
        extreme_count
    )

    if alert_active:

        st.warning(
            alert_text
        )

    driest_list = ", ".join(
        driest["province"].tolist()
    )

    st.info(
        f"""
### 🧠 National Rainfall Summary

{status}

- Indonesia is currently recording an average accumulated rainfall of **{average} mm**.

- The highest rainfall today is observed in **{wettest['province']}** with **{wettest['rainfall']} mm**.

- The lowest rainfall recorded is **{stats['min_rainfall']} mm**, currently shared by **{len(driest)} provinces**: **{driest_list}**

- A total of **{high_count + extreme_count} provinces** are currently experiencing High to Extreme rainfall conditions.

- Provinces classified as Extreme: **{extreme_count}**
        """
    )
    
def render_top3_cards(df):

    top3 = df.head(3)

    st.subheader(
        "🥇 Rainfall Leaders Today"
    )

    col1, col2, col3 = st.columns(3)

    medals = [
        "🥇",
        "🥈",
        "🥉"
    ]

    columns = [
        col1,
        col2,
        col3
    ]

    for idx, (_, row) in enumerate(
        top3.iterrows()
    ):

        with columns[idx]:

            st.metric(
                f"{medals[idx]} {row['province']}",
                f"{row['rainfall']} mm"
            )