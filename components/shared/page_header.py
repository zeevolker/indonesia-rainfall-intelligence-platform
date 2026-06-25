import streamlit as st


def render_page_header(
    title,
    subtitle,
    metadata=None
):
    """
    Render a consistent page header.

    Parameters
    ----------
    title : str
        Main page title.

    subtitle : str
        Short page description.

    metadata : str | None
        Optional metadata shown below subtitle.
    """

    st.title(
        title
    )

    st.caption(
        subtitle
    )

    if metadata:

        st.caption(
            metadata
        )
        
    st.divider()