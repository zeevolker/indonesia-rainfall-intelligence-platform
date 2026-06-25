import streamlit as st


def render_leaderboard(
    df,
    update_time
):

    leaderboard = (
        df[
            [
                "rank",
                "province",
                "rainfall",
                "category"
            ]
        ]
        .copy()
    )

    st.subheader(
        "🏆 National Rainfall Ranking"
    )

    st.caption(
        f"Data refreshed: {update_time.strftime('%d %b %Y %H:%M:%S')}"
    )

    st.dataframe(
        leaderboard,
        use_container_width=True,
        hide_index=True,
        column_config={
            "rank": st.column_config.NumberColumn(
                "Rank",
                width="small"
            ),
            "province": st.column_config.TextColumn(
                "Province"
            ),
            "rainfall": st.column_config.NumberColumn(
                "Today's Rainfall (mm)",
                format="%.1f"
            ),
            "category": st.column_config.TextColumn(
                "Category"
            ),
        }
    )