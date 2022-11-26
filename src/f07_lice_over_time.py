# This is the first script for the project.
# -*- coding: utf-8 -*-
# Authors: Taohong Liao and Nikolai Vestbøstad
# Date: 2022.10.25
# Updated: 2022.10.31
# *** File purpose ***#
""" 
Aim: The goal with this file is to generate a map animation that shows the
lice situation over time. This map will be generated for all locations.

How achived:
    What datapoints are needed?

    From the csv's we need:
    * location number
    * female lice
    * time (year and week)
    * location (longditude and lattitude)

    From other sources we need:
    * Map of Norway

Steps:
    1. Generate a dataframe that only has locationnumber, female lice, time and location.

    2. Make a plot that shows the lice situation for a given time.

    3. make a loop that loops the lice situation for all times.
"""

# *** Importing Packages ***#  
from functions_and_parameters import pull_data_frame, push_data_frame, pull_6_columns, interim_path, plt , np, video_read_path, os
import geopandas as gpd

# *** Define parameters ***#
lice_file = "lice.csv"
world_data = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
norge =  world_data[world_data.name == "Norway"]
print(norge)

# *** Defining Functions ***#
# generates a dataframe with all the accounts that happend at a given time
def generate_time_dataframe(dataframe, year, week):
    return dataframe[(dataframe["location_time_year"] == year) & (dataframe["location_time_week"] == week)]

def normalize_with_x_numbers(number):
    #some problems with sorting requires the same numbers of nubmers...
    if number < 10:
        number = f"00{number}"
    elif number < 100:
        number = f"0{number}"
    else:
        number = number
    return number

def generate_map(dataframe, year, week, index):
    time_dataframe = generate_time_dataframe(dataframe, year, week)
    sizes = np.array([time_dataframe["lice_female_mature"]*50])
    colors =np.array([time_dataframe["lice_female_mature"]])
    axis=norge.plot()
    ax = time_dataframe.plot.scatter(x="location_longditude", y="location_lattitude", cmap="Dark2", c=colors, s = sizes, ax = axis)
    ax.set_title(f"Lice situation in week {normalize_with_x_numbers(week)} in {year}")
    ax.x_label = "Longditude"
    ax.y_label = "Lattitude"
    ax.xticks = np.arange(4, 31, 1)
    ax.yticks = np.arange(57, 71, 1)
    ax.set_xlim(1, 34)
    ax.set_ylim(54, 75)
    os.chdir(video_read_path)
    ax.figure.savefig(f"{normalize_with_x_numbers(index)}_{year}_{normalize_with_x_numbers(week)}_licesituation.png", dpi=300)


# makes a plot that shows the locations and the lice situation for a given time
def generate_pictures_for_animation():
    index = 0
    for i in range (2012, 2023):
        for j in range (1, 53):
            generate_map(new_lice_dataframe, i, j, index)
            print("f07_lice_over_time frames generator : (year/month/index) ", i ,"/", str(normalize_with_x_numbers(j)) ,"/", str(normalize_with_x_numbers(index)) ," done")
            index = index + 1

# *** Load Data *** #
lice_dataframe = pull_data_frame(lice_file, interim_path, seperator=",")

# *** Manipulate the Data *** #

new_lice_dataframe = pull_6_columns(
    lice_dataframe,
    "location_number",
    "lice_female_mature",
    "location_time_year",
    "location_time_week",
    "location_lattitude",
    "location_longditude")

new_lice_dataframe = new_lice_dataframe.sort_values(by=["location_time_year", "location_time_week"])

generate_pictures_for_animation()

# *** Save Data *** #
push_data_frame("reduced_lice_dataframe.csv", new_lice_dataframe, interim_path) 
