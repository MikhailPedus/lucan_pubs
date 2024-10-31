# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:27:20 2024

@author: mihai
"""

import folium
import pandas as pd

# Загрузка данных из файла
data = pd.read_csv("C://pubs/pubs.csv")

# Определяем центр карты для Лукана, Ирландия
center_lat, center_lon = 53.3574, -6.4481
city_map = folium.Map(location=[center_lat, center_lon], zoom_start=13)

# Добавляем бары на карту
for _, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['name']} - Посещений: {row['visits']}",
        icon=folium.Icon(color="blue" if row['visits'] == 0 else "red")
    ).add_to(city_map)

# Сохраняем карту в HTML-файл
city_map.save("C://pubs/city_bars_map.html")