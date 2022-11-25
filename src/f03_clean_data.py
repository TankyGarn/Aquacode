# This is the first script for the project.
# -*- coding: utf-8 -*-
# Authors: Taohong Liao
# Date: 2022.10.25
# Updated: 2022.10.31
# *** File purpose ***#
""" 
Aim: Clean the data of 'sorted_lice' and 
'salmon_licence', combine the two dataframes
"""
# *** Importing Packages ***#
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from functions_and_parameters import *

# *** Define parameters ***#
lice_and_licence_file = "df_lice_and_licence.csv"


# *** Defining Functions ***#
# No functions


# *** Load Data *** #
lice_dataframe = pull_data_frame(lice_and_licence_file, interim_path, seperator=",")

# *** Manipulate the Data *** #
# Subest the dataset and take the mean
# investigation per region
lakslus_region_mean = lice_dataframe.groupby("location_name")[
    "location_number",
    "lice_female_mature",
    "lice_movables",
    "location_lattitude",
    "location_longditude",
].mean()

# simple desriptive statistics
lakslus_region_mean.mean()
lakslus_region_mean.std()


# *** Save Data *** #
# Investigateion on two chosen locations and compare
lakslus_Aldalen = lice_dataframe[lice_dataframe["location_name"] == "Aldalen"]
lakslus_Nautvik = lice_dataframe[lice_dataframe["location_name"] == "Nautvik"]

lakslus_Aldalen_2022 = lakslus_Aldalen[lakslus_Aldalen["location_time_year"] == 2022][["location_time_week", "lice_female_mature", "lice_movables", "temperature"]]
lakslus_Nautvik_2022 = lakslus_Nautvik[lakslus_Nautvik["location_time_year"] == 2022][["location_time_week", "lice_female_mature", "lice_movables", "temperature"]]
