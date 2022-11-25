# This is the first script for the project.
# -*- coding: utf-8 -*-
# Authors: Nikolai Vestbøstad
# Date: 2022.11.25
# Updated: 2022.11.25
# *** File purpose ***#
"""
Aim:
The aim for this file is to be able to make a location report that 
creates a plot of lice over the history of the location.

How achived:
*Write functions that make it posible to generate alot of reports, per location.

What to improve:
*Would like to use this to generate a location report in Pdf form where we could
combine different plots like these to create a location report, whom utilizes 
the location reports that are in the sedimentation dataset.
"""
# *** Importing Packages ***#
import pandas as pd
from functions_and_parameters import *
from f04_process_data import get_owner, licence_dataframe
import matplotlib.pyplot as plt


# *** Define parameters ***#
# Parameters
licence_file = "licence.csv"
lice_file = "lice.csv"
sedimentation_file = "sedimentation.csv"


# *** Defining Functions ***
def get_list_of_all_lice_on_location(dataframe, location, identificaiton="location_number"):
    """
    This function splits the dataframe into a dataframe that folows one location.
    Then it returnes a list of all the licecounts.
    NAN objects in list means there has not been any counting of sealice.


    Args:
        dataframe (dataframe): needs a dataframe with the correct identification value as a column
        location (int): should be a location id number
        identificaiton (str, optional): _description_. Defaults to "location_number", this exists 
        to be able to maybe use this more universal

    Returns:
        list: list of all accounts of lice.
    """
    location_dataframe = dataframe.loc[(dataframe[identificaiton] == location)]
    location_dataframe = location_dataframe.set_index(["location_time_year", "location_time_week"])
    location_dataframe = location_dataframe.sort_index()
    location_lice_list = makeList(location_dataframe, "lice_female_mature")

    return location_lice_list

def get_location(location_number, dataframe):
    """
    LOCAL: Takes in a location_number and returns the location_name of that location
    Note: This function is only for the local use of the project.
    This is a result of spagetti and probable should be done in a better way.

    Args:
        location_number (int): takes in a location_number from the licence_dataframe.

    Returns:
        str: returns the name of name of the location.
    """
    location_df = dataframe.loc[
        dataframe["location_number"] == location_number
    ]
    location = location_df["location_name"].to_list()
    return location[0]


def create_equal_long_plot(list):
    #I know you could make this using linspcae..
    list1 = []
    for i in range(len(list)):
        list1.append(i)
    return list1

def plot_for_location(location_number):
    #this is a plot generator for the location. 
    # 
    # Needs to be done: Make time be in date/ other format
    # Want to be : make plot prettier
    location_owner = get_owner(location_number,licence_dataframe)
    location_name = get_location(location_number,df_merged)
    
    lice_location = get_list_of_all_lice_on_location(df_merged,location_number)
    time_location = create_equal_long_plot(lice_location)
    #not sure if this path is best path to be.
    os.chdir(visualisation_path)

    #standard plot..
    plt.plot(time_location, lice_location)
    plt.title(f"Sealice at location:   {location_name}  whole dataset")
    plt.xlabel("Weeks since 1.janary 2012")
    plt.ylabel("Mean Female Sealice")
    plt.savefig(f"{location_number}{location_name}lice.png",dpi = 300)

    return location_name, location_number, location_owner

# *** Load Data ***#
df_licence = pull_data_frame(licence_file, interim_path, seperator=",")
df_lice = pull_data_frame(lice_file, interim_path, seperator=",")
df_merged = pd.concat([df_lice, df_licence])

# *** Manipulate the Data *** #
plot_for_location(34697)


# *** Save Data ***#
push_data_frame("df_lice_and_licence.csv", df_merged, interim_path)
