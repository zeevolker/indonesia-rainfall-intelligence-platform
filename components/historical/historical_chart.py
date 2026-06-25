import altair as alt
import streamlit as st

def render_historical_chart(
    df,
    is_mobile=False
):

    nearest = alt.selection_point(
        nearest=True,
        on="mouseover",
        fields=["date"],
        empty=False
    )

    line = (
        alt.Chart(df)
        .mark_line()
        .encode(
            x=alt.X(
                "date:T",
                title="Date"
            ),
            y=alt.Y(
                "rainfall:Q",
                title="Rainfall (mm)"
            )
        )
    )

    selectors = (
        alt.Chart(df)
        .mark_point()
        .encode(
            x="date:T",
            opacity=alt.value(0)
        )
        .add_params(nearest)
    )

    points = (
        line.mark_circle(size=70)
        .encode(
            opacity=alt.condition(
                nearest,
                alt.value(1),
                alt.value(0)
            )
        )
    )

    rules = (
        alt.Chart(df)
        .mark_rule()
        .encode(
            x="date:T"
        )
        .transform_filter(nearest)
    )

    tooltips = (
        alt.Chart(df)
        .mark_text(
            align="left",
            dx=8,
            dy=-8
        )
        .encode(
            x="date:T",
            y="rainfall:Q",
            text="rainfall:Q"
        )
        .transform_filter(nearest)
    )

    chart = (
        alt.layer(
            line,
            selectors,
            points,
            rules,
            tooltips
        )
        .properties(
            title="Daily Rainfall Trend",
            height=320 if is_mobile else 450
        )
    )

    st.altair_chart(
        chart,
        use_container_width=True
    )