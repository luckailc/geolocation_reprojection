import pandas as pd
import geopandas

# Load DataFrame
df = pd.read_excel("dataset/NA_G.xlsx")

print(df.head())


# DATA FIX - Values that cannot be parsed as WKT:
# for index, row in df.iterrows():
#     try:
#         value = row["GEOMETRY"]
#         wkt.loads(value)
#     except Exception:
#         print(f'{index} [{len(value)}] {value!r}')


# Creating a GeoDataFrame from a DataFrame with coordinates - From WKT format
df["GEOMETRY"] = geopandas.GeoSeries.from_wkt(df["GEOMETRY"])

# Projection (MGI 1901 / Slovene National Grid, EPSG: 3912)
gdf = geopandas.GeoDataFrame(df, geometry="GEOMETRY", crs=3912)

gdf.dtypes
gdf.crs

# Reproject (Slovenia 1996 / Slovene National Grid, EPSG: 3794)
gdf_3794 = gdf.to_crs(epsg=3794)
gdf_3794.crs

# Save GeoDataFrame

gdf.to_file("results/geodataframe_3912.shp")
gdf.to_excel("results/geodataframe_3912.xlsx", index=False)

gdf_3794.to_file("results/geodataframe_3794.shp")
gdf_3794.to_excel("results/geodataframe_3794.xlsx", index=False)
