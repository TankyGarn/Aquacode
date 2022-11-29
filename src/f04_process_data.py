# This is the first script for the project.
# -*- coding: utf-8 -*-
# Authors: Nikolai Vestbøstad
# Date: 24.11.2022
# Updated: 24.11.2022


# *** File purpose ***#
""" Aim: 
* The aim of this file is to create a dataset that
is suitable for a scatterplot that could show  if there
is some correlation between high lice and high sedimentation levels
* Note, we have not found any reasearch that looks into this.

How achived:
* Write functions that pull data neatly from datasets and combines them into new datasets.
* Pipelining

What to improve:
* The code is not very readable, and could be improved.
"""


# *** Importing Packages ***#
from functions_and_parameters import *


# *** Define parameters ***#
licence_file = "licence.csv"
sedimentation_file = "sedimentation.csv"
lice_file = "lice.csv"


# *** Defining Functions ***#
def from_dataframe_return_company_and_values(study_dataframe, study_column, value_column, mean=False):
    """Pull two columns from a dataframe and returns
    a dataframe with a indexcolumn (study_column),
    wich should be a parent hierarchially to the value_column.
    
    The value_column will be returned as the sum/mean of all
    the values with one column, wich is the sum/mean of all
    the values for that specific index.

    Args:
        study_dataframe (DataFrame): The dataframe that will be used.
        study_column (DataFrame_Column): The column that will be used as the index.
        value_column (DataFrame_Column): The column that will be for the value calculations.
        mean (bool, optional): if you want the value to be the mean do mean == True. Defaults to False.

    Returns:
        DataFrame: with study_column as index and value_column as the sum/mean of all the values.
    """
    # creates two dataframes, one for the return and one for the calculations.
    new_dataframe = pandas.DataFrame()
    returnable_dataframe = pandas.DataFrame()

    # adds the two columns to the new dataframe.
    new_dataframe[study_column] = study_dataframe[study_column]
    new_dataframe[value_column] = study_dataframe[value_column]

    # calculates the sum/mean of the values for the index.
    saved_sum = new_dataframe.groupby(study_column)[value_column].sum()

    # if mean == True, the value will be the mean of all the values for the index.
    if mean:
        saved_sum = saved_sum/len(saved_sum)
    else:
        saved_sum = saved_sum

    # adds the sum/mean to the returnable dataframe.
    returnable_dataframe[value_column] = saved_sum

    # returns the dataframe.
    return returnable_dataframe


def get_owner(location_number, dataframe):
    """
    LOCAL: Takes in a location_number and returns the owner of that location
    Note: This function is only for the local use of the project.
    This is a result of spagetti and probable should be done in a better way.

    Args:
        location_number (int): takes in a location_number from the licence_dataframe.

    Returns:
        str: returns the name of the owner of the location.
    """
    location_df = dataframe.loc[
        dataframe["location_number"] == location_number
    ]
    owner = location_df["location_owner"].to_list()
    return owner[0]


def get_owner_columb(dataframe_with_no_owner):
    """
    LOCAL:Takes in a dataframe with no owner columb 
    and returns a dataframe with a owner columb.
    Note: This function is only for the local use of the project.

    Args:
        dataframe_with_no_owner (dataframe): takes in a dataframe with no owner columb.

    Returns:
        dataframe: dataframe with a owner columb.
    """
    # make emty list.
    owner_list = []

    # not sure why this works but it does.
    location_number_list = list(dataframe_with_no_owner. index.values)
    dataframe_with_owner_column = dataframe_with_no_owner

    for location_number in location_number_list:
        owner_list.append(get_owner(location_number, licence_dataframe))

    # appends the owner_list to the dataframe.
    dataframe_with_owner_column["location_owner"] = owner_list

    # returns the dataframe.
    return dataframe_with_owner_column


# *** Load Data ***#
licence_dataframe = pull_data_frame(licence_file, interim_path, seperator=",")
sedimentation_dataframe = pull_data_frame(sedimentation_file, interim_path, seperator=",")
lice_dataframe = pull_data_frame(lice_file, interim_path, seperator=",")


# *** Manipulate the Data *** #
# From Licence dataframe get location capasity
licence_dataframe_location_capasity = from_dataframe_return_company_and_values(
    licence_dataframe, "location_number", "location_capasity")
# From Lice dataframe get number of female mature lice
lice_dataframe_female_lice = from_dataframe_return_company_and_values(
    lice_dataframe, "location_number", "lice_female_mature", mean=True)
# From Sedimentation dataframe get sedimentation level
sedimentation_dataframe_sedimentation_state = from_dataframe_return_company_and_values(
    sedimentation_dataframe, "location_number", "location_state", mean=True)

# combining the dataframes into one dataframe (This should be done in a better way)
lice_location_state_owner_dataframe = lice_dataframe_female_lice.merge(
    licence_dataframe_location_capasity, on="location_number")
lice_location_state_owner_dataframe = lice_location_state_owner_dataframe.merge(
    sedimentation_dataframe_sedimentation_state, on="location_number")

# adding the owner column to the dataframe (This should be done in a better way)
lice_location_state_owner_dataframe = get_owner_columb(lice_location_state_owner_dataframe)

# *** Save Data *** #
push_data_frame("lice_location_state_owner_dataframe.csv", lice_location_state_owner_dataframe, interim_path)