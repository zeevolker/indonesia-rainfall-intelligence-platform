def generate_national_assessment(df):

    avg_rainfall = (
        df["rainfall"]
        .mean()
    )

    high_count = (
        df["rainfall"] >= 5
    ).sum()

    if avg_rainfall >= 10:

        status = (
            "🔴 High Rainfall Activity"
        )

    elif avg_rainfall >= 3:

        status = (
            "🟠 Moderate Rainfall Activity"
        )

    else:

        status = (
            "🟢 Low Rainfall Activity"
        )

    summary = (
        f"""
- National average rainfall is
{avg_rainfall:.1f} mm.

- {high_count} provinces are currently
recording elevated rainfall conditions.
"""
    )

    return (
        status,
        summary
    )

def get_key_highlights(df):

    wettest = df.loc[
        df["rainfall"].idxmax()
    ]

    driest = df.loc[
        df["rainfall"].idxmin()
    ]

    national_avg = round(
        df["rainfall"].mean(),
        1
    )

    high_count = (
        df["rainfall"] >= 5
    ).sum()

    return {
        "wettest": wettest,
        "driest": driest,
        "average": national_avg,
        "high_count": high_count
    }
    
def get_current_situation(df):

    avg_rainfall = round(
        df["rainfall"].mean(),
        1
    )

    above_avg = (
        df["rainfall"] > avg_rainfall
    ).sum()

    below_avg = (
        df["rainfall"] <= avg_rainfall
    ).sum()

    wettest = df.loc[
        df["rainfall"].idxmax()
    ]

    return {
        "average": avg_rainfall,
        "above_avg": above_avg,
        "below_avg": below_avg,
        "wettest": wettest
    }
    
def calculate_intelligence_score(df):

    avg_rainfall = (
        df["rainfall"]
        .mean()
    )

    high_count = (
        df["rainfall"] >= 5
    ).sum()

    extreme_count = (
        df["rainfall"] >= 10
    ).sum()

    score = (
        (avg_rainfall * 3)
        +
        (high_count * 2)
        +
        (extreme_count * 4)
    )

    score = min(
        round(score),
        100
    )

    if score >= 81:

        status = (
            "🔴 Extreme Activity"
        )

    elif score >= 61:

        status = (
            "🟠 High Activity"
        )

    elif score >= 31:

        status = (
            "🟡 Moderate Activity"
        )

    else:

        status = (
            "🟢 Low Activity"
        )

    return (
        score,
        status
    )
    
def compare_to_historical(
    current_df,
    historical_df
):

    current_avg = round(
        current_df["rainfall"].mean(),
        1
    )

    historical_avg = round(
        historical_df["rainfall"].mean(),
        1
    )

    if historical_avg == 0:

        diff_pct = 0

    else:

        diff_pct = round(
            (
                (
                    current_avg
                    - historical_avg
                )
                /
                historical_avg
            ) * 100,
            1
        )

    if diff_pct > 20:

        status = (
            "📈 Above Historical Average"
        )

    elif diff_pct < -20:

        status = (
            "📉 Below Historical Average"
        )

    else:

        status = (
            "➡️ Near Historical Average"
        )

    return {
        "current_avg": current_avg,
        "historical_avg": historical_avg,
        "diff_pct": diff_pct,
        "status": status
    }
    
def generate_executive_summary(
    df,
    historical_df
):

    score, status = (
        calculate_intelligence_score(
            df
        )
    )

    comparison = (
        compare_to_historical(
            df,
            historical_df
        )
    )

    wettest = df.loc[
        df["rainfall"].idxmax()
    ]

    driest = df.loc[
        df["rainfall"].idxmin()
    ]

    return f"""
### 📝 Executive Summary

Indonesia is currently experiencing
{status.replace('🟢','').replace('🟡','').replace('🟠','').replace('🔴','').lower()}.

The national intelligence score is
{score}/100.

Current rainfall conditions are
{comparison['status'].replace('📈','').replace('📉','').replace('➡️','').lower()}.

The wettest province today is
{wettest['province']}
({wettest['rainfall']:.1f} mm).

The driest province today is
{driest['province']}
({driest['rainfall']:.1f} mm).
"""