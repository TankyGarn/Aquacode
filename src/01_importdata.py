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
# Due to using same funcitons over multiple files we chose to import dependencies once.
# We are not sure if this is the way to do it in python, but it is common in C++
from functions_and_parameters import *


# *** Define parameters ***#
# Defining the names of the files we want to read, found in raw_path:
licence_file = "Akvakulturregisteret.csv"
sedimentation_file = "Historiske_B-undersøkelser.csv"
lice_file = "lakselus_per_fisk.csv"

# *** Defining Functions ***#
# There are no functions in this file.
# The functions whom are developed for this file are pretty universal
# Therefore the functions are in the / functions_and_parameters.py


# *** Load Data ***#
# use the pull_data_frame function, in /functions_and_parameters.py
licence = pull_data_frame(licence_file, raw_path, True)
sedimentation = pull_data_frame(sedimentation_file, raw_path)
lice = pull_data_frame(lice_file, raw_path)


# *** Manipulate the Data *** #
# We would like to rename the columnnames to be the same
# in all of the different files.
licence.rename(columns=translation_dict_licence, inplace=True)
lice.rename(columns=translation_dict_lice, inplace=True)
sedimentation.rename(columns=translation_dict_sediment, inplace=True)

# Add Type Of Data to files
# Not sure if we actually need this in the frames, since we changed path.
lice["instance_type"] = "Lusetelling"
sedimentation["instance_type"] = "sedimentation"

# Sorting out so we only look at salmon locations with seawater.
# Sort out the licences with salmon (Biomass allowed is noted on the salmon values) we only want salmon and seawater
licence = licence.loc[(licence["location_species"] == "Laks") & (licence["VANNMILJØ"] == "SALTVANN")]

# Sorting so we get a more prefferable index.
licence = licence.set_index(["location_name", "location_number"]).sort_index()
sedimentation = sedimentation.set_index(["location_name", "location_number"]).sort_index()
lice = lice.set_index(["location_name", "location_number"]).sort_index()

# Clean Dataset characters, look at funciton comments to se how.
# Required since the invisible characters messes up the data for the datasets.
clean_dataset_char(licence, ",", ".", "location_capasity")
clean_dataset_char(licence, " ", "", "location_capasity")
clean_dataset_char(licence, ",", ".", "TILL_KAP")
clean_dataset_char(licence, " ", "", "TILL_KAP")

# Change time in sedimentation data to week.
# Adding it so that sedimentation and lice data have the same time format.
sedimentation["location_time_week"] = sedimentation["time"].apply(fromDateToWeek)
sedimentation["location_time_year"] = sedimentation["time"].apply(fromDateToYear)


# *** Save Data *** #
# Saving data into the interim_path
push_data_frame("licence.csv", licence, interim_path)
push_data_frame("sedimentation.csv", sedimentation, interim_path)
push_data_frame("lice.csv", lice, interim_path)
