# GeoData@SciLi Basic Geopandas Examples

This repo includes a Python 3 script and Jupyter Notebook that read in sample data from a shapefile and CSV to demonstrate basic geospatial operations with Geopandas. With [Geopandas](https://geopandas.org/en/stable/index.html), you can script and automate many operations that are commonly found in GIS software. 

Click the green Code button and choose Download ZIP to download the examples, or clone the repo if you're familiar with GitHub. If you just want to preview the content, click on the ipynb notebook file to view it.

## Prerequisites

1. Install Python 3 (either directly from [python.org](https://www.python.org/) or via a distribution like [Anaconda](https://www.anaconda.com/products/distribution))

2. If they are not already prepacked with your distribution, use pip install or your distribution's package handler to install the following modules: [Pandas](https://pandas.pydata.org/), [Geopandas](https://geopandas.org/en/stable/index.html), and [Shapely](https://pypi.org/project/shapely/)

3. Plotting coordinates and transforming projections requires familiarity with [EPSG codes](https://epsg.io/), which are unique identifiers for coordinate reference systems.

## Demonstrated Concepts

1. Read a shapefile into a geodataframe

2. Read a CSV with coordinate data into a geodataframe and convert the coordinates into point geometry

3. Obtain the coordinate reference system (CRS) from each file, and transform the map projection

4. Generate lines from point geometry based on point sequence and shared categories

5. Perform a spatial join between points and polygons, assigning each point the attributes of the polygon that it intersects

6. Create a basic plot with several layers

7. Export geodataframes out as shapefiles

