import folium
import pandas as pd
import json
import webbrowser
import os
with open("kz.json") as f:
    geo_data = json.load(f)
data = {
    "region": ["Abai", "Akmola", "Aktobe", "Almaty", "Atyrau",
               "West Kazakhstan", "Jambyl", "Jetisu", "Karaganda",
               "Kostanay", "Kyzylorda", "Mangystau", "Pavlodar",
               "North Kazakhstan", "Turkestan", "Ulytau", "East Kazakhstan",
               "Astana", "Almaty (city)", "Shymkent (city)"],
    "population_2020": [622545, 736735, 881651, 1354232, 645280, 656844, 1130099, 701493,
                        1133659, 868549, 803531, 698796, 752169, 548755, 2016037, 218432,
                        736589, 1136156, 1916822, 1038152],
    "population_2021": [618945, 735566, 894333, 1378489, 657110, 661316, 1139192, 699478,
                        1133596, 864550, 814588, 719571, 751012, 543735, 2044742, 219875,
                        734567, 1184411, 1977258, 1074466],
    "population_2022": [611888, 785708, 916750, 1478496, 681241, 683327, 1209665, 698757,
                        1134966, 835686, 823251, 745909, 756511, 539111, 2088510, 220913,
                        732966, 1295711, 2101485, 1162308],
    "population_2023": [610198, 788013, 928159, 1505896, 693079, 688127, 1218158, 698726,
                        1134855, 832234, 833666, 767106, 754944, 534104, 2119226, 221421,
                        730238, 1354556, 2161902, 1192199],
    "population_2024": [607589, 787976, 939405, 1531167, 704074, 693261, 1222593, 697987,
                        1135351, 829984, 841929, 786837, 753933, 530089, 2142172, 221582,
                        727053, 1430117, 2228677, 1222066]
}
df = pd.DataFrame(data)
m = folium.Map(location=[43.222, 76.851], zoom_start=5)
folium.Choropleth(
    geo_data="kz.json",
    name="Population 2020",
    data=df,
    columns=["region", "population_2020"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population in 2020"
).add_to(m)
folium.Choropleth(
    geo_data="kz.json",
    name="Population 2021",
    data=df,
    columns=["region", "population_2021"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population in 2021"
).add_to(m)
folium.Choropleth(
    geo_data="kz.json",
    name="Population 2022",
    data=df,
    columns=["region", "population_2022"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population in 2022"
).add_to(m)
folium.Choropleth(
    geo_data="kz.json",
    name="Population 2023",
    data=df,
    columns=["region", "population_2023"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population in 2023"
).add_to(m)
folium.Choropleth(
    geo_data="kz.json",
    name="Population 2024",
    data=df,
    columns=["region", "population_2024"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population in 2024"
).add_to(m)
folium.LayerControl().add_to(m)
m.save("kazakhstan_population_map_2020_2024.html")
file_path = os.path.abspath('kazakhstan_population_map_2020_2024.html')
webbrowser.get(f'"C:/Program Files/Google/Chrome/Application/chrome.exe" %s').open(f'file://{file_path}')
