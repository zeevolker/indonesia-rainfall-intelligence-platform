import streamlit as st


def render_comparison_summary(
    df1,
    df2,
    province_1,
    province_2
):

    avg_1 = round(
        df1["rainfall"].mean(),
        2
    )

    avg_2 = round(
        df2["rainfall"].mean(),
        2
    )

    wetter = (
        province_1
        if avg_1 > avg_2
        else province_2
    )

    st.info(
        f"""
### 🆚 Province Comparison Summary

Average rainfall:

• {province_1}: {avg_1} mm

• {province_2}: {avg_2} mm

🌧 {wetter} recorded the higher average rainfall during the selected period.
"""
    )