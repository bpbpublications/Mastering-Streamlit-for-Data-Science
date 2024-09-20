import pydeck as pdk
import streamlit as st
import pandas as pd
import numpy as np

# Generating some random data points
np.random.seed(42)
data = pd.DataFrame({
    'lat': np.random.normal(37.76, 0.05, 1000),
    'lon': np.random.normal(-122.4, 0.05, 1000)
})

# Define a layer to display on a map
layer = pdk.Layer(
    "HexagonLayer",
    data,
    get_position=['lon', 'lat'],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1
)

# Set the viewport location
view_state = pdk.ViewState(
    latitude=37.76,
    longitude=-122.4,
    zoom=11,
    pitch=40
)

# Render the deck.gl map in Streamlit
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
