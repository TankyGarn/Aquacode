# -*- coding: utf-8 -*-
# Authors: Taohong Liao and Nikolai Vestbøstad
# Date: 2022.10.25
# Updated: 2022.10.31
# *** File purpose ***#
""" 
Aim: generate a location plot that shows
salmon lice at a location one year
"""
# *** Importing Packages ***#
import matplotlib.pyplot as plt
from functions_and_parameters import *

# *** Define parameters ***#
lice_and_licence_file = "df_lice_and_licence.csv"


# *** Defining Functions ***#

def plot_lice_year(Location_name, year):
    """
    Takes the location name of a location and year you want to study.
    note: you have to write location name with capital letter, this should be fixed

    Args:
        Location_name (string): Remember Capital letter
        year (int): (between 2012-2022)
    """
    # locate data
    lice_location = lice_dataframe[lice_dataframe["location_name"] == Location_name]
    lice_location_year = lice_location[lice_location["location_time_year"] == year][["location_time_week", "lice_female_mature", "lice_movables", "temperature"]]

    os.chdir(visualisation_path)
    # plot data
    f5 = plt.figure()
    plt.plot(lice_location_year['location_time_week'], lice_location_year['lice_female_mature'])
    plt.xlabel(f'Weeks in {year}')
    plt.ylabel('Mature female lice number')
    plt.title(f'The mature female lice of {Location_name} in {year}')
    plt.savefig(f'lice_{Location_name}_{year}.png')
    # ** plt.show()


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

plot_lice_year("Nautvik", 2022)
plot_lice_year("Aldalen", 2022)