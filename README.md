<p align="center">
  <img src="assets/logo2.png" alt="DataBloom Logo" width="300">
</p>

<h1 align="center">DataBloom</h1>

<p align="center">
  <strong>Transforming raw data into flourishing insights.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/Em0ani/DataBloom?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/stars/Em0ani/DataBloom?style=flat-square" alt="Stars">
  <img src="https://img.shields.io/github/issues/Em0ani/DataBloom?style=flat-square" alt="Issues">
  <img src="https://img.shields.io/github/languages/top/Em0ani/DataBloom?style=flat-square" alt="Top Language">
</p>

---

## 🌸 About DataBloom

**DataBloom** is a data processing and visualization library designed to help developers and data scientists cultivate meaningful patterns from chaotic datasets. Much like a bloom, this project focuses on growth, structure, and the organic beauty of well-organized information.

## ✨ Key Features

- 🚀 **Fast Processing:** Optimized pipelines for high-velocity data.
- 🗺️ **Interactive Geospatial Visuals:** Generate dynamic choropleth maps with automatic JavaScript callbacks and Bokeh integration.
- 🎨 **Elegant Design:** Create intuitive charts and graphs that represent growth.
- 🛠️ **Modular Design:** Easily plug in your own data sources and transformation logic.
- 📈 **Scalable:** Built to grow alongside your data needs.

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+**
- **Geopandas** (for spatial data)
- **Pandas** (for data manipulation)
- **Bokeh** (for interactive rendering)

### Installation

```bash
# Clone the repository
git clone https://github.com/Em0ani/DataBloom.git

# Navigate into the directory
cd DataBloom

# Install dependencies
pip install pandas geopandas bokeh
🗺️ Interactive Choropleth Maps

DataBloom now simplifies the creation of interactive maps. Instead of writing complex JavaScript callbacks manually, you can generate a professional dashboard for election results or demographic data with a single function call.

Example: Mauritania Election Results

This example shows how to visualize candidate performance across different regions (Moughataas) using the logic from our latest interactive module.

code
Python
download
content_copy
expand_less
import databloom as db
import geopandas as gpd
import pandas as pd
from bokeh.io import show, output_notebook

# 1. Load your geographic and electoral data
gdf = gpd.read_file("mrt_admbnda_adm2.shp")
df = pd.read_csv("results_elections_2024.csv")

# 2. Pivot the data so candidates appear as selectable columns
df_pivot = df.pivot(index='moughataa', columns='candidate', values='nb_votes').fillna(0)
candidates = df_pivot.columns.tolist()

# 3. Generate the interactive layout with DataBloom
# DataBloom handles the GeoJSON conversion and JavaScript logic internally
layout = db.plot_interactive_choropleth(
    gdf=gdf,
    df=df_pivot,
    join_on='moughataa',
    value_columns=candidates,
    title_prefix="Votes per Region -"
)
# 4. Show the bloom!
output_notebook()
show(layout)

```

## 🤝 Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

<p align="center">
Made with ☕ by <a href="https://github.com/Em0ani">Emani BABE</a>
</p>

