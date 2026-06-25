from services.nasa_power import (
    get_historical_rainfall
)

from services.national_history import (
    get_national_historical_rainfall
)

from utils.locations import (
    PROVINCES
)


def load_history(
    province,
    start_date,
    end_date
):

    start = start_date.strftime(
        "%Y%m%d"
    )

    end = end_date.strftime(
        "%Y%m%d"
    )

    if province == "All Provinces":

        return (
            get_national_historical_rainfall(
                start,
                end
            )
        )

    lat, lon = PROVINCES[
        province
    ]

    return (
        get_historical_rainfall(
            lat,
            lon,
            start,
            end
        )
    )