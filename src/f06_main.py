#This is the main script for the project TEP4221
# -*- coding: utf-8 -*-
# Authors: Taohong Liao
# Date: 2022.10.25
# Updated: 2022.10.31
# *** File purpose ***#
""" Aim: The aim is to compare enviormental impact of locations looking at salmon lice data and sedimentation analysis data. 
And after that comparing inbetween different locations, companies and regions, to find out if they could be used as a factor 
for "trafikklyssystemet".
"""



# *** Importing Packages ***#
# *** Define parameters ***#
# *** Defining Functions ***#
# *** Load Data ***#
# *** Manipulate the Data *** #
# *** Save Data *** #

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from functions_and_parameters import interim_path, visualisation_path, pull_data_frame


lice_file = "lice.csv"
#Removing the missing values of the data 'sorted_lice.csv', and save the new data to 'lakslus.csv'

lakslus_original = pull_data_frame(lice_file, interim_path, seperator=",")
lakslus_cleaned = lakslus_original.dropna()  # remove the missing value



#Subest the dataset and take the mean 


# investigation per region
lakslus_region_mean = lakslus_cleaned.groupby('location_name')[
    "location_number",
    "lice_female_mature",
    "lice_movables",
    "location_longditude",
    "location_lattitude"].mean()

# simple desriptive statistics
lakslus_region_mean.mean()
lakslus_region_mean.std()
print(lakslus_region_mean)


# compare the histogram NO IDEA WHAT THIS HISTOGRAM SHOWS
f1 = plt.figure()
lakslus_region_mean['lice_female_mature'].hist(bins = 200, color='b')  
# choose the bins number to make a good graph
plt.xlabel('Lice number per fish')
plt.ylabel('Location number')
plt.title('The histogram of adult female lice')
plt.savefig(visualisation_path / "lice_female_mature.png")
plt.show()
f2 = plt.figure()
lakslus_region_mean['lice_movables'].hist(bins = 200, color='g')
plt.xlabel('Lice number per fish')
plt.ylabel('Location number')
plt.title('The histogram of lice in motile stages')
plt.savefig(visualisation_path / "lice_movables.png")
plt.show()
f3 = plt.figure()


# Investigateion on two chosen locations and compare


lakslus_Aldalen = lakslus_cleaned[lakslus_cleaned['location_name'] == "Aldalen"]
lakslus_Nautvik = lakslus_cleaned[lakslus_cleaned['location_name'] == "Nautvik"]

lakslus_Aldalen_2022 = lakslus_Aldalen[lakslus_Aldalen['location_time_year']==2022][['location_time_week', 'lice_female_mature', 'lice_movables', 'temperature']]
f3 = plt.figure()
plt.plot(lakslus_Aldalen_2022['location_time_week'], lakslus_Aldalen_2022['lice_female_mature'])
plt.xlabel('Weeks in 2022')
plt.ylabel('Adult female lice number')
plt.title('The adult female lice of Aldalen in 2022')
plt.savefig(visualisation_path / 'Aldalen_Voksne_hunnlus.png')
plt.show()


lakslus_Nautvik_2022 = lakslus_Nautvik[lakslus_Nautvik['location_time_year']==2022][['location_time_week', 'lice_female_mature', 'lice_movables', 'temperature']]
f4 = plt.figure()
plt.plot(lakslus_Nautvik_2022['location_time_week'], lakslus_Nautvik_2022['lice_female_mature'])
plt.xlabel('Weeks in 2022')
plt.ylabel('Adult female lice number')
plt.title('The adult female lice of Nautvik in 2022')
plt.savefig(visualisation_path / 'Nautvik_Voksne_hunnlus.png')
plt.show()
# lakslus_cleaned[lakslus_cleaned['Sjøtemperatur'] >= 20].sort_values('Sjøtemperatur', ascending=False)

# yearly average
#lakslus_Aldalen_weekly_mean = lakslus_Aldalen.groupby('Uke').mean()


# join the lice data with the license data
salmon_licence = pd.read_csv('/Users/taohongliao/Desktop/TEP4221/project/data/interim/salmon_licence.csv')

# test are there 
lakslus_region_mean['Lokalitetsnummer'].isin(salmon_licence['LOK_NR']).value_counts() 

lakslus_region_mean_new = lakslus_region_mean.merge(salmon_licence, how='inner', left_on='Lokalitetsnummer', right_on='LOK_NR') # Combine the data of salmon_licence and lakslus_region_mean by the same location number



#%%
lakslus_region_mean_new.to_csv('/Users/taohongliao/Desktop/TEP4221/project/data/interim/lakslus_region_mean_new.csv')

# does not work yet, need to clean the data first
# lakslus_region_mean_new['Total voksne hunnlus'] = lakslus_region_mean_new['Voksne hunnlus'] * lakslus_region_mean_new['LOK_KAP'] * 1.6 / 2

# lakslus_region_mean_new['Total lus i bevegelige stadier'] = lakslus_region_mean_new['Lus i bevegelige stadier'] * lakslus_region_mean_new['LOK_KAP'] * 1.6 / 2.0

# lakslus_region_mean_new['Total fastsittende lus'] = lakslus_region_mean_new['Fastsittende lus'] * lakslus_region_mean_new['LOK_KAP'] * 1.6 / 2

#%%




# %% convert to geopandas
lakslus_geopd = gpd.GeoDataFrame(
    lakslus_region_mean, geometry=gpd.points_from_xy(lakslus_region_mean.Lon, lakslus_region_mean.Lat))

lakslus_geopd.plot()

# %%
import contextily
fig, ax = plt.subplots()
ax.plot(lakslus_geopd["Lon"], lakslus_geopd["Lat"], 'o', markersize=1)
contextily.add_basemap(ax)
plt.show()


# %%

fig, ax = plt.subplots()
lakslus_geopd.plot(column = 'Fastsittende lus', cmap = 'RdPu', edgecolor = 'black', legend = True, alpha = 0.5, ax = ax)
plt.title('Schools per decimal degrees squared area')
plt.xlabel('longitude')
plt.ylabel('latitude')
contextily.add_basemap(ax)

# read the norway border
norway_boarder = gpd.read_file('/Users/taohongliao/Desktop/TEP4221/project/data/interim/gadm41_NOR_0.shx')
norway_boarder.plot(ax =ax)
plt.savefig('/Users/taohongliao/Desktop/TEP4221/project/visualisation/map.png')
plt.show()

# %%
