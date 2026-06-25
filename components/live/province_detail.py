import streamlit as st


def render_province_detail(province_data):

    with st.container(border=True):

        st.subheader(
            "📍 Province Overview"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Province",
                province_data["province"]
            )

        with col2:

            st.metric(
                "Today's Rainfall",
                f"{province_data['rainfall']} mm"
            )

        with col3:

            st.metric(
                "Category",
                province_data["category"]
            )

        with col4:

            st.metric(
                "National Rank",
                f"#{province_data['rank']}"
            )