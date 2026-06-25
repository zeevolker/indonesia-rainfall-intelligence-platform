import streamlit as st


def render_feature_card(
    icon,
    title,
    description,
    features
):

    features_html = "<br>".join(
        [
            f"• {feature}"
            for feature in features
        ]
    )

    st.markdown(
        f"""
<div class="feature-card">

<div class="feature-title">
{icon} {title}
</div>

<div class="feature-description">
{description}
</div>

<div class="feature-list">
{features_html}
</div>

</div>
""",
        unsafe_allow_html=True
    )