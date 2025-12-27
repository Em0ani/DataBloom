import databloom as db
import pandas as pd
import geopandas as gpd

# 1. Load data
gdf = gpd.read_file("your_shapefile.shp").rename(columns={"ADM2_EN": "moughataa"})
df = pd.read_csv("results.csv")

# 2. Pivot data (standard pandas)
df_pivot = df[df['year']==2024].pivot(index='moughataa', columns='candidate', values='nb_votes').fillna(0)
candidates = df_pivot.columns.tolist()

# 3. Use your new DataBloom function
map_layout = db.plot_interactive_choropleth(
    gdf=gdf, 
    df=df_pivot, 
    join_on='moughataa', 
    value_columns=candidates,
    title_prefix="Votes par Moughataa"
)

db.show(map_layout)