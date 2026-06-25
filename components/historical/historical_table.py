import streamlit as st


def render_historical_table(
    df,
    province
):

    if province == "All Provinces":

        title = (
            "📊 National Historical Rainfall Dataset"
        )

    else:

        title = (
            f"📊 Historical Rainfall - {province}"
        )

    st.subheader(
        title
    )

    st.dataframe(
        df,
        use_container_width=True
    )