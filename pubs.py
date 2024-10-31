# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:27:20 2024

@author: mihai
"""

import folium
import pandas as pd

data = pd.read_csv("C://pubs/pubs.csv")

center_lat, center_lon = 53.3574, -6.4481
city_map = folium.Map(location=[center_lat, center_lon], zoom_start=13)

for _, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['name']} - visits: {row['visits']}",
        icon=folium.Icon(color="blue" if row['visits'] == 0 else "red")
    ).add_to(city_map)

city_map.save("C://pubs/city_bars_map.html")