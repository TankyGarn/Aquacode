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
import pandas as pd
from functions_and_parameters import *
import matplotlib.pyplot as plt

# *** Define parameters ***#
# Parameters
licence_file = "licence.csv"
lice_file = "lice.csv"
sedimentation_file = "sedimentation.csv"
# *** Defining Functions ***#
# *** Load Data ***#
# *** Manipulate the Data *** #
# *** Save Data *** #




# Functions


def get_list_of_all_lice_on_location(dataframe, location, identificaiton="location_number" ):

    location_dataframe = dataframe.loc[(df_merged[identificaiton] == location)]
    location_dataframe = location_dataframe.set_index(["location_time_year", "location_time_week"])
    location_dataframe = location_dataframe.sort_index()
    location_lice_list = makeList(location_dataframe, "lice_female_mature")

    return location_lice_list


def create_equal_long_plot(list):
    list1 = []
    for i in range(len(list)):
        list1.append(i)
    return list1

# Load data

df_licence = pull_data_frame(licence_file, interim_path, seperator=",")
df_lice = pull_data_frame(lice_file, interim_path, seperator=",")

# add location owner:
df_merged = pd.concat([df_lice,df_licence])

lice_soløya = get_list_of_all_lice_on_location(df_merged, 10029)
print("tetst")
time_soløya = create_equal_long_plot(lice_soløya)

plt.plot(time_soløya,lice_soløya)

plt.show()
# Export Data
#push_data_frame("df_lice_and_licence.csv", df_merged, interim_path)