def rainfall_status_label(avg_rainfall):

    if avg_rainfall < 2:
        return "🟢 Low"

    elif avg_rainfall < 5:
        return "🟡 Moderate"

    elif avg_rainfall < 10:
        return "🟠 High"

    return "🔴 Extreme"


def rainfall_status(avg_rainfall):

    if avg_rainfall < 2:

        return (
            "- Rainfall activity remains low across most provinces today."
        )

    elif avg_rainfall < 5:

        return (
            "- Rainfall activity is moderate across Indonesia today."
        )

    elif avg_rainfall < 10:

        return (
            "- Several regions are experiencing significant rainfall activity today."
        )

    return (
        "- Widespread heavy rainfall is currently affecting multiple provinces."
    )


def rainfall_alert(extreme_count):

    if extreme_count >= 5:

        return (
            True,
            f"""
⚠️ Rainfall Alert

{extreme_count} provinces are currently
classified as Extreme rainfall conditions.
"""
        )

    return (
        False,
        ""
    )