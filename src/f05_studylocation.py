# This is the first script for the project.
# -*- coding: utf-8 -*-
# Authors: Taohong Liao and Nikolai Vestbøstad
# Date: 2022.10.25
# Updated: 2022.10.31
# *** File purpose ***#
""" Aim: 
The aim of this file is to create two scatter plots.
1. Plot: How to all locations distribute in a 
sedimentation level x lice concentration plot.

2. like the first plot, but group the locations in by company.
this will give us a view if some companies are using tactics.
wich can be used to compare how the different companies
align them selves concidering sedimentationlevel
and licelevel. 

How achived:
* Using the dataset created in /04

What to do next:
* Clean code, this is a hacky mess.
* Find out how to write plotting code nicer. 

"""


# *** Importing Packages ***#
from functions_and_parameters import *
from f04_process_data import from_dataframe_return_company_and_values


# *** Define parameters ***#
licence_file = "licence.csv"
sedimentation_file = "sedimentation.csv"
lice_file = "lice.csv"

# *** Defining Functions ***#

def index_of_location(location_number):
    index_for_the_location = list_of_locationnumbers.index(location_number)
    return index_for_the_location


# *** Load Data ***#
new_dataframe = pull_data_frame("lice_location_state_owner_dataframe.csv", interim_path, seperator=",")

# *** Manipulate the Data *** #
# this is the plot for all individual locations
sizes = np.array([new_dataframe["location_capasity"] / 1000])
new_dataframe.plot.scatter(
    x="lice_female_mature",
    y="location_state",
    s=sizes,
    c=np.random.rand(len(new_dataframe["location_capasity"]), 3),
)

list_of_locationnumbers = list(new_dataframe["location_number"])


# The folowing block is a bad way to sort a dataframe, but it works...
# What the code does is as follows:
# 1. It sorts the dataframe by company
new_dataframe = new_dataframe.set_index("location_owner")
new_dataframe = new_dataframe.sort_index()
new_dataframe = new_dataframe.reset_index()

# 2. It creates new dataframes where they sum up the mean values for the different companies
licence_dataframe_location_capasity = from_dataframe_return_company_and_values(
    new_dataframe, "location_owner", "location_capasity"
)
lice_dataframe_female_lice = from_dataframe_return_company_and_values(
    new_dataframe, "location_owner", "lice_female_mature", mean=True
)
sedimentation_dataframe_sedimentation_state = from_dataframe_return_company_and_values(
    new_dataframe, "location_owner", "location_state", mean=True
)

# 3. It combines the dataframes into one dataframe
newest_dataframe = lice_dataframe_female_lice.merge(
    licence_dataframe_location_capasity, on="location_owner"
)
newest_dataframe = newest_dataframe.merge(
    sedimentation_dataframe_sedimentation_state, on="location_owner"
)
# 4. It Plots the data that is aquired, and it is a bit messy, but it works
sizes = np.array([newest_dataframe["location_capasity"] / 1000])
x = newest_dataframe["lice_female_mature"].to_list()
y = newest_dataframe["location_state"].to_list()
z = newest_dataframe.index.values.tolist()

# This is the plot that shows the companies seperated.
ax = newest_dataframe.plot.scatter(
    x="lice_female_mature",
    y="location_state",
    s=sizes,
    c=np.random.rand(len(newest_dataframe["location_capasity"]), 3),
    xlabel=None,
    title="Lice concentration vs. Sedimentation level",   
)
# 5. It adds the company names to the plot
for i, txt in enumerate(z):
    ax.annotate(txt, (x[i], y[i]))






print(newest_dataframe.sort_index())

plt.show()
