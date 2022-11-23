# This is the first script for the project.
# -*- coding: utf-8 -*-
# Authors: Taohong Liao and Nikolai Vestbøstad
# Date: 2022.10.25
# Updated: 2022.10.31
# *** File purpose ***#
""" Aim: 
* The aim of this file is to pull data from .csv files.
* Edit the data and remove a couple of the initial problems that comes from the getgo.
* Change the names of the files that we will use later.
"""
# *** Importing Packages ***#
# *** Define parameters ***#
# *** Defining Functions ***#
# *** Load Data ***#
# *** Manipulate the Data *** #
# *** Save Data *** #
""" Aim: Clean the data of 'sorted_lice' and 'salmon_licence', combine the two data ".
"""

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from functions_and_parameters import*


raw_path = data_path / "raw" / "FDIR"
own_path = data_path / "raw" / "OWN"
interim_path = data_path / "interim"

lice_and_licence_file = "df_lice_and_licence.csv"

lice_dataframe = pull_data_frame(lice_and_licence_file, interim_path,seperator=",")

print(lice_dataframe)

#Subest the dataset and take the mean 
# investigation per region
lakslus_region_mean = lice_dataframe.groupby('location_name')['location_number', 'lice_female_mature', 'lice_movables','location_lattitude', 'location_longditude'].mean()
# simple desriptive statistics
lakslus_region_mean.mean()
lakslus_region_mean.std()

# Investigateion on two chosen locations and compare


lakslus_Aldalen = lice_dataframe[lice_dataframe['location_name'] == "Aldalen"]
lakslus_Nautvik = lice_dataframe[lice_dataframe['location_name'] == "Nautvik"]

lakslus_Aldalen_2022 = lakslus_Aldalen[lakslus_Aldalen['location_time_year']==2022][['location_time_week', 'lice_female_mature', 'lice_movables', 'temperature']]
lakslus_Nautvik_2022 = lakslus_Nautvik[lakslus_Nautvik['location_time_year']==2022][['location_time_week', 'lice_female_mature', 'lice_movables', 'temperature']]

