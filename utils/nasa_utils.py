from datetime import (
    date,
    timedelta
)


def get_last_available_date():

    return (
        date.today()
        - timedelta(days=2)
    )