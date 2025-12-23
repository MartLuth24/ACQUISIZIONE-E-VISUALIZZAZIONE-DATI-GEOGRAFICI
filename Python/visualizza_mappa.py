import folium
import json
import os
from db_utils import get_traiettorie

# Centro mappa (Verona circa)
mappa = folium.Map(location=[45.4384, 10.9916], zoom_start=14)

traiettorie = get_traiettorie()

for sorgente, geojson_str in traiettorie:
    geojson = json.loads(geojson_str)

    folium.GeoJson(
        geojson,
        name=sorgente
    ).add_to(mappa)

mappa.save("mappa_traiettorie.html")
print("Mappa generata correttamente")

print("File creato in:", os.getcwd())
