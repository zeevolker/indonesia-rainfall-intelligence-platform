DOCUMENTATION = {

    "live": {

        "methodology": """
### 🌧 Methodology

**Data Source**
- Open-Meteo Weather Forecast API

**Update Frequency**
- Near real-time (approximately every 5 minutes)

**Spatial Resolution**
- Province centroid coordinates

**Rainfall Measurement**
- Daily accumulated precipitation (mm)

**Analysis**
- National statistics are calculated from all Indonesian provinces.
""",

        "definitions": """
### ℹ Definitions

**Today's Rainfall**
Daily accumulated precipitation.

**National Average**
Average rainfall across all monitored provinces.

**Wettest Province**
Province with the highest rainfall.

**Driest Province**
Province with the lowest rainfall.

**Rainfall Category**
Low (<2 mm), Moderate (2–5 mm),
High (5–10 mm), Extreme (>10 mm).
"""
    },

    "historical": {

        "methodology": """
### 📈 Methodology

**Data Source**
- NASA POWER

**Dataset**
- PRECTOTCORR

**Temporal Resolution**
- Daily

**Analysis**
- Daily and monthly rainfall aggregation.

**Historical Coverage**
- Based on NASA POWER available archive.
""",

        "definitions": """
### ℹ Definitions

**Average Rainfall**
Mean daily rainfall.

**Maximum Daily Rainfall**
Highest daily precipitation.

**Total Rainfall**
Accumulated rainfall.

**Rainy Days**
Days with rainfall greater than 0 mm.
"""
    },

    "forecast": {

        "methodology": """
### 🔮 Methodology

**Data Source**
- Open-Meteo Forecast API

**Forecast Horizon**
- 3, 7 or 14 days

**Rainfall Variable**
- Daily precipitation forecast

**Analysis**
- Forecast statistics are calculated from predicted daily rainfall.
""",

        "definitions": """
### ℹ Definitions

**Expected Total Rainfall**
Accumulated forecast rainfall.

**Daily Average**
Mean forecast rainfall.

**Rainy Days**
Forecast days with rainfall greater than 0 mm.

**Rainfall Intensity**
Low (<2 mm), Moderate (2–5 mm),
High (5–10 mm), Extreme (>10 mm).
"""
    },

    "intelligence": {

        "methodology": """
### 🧠 Methodology

National Intelligence integrates:

• Live Monitoring

• Historical Analytics

• Forecast Analytics

All insights are generated using
rule-based statistical analysis.
""",

        "definitions": """
### ℹ Definitions

**Intelligence Score**
Overall national rainfall indicator.

**Current Situation**
Current rainfall conditions.

**Historical Context**
Comparison with historical observations.

**Forecast Outlook**
Expected rainfall conditions.

**Executive Summary**
Integrated rainfall assessment.
"""
    }

}