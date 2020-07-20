import folium
import pandas
map = folium.Map(location=[38.58, -99.09], zoom_start=6)

df = pandas.read_csv("Volcanoes.txt")

lat = list(df["LAT"])
lon = list(df["LON"])
name = list(df["NAME"])
elev = list(df["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

fg1 = folium.FeatureGroup(name="Polygons")
fg2 = folium.FeatureGroup(name="Markers")

for lt, ln, nm, el in zip(lat, lon, name, elev) :
    fg2.add_child(folium.CircleMarker(location=[lt, ln], radius=6, fill=True, fill_color=color_producer(el), fill_opacity=0.7, popup=nm + "(" + str(el) + "m)"))


fg1.add_child(folium.GeoJson(data=open("115 world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map1.html")
