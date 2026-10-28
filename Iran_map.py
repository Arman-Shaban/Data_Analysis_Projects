import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely import geometry
from shapely.geometry import Point

path = "gadm41_IRN_shp/gadm41_IRN_0.shp"
iran = gpd.read_file(path)

cities = pd.DataFrame({
    "name": ['Tehran', 'Mashhad', 'Isfhan', 'Shiraz', 'Tabriz'],
    "lon": [51.389, 59.606, 51.667, 52.531, 46.299],
    "lat": [35.689, 36.297, 32.654, 29.591, 38.080]
    }
)

geometry = [Point(xy) for xy in zip(cities['lon'], cities['lat'])]
cities_gdf = gpd.GeoDataFrame(cities, geometry=geometry, crs="EPSG:4326")


fig, ax = plt.subplots(figsize=(10, 8))

iran.plot(ax=ax, color="#f0f0f0", markersize=50, zorder=5)

cities_gdf.plot(ax=ax, color="red", markersize=50, zorder=5)

for idx, row in cities_gdf.iterrows():
    ax.annotate(row["name"], (row["lon"], row["lat"]),
                textcoords="offset points", xytext=(5, 5),
                fontsize=9, color="darkred"
                )

ax.set_title("Map of Iran")
ax.set_xlabel("Longitude")
ax.set_ylabel('Latitude')
ax.set_aspect("equal")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()