def rainfall_category(value):

    if value < 1:
        return "🟢 Low"
    elif value < 5:
        return "🟡 Moderate"
    elif value < 10:
        return "🟠 High"
    else:
        return "🔴 Extreme"

RAINFALL_COLORS = {
    "low": "green",
    "moderate": "orange",
    "high": "red",
    "extreme": "darkred"
}

def rainfall_color(value):

    if value < 1:
        return RAINFALL_COLORS["low"]

    if value < 5:
        return RAINFALL_COLORS["moderate"]

    if value < 10:
        return RAINFALL_COLORS["high"]

    return RAINFALL_COLORS["extreme"]