#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic Geopandas Examples
https://geopandas.org/en/stable/index.html

Frank Donnelly
Head of GIS & Data Services, Brown University Library
Dec 11, 2024
"""

import os, pandas as pd
import geopandas as gpd
from shapely.geometry import LineString
import matplotlib.pyplot as plt

# READ INPUT AND CREATE GEOMETRY FROM POINTS
# (Must know and plot the CRS of points as is; CRS is referenced using EPSG codes: 
# https://epsg.io/. 4269 is NAD 83, often used by US federal govt. The most 
# common long / lat CRS is 4326, WGS 84)

point_file=os.path.join('input','test_points.csv')
county_file=os.path.join('input','ri_county_bndy.shp')

gdf_cnty=gpd.read_file(county_file)
print(gdf_cnty.head)

df_pnts=pd.read_csv(point_file, index_col='OBS_NUM', delimiter=',',dtype={'GEOID':str})
gdf_pnts = gpd.GeoDataFrame(df_pnts,geometry=gpd.points_from_xy(
    df_pnts['INTPTLONG'],df_pnts['INTPTLAT']),crs = 'EPSG:4269')
print(gdf_pnts.head)

# GET CRS INFO AND TRANSFORM
# (3438 is the EPSG for for the RI State Plane Zone)

print('County CRS',gdf_cnty.crs)
print('County bbox',gdf_cnty.total_bounds)
print('Point CRS', gdf_pnts.crs)
print('Point bbox',gdf_pnts.total_bounds)

gdf_pnts.to_crs(3438,inplace=True)

print('New point CRS',gdf_pnts.crs)
print('New point bbox',gdf_pnts.total_bounds)

# GENERATE LINES FROM POINTS GROUPED BY CATEGORIES AND CALCULATE LENGTH
# (assumes points are in proper sequence; if not, sort by sequence column first)
# (output measurement units are based on the CRS)

lines = gdf_pnts.groupby('GROUP')['geometry'].apply(lambda x: LineString(x.tolist()))
gdf_lines = gpd.GeoDataFrame(lines, geometry='geometry',crs = 'EPSG:3438').reset_index()
gdf_lines['length_mi']=(gdf_lines.length)/5280
print(gdf_lines.loc[:,['GROUP','length_mi']].head)

# SPATIAL JOIN POINTS AND POLYGONS
# (keep all points on left, null values for non-matching counties on right)
# (take subset of columns from right, must always include geom for spatial joins)

gdf_pnts_wcnty=gpd.sjoin(gdf_pnts, gdf_cnty[['geoid','namelsad','geometry']],
                         how='left', predicate='intersects')
gdf_pnts_wcnty.rename(columns={'geoid': 'COUNTY_ID', 'namelsad': 'COUNTY'}, inplace=True)
print(gdf_pnts_wcnty.loc[:,['OBS_NAME','OBS_DATE','COUNTY']].head)

# PLOT

fig, ax = plt.subplots()
gdf_cnty.plot(ax=ax, color='yellow', edgecolor='grey')
gdf_pnts.plot(ax=ax,color='black', markersize=5)
gdf_lines.plot(ax=ax, column="GROUP", legend=True)

# WRITE OUTPUT
# (shapefile format cannot handle column names > 10 characters)

out_points=os.path.join('output','test_points_counties.shp')
out_lines=os.path.join('output','test_lines.shp')

gdf_pnts_wcnty.to_file(out_points)
gdf_lines.to_file(out_lines)
