import streamlit as st

from contextlib import contextmanager


# ==========================
# Progress Loading
# ==========================

def create_progress_loading():

    progress = st.progress(0)

    status = st.empty()

    return (
        progress,
        status
    )


def update_progress_loading(
    progress,
    status,
    current,
    total,
    item
):

    progress.progress(
        current / total
    )

    status.caption(
        f"Processing {current}/{total} • {item}"
    )


def finish_progress_loading(
    progress,
    status
):

    progress.empty()

    status.empty()


# ==========================
# Spinner Loading
# ==========================

@contextmanager
def spinner_loading(message):

    with st.spinner(message):

        yield


# ==========================
# Status Loading
# ==========================

def create_status_loading():

    return st.empty()


def update_status_loading(
    status,
    message
):

    status.info(message)


def finish_status_loading(
    status
):

    status.empty()