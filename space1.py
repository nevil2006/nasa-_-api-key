import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# CONFIG
st.set_page_config("🚀 NASA Space Dashboard", layout="wide")
st.title("🚀 NASA Space Dashboard")
API_KEY = "5rpiRdcYrp2GKVIrOhgv0BsMGxOkXr06hau241pv"

# Tabs
tab1, tab2, tab3 = st.tabs(["🪐 APOD", "☄️ Asteroids", "🛰️ ISS Tracker"])

# 🌌 Astronomy Picture of the Day (APOD)
with tab1:
    st.header("🪐 Astronomy Picture of the Day")
    selected_date = st.date_input("Select a date", datetime.today())
    apod_url = f"https://api.nasa.gov/planetary/apod?date={selected_date.strftime('%Y-%m-%d')}&api_key={API_KEY}"

    with st.spinner("Fetching Astronomy Picture of the Day..."):
        apod_data = requests.get(apod_url).json()

    media_type = apod_data.get("media_type", "")
    title = apod_data.get("title", "NASA Astronomy Picture of the Day")
    explanation = apod_data.get("explanation", "No explanation available.")

    if media_type == "image":
        st.image(apod_data["url"], caption=title, use_column_width=True)
    elif media_type == "video":
        st.video(apod_data["url"])
    else:
        st.warning("⚠️ The media type for this day is not supported for display.")
        st.write(f"**Title:** {title}")

    st.markdown(explanation)
    st.download_button("📥 Download Explanation", explanation, file_name=f"APOD_{selected_date}.txt")

# ☄️ Near Earth Asteroids
with tab2:
    st.header("☄️ Asteroids Near Earth")

    today = datetime.today().strftime('%Y-%m-%d')
    tomorrow = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    neo_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&end_date={tomorrow}&api_key={API_KEY}"

    with st.spinner("Fetching asteroid data..."):
        neo_data = requests.get(neo_url).json()

    asteroids = []
    for date in neo_data.get('near_earth_objects', {}):
        for obj in neo_data['near_earth_objects'][date]:
            asteroids.append({
                'Name': obj['name'],
                'Diameter (m)': obj['estimated_diameter']['meters']['estimated_diameter_max'],
                'Miss Distance (km)': float(obj['close_approach_data'][0]['miss_distance']['kilometers']),
                'Velocity (km/h)': float(obj['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']),
                'Date': date
            })

    df_asteroids = pd.DataFrame(asteroids)

    # Filter by diameter
    st.markdown("### 🔍 Filter by Diameter")
    min_dia = st.slider("Minimum Diameter (m)", 0.0, 1000.0, 0.0, 10.0)
    filtered_df = df_asteroids[df_asteroids["Diameter (m)"] > min_dia]

    st.dataframe(filtered_df)

    # Plotting
    fig = px.scatter(
        filtered_df,
        x="Miss Distance (km)",
        y="Velocity (km/h)",
        size="Diameter (m)",
        hover_name="Name",
        title="Asteroids Approaching Earth",
        size_max=40
    )
    st.plotly_chart(fig)

# 🛰️ ISS Current Location
with tab3:
    st.header("🛰️ Current ISS Location")

    with st.spinner("Fetching ISS location..."):
        iss_response = requests.get("http://api.open-notify.org/iss-now.json").json()
        lat = float(iss_response["iss_position"]["latitude"])
        lon = float(iss_response["iss_position"]["longitude"])

        df_iss = pd.DataFrame({'lat': [lat], 'lon': [lon]})
        st.map(df_iss, zoom=1)

    st.markdown(f"**Latitude:** {lat}  \n**Longitude:** {lon}")
