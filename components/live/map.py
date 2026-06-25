import folium

from streamlit_folium import st_folium

from utils.rainfall import rainfall_color

def get_color(rainfall):

    if rainfall < 1:
        return "green"

    elif rainfall < 5:
        return "orange"

    elif rainfall < 10:
        return "red"

    return "darkred"


def render_map(
    df,
    selected_province=None,
    is_mobile=False
):

    zoom = 3 if is_mobile else 5

    center = [-2.5, 118]

    if (
        selected_province
        and selected_province != "All Provinces"
    ):

        row = df[
            df["province"]
            == selected_province
        ].iloc[0]

        center = [
            row["lat"],
            row["lon"]
        ]

        zoom = 7

    m = folium.Map(
        location=center,
        zoom_start=zoom,
        tiles="CartoDB positron"
    )

    for _, row in df.iterrows():

        color = rainfall_color(
            row["rainfall"]
        )

        radius = max(
            6,
            min(
                18,
                row["rainfall"] * 2
            )
        )

        weight = 1.5

        if (
            selected_province != "All Provinces"
            and row["province"]
            == selected_province
        ):

            radius = 20
            weight = 3

            # Highlight ring
            folium.Circle(
                location=[
                    row["lat"],
                    row["lon"]
                ],
                radius=30000,
                color=color,
                weight=2,
                fill=True,
                fill_color=color,
                fill_opacity=0.08
            ).add_to(m)

        popup_html = f"""
        <div style="
            width:220px;
            padding:10px;
            font-family:Arial,sans-serif;
        ">

            <h4 style="
                margin-bottom:8px;
                color:#1976D2;
            ">
                {row['province']}
            </h4>

            <hr>

            <b>🌧 Today's Rainfall</b><br>
            {row['rainfall']} mm

            <br><br>

            <b>📊 Category</b><br>
            {row['category']}

            <br><br>

            <b>🏆 National Rank</b><br>
            #{row['rank']}

        </div>
        """

        folium.CircleMarker(
            location=[
                row["lat"],
                row["lon"]
            ],
            radius=radius,
            color=color,
            weight=weight,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            tooltip=folium.Tooltip(
                f"""
                <b>{row['province']}</b><br>
                Today's Rainfall: {row['rainfall']} mm
                """,
                sticky=True
            ),
            popup=folium.Popup(
                popup_html,
                max_width=250
            )
        ).add_to(m)

    legend_html = """
    <div style="
    position: fixed;
    bottom: 20px;
    left: 20px;
    z-index:9999;
    background:white;
    padding:12px;
    border-radius:12px;
    box-shadow:0 2px 12px rgba(0,0,0,.15);
    font-size:14px;
    min-width:180px;
    ">

        <b>🌧 Rainfall Category</b>

        <hr style="margin:8px 0">

        🟢 Low (< 1 mm)<br>

        🟠 Moderate (1 - 5 mm)<br>

        🔴 High (5 - 10 mm)<br>

        ⚫ Extreme (> 10 mm)

    </div>
    """

    m.get_root().html.add_child(
        folium.Element(
            legend_html
        )
    )

    st_folium(
        m,
        width=None,
        height = 450 if is_mobile else 650,
        use_container_width=True
    )