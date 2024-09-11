from shapely.geometry import Polygon, Point
import geopandas as gpd

area = Polygon(
    [
        (27.700236978687286, 85.27981369021475),
        (27.699743018012562, 85.33972350958649),
        (27.678006535283394, 85.28346149440286),
        (27.678918642504875, 85.33701984295296),
    ]
)

location = Point(27.68439112588477, 85.3070220179237)

gdf = gpd.GeoDataFrame({"geometry": [area]}, crs="EPSG:4326")

is_inside = area.contains(location)

print(f"Is the point inside the area? {is_inside}")
