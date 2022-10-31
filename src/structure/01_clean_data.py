#%%
#This is the main script for the project TEP4221
# -*- coding: utf-8 -*-
# Authors: Taohong Liao and Nikolai Vestbøstad
# Date: 2022.10.25
# Updated: 2022.10.31
""" Aim: Clean the data of 'sorted_lice' and 'salmon_licence', combine the two data ".
"""

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

#%% Removing the missing values of the data 'sorted_lice.csv', and save the new data to 'lakslus.csv'

lakslus_original = pd.read_csv('/Users/taohongliao/Desktop/TEP4221/project/data/interim/sorted_lice.csv')
lakslus_cleaned = lakslus_original.dropna()  # remove the missing value
lakslus_cleaned.to_csv('/Users/taohongliao/Desktop/TEP4221/project/data/interim/lakslus_cleaned.csv') 

#%% Subest the dataset and take the mean 
# investigation per region
lakslus_region_mean = lakslus_cleaned.groupby('Lokalitetsnavn')['Lokalitetsnummer', 'Voksne hunnlus', 'Lus i bevegelige stadier', 'Fastsittende lus','Lat', 'Lon'].mean()
# simple desriptive statistics
lakslus_region_mean.mean()
lakslus_region_mean.std()

#%% Investigateion on two chosen locations and compare


lakslus_Aldalen = lakslus_cleaned[lakslus_cleaned['Lokalitetsnavn'] == "Aldalen"]
lakslus_Nautvik = lakslus_cleaned[lakslus_cleaned['Lokalitetsnavn'] == "Nautvik"]

lakslus_Aldalen_2022 = lakslus_Aldalen[lakslus_Aldalen['År']==2022][['Uke', 'Voksne hunnlus', 'Lus i bevegelige stadier', 'Fastsittende lus', 'Sjøtemperatur']]
lakslus_Nautvik_2022 = lakslus_Nautvik[lakslus_Nautvik['År']==2022][['Uke', 'Voksne hunnlus', 'Lus i bevegelige stadier', 'Fastsittende lus', 'Sjøtemperatur']]

#%% join the lice data with the license data
salmon_licence = pd.read_csv('/Users/taohongliao/Desktop/TEP4221/project/data/interim/salmon_licence.csv')

# test and compare the same location number between lice data and licence data 
lakslus_region_mean['Lokalitetsnummer'].isin(salmon_licence['LOK_NR']).value_counts() 
lakslus_region_mean_new = lakslus_region_mean.merge(salmon_licence, how='inner', left_on='Lokalitetsnummer', right_on='LOK_NR') # Combine the data of salmon_licence and lakslus_region_mean by the same location number
lakslus_region_mean_new.to_csv('/Users/taohongliao/Desktop/TEP4221/project/data/interim/lakslus_region_mean_new.csv')
