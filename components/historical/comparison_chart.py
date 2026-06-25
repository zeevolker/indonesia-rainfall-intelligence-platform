import altair as alt

import pandas as pd

import streamlit as st

def render_comparison_chart(
    df1,
    df2,
    province_1,
    province_2,
    is_mobile=False
):

    compare_df = pd.DataFrame({
        "date": df1["date"],
        province_1: df1["rainfall"],
        province_2: df2["rainfall"]
    })

    chart = (
        alt.Chart(
            compare_df
            .melt(
                "date",
                var_name="province",
                value_name="rainfall"
            )
        )
        .mark_line()
        .encode(
            x=alt.X(
                "date:T",
                title="Date"
            ),
            y=alt.Y(
                "rainfall:Q",
                title="Rainfall (mm)"
            ),
            color="province:N",
            tooltip=[
                "date",
                "province",
                "rainfall"
            ]
        )
        .properties(
            title="Province Rainfall Comparison",
            height=320 if is_mobile else 450
        )
    )

    st.altair_chart(
        chart,
        use_container_width=True
    )