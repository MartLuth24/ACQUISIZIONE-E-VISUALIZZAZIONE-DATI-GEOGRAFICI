from video_analysis import analizza_video
from db_utils import insert_osservazione

VIDEO_FILE = "primo.mp4"
SORGENTE = "Camera_01"

# Coordinate geografiche di riferimento (telecamera)
lon_base = 10.99
lat_base = 45.43

risultati = analizza_video(VIDEO_FILE)

for r in risultati:
    # Simuliamo una conversione pixel → coordinate
    lon = lon_base + r["cx"] * 0.000001
    lat = lat_base + r["cy"] * 0.000001

    insert_osservazione(SORGENTE, lon, lat)

    print(
        f"Frame {r['frame']} → "
        f"pixel ({r['cx']},{r['cy']}) → "
        f"geo ({lon},{lat})"
    )
