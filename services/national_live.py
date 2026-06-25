import pandas as pd

from services.openmeteo import (
    get_rainfall
)

from utils.locations import (
    PROVINCES
)


def get_national_live_data():

    data = []

    for province, (
        lat,
        lon
    ) in PROVINCES.items():

        rain = get_rainfall(
            lat,
            lon
        )

        data.append({
            "province": province,
            "rainfall": rain
        })

    return pd.DataFrame(
        data
    )