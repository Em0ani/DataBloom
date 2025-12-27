import pandas as pd
import geopandas as gpd
from bokeh.io import show, output_notebook
from bokeh.models import (GeoJSONDataSource, LinearColorMapper, ColorBar, 
                          HoverTool, Select, CustomJS)
from bokeh.plotting import figure
from bokeh.palettes import OrRd9
from bokeh.layouts import column

def plot_interactive_choropleth(gdf, df, join_on, value_columns, title_prefix="Map"):
    """
    Creates an interactive choropleth map where users can switch 
    between data columns (e.g., candidates) via a dropdown.
    """
    # 1. Prepare Data
    # Merge geometries with data
    gdf_final = gdf.merge(df, on=join_on, how='left').fillna(0)
    
    # Remove datetime for JSON compatibility
    gdf_final = gdf_final.select_dtypes(exclude=['datetime64', 'datetime64[ns]'])
    
    # Calculate global maximums for the color scale
    max_values = {col: float(gdf_final[col].max()) for col in value_columns}
    initial_col = value_columns[0]
    
    geosource = GeoJSONDataSource(geojson=gdf_final.to_json())
    
    # 2. Setup Bokeh Figure
    color_mapper = LinearColorMapper(palette=OrRd9[::-1], low=0, high=max_values[initial_col])
    
    p = figure(title=f"{title_prefix}: {initial_col}", height=650, width=850,
               tools="pan,wheel_zoom,reset", toolbar_location="below")
    p.axis.visible = False
    p.grid.grid_line_color = None

    renderer = p.patches('xs', 'ys', source=geosource,
                         fill_color={'field': initial_col, 'transform': color_mapper},
                         line_color='black', line_width=0.5, fill_alpha=0.9)

    # 3. Tooltip
    hover = HoverTool(tooltips=[(join_on.capitalize(), f"@{join_on}"),
                                ("Value", f"@{{{initial_col}}}{{0,0}}")])
    p.add_tools(hover)

    # 4. JavaScript Interactivity
    callback = CustomJS(args=dict(source=geosource, renderer=renderer, 
                                  hover=hover, title=p.title, max_vals=max_values), 
    code="""
        const c = cb_obj.value;
        const new_max = max_vals[c];
        
        // Update data field
        renderer.glyph.fill_color.field = c;
        
        // Update Title
        title.text = "Visualizing: " + c;
        
        // Update Tooltip format
        hover.tooltips = [[ "Location", "@""" + join_on + """"], ["Value", "@{" + c + "}{0,0}"]];
        
        source.change.emit();
    """)

    # 5. Widget
    select = Select(title="Select Variable:", value=initial_col, options=value_columns)
    select.js_on_change('value', callback)
    
    return column(select, p)