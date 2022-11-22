# The goal of this file is to pull licence data, and find out the production tonnage of each company.
import matplotlib.pyplot as plt
import numpy as np
from functions_and_parameters import *

licence_file = "licence.csv"
sedimentation_file = "sedimentation.csv"
lice_file = "lice.csv"


licence_dataframe = pull_data_frame(licence_file, interim_path, seperator=",")
sedimentation_dataframe = pull_data_frame(sedimentation_file, interim_path, seperator=",")
lice_dataframe = pull_data_frame(lice_file, interim_path, seperator=",")

"""
print(licence_dataframe.columns)
owner_capasity_location = licence_dataframe[
    [
        "location_name",
        "location_owner",
        "location_capasity",
        "location_lattitude",
        "location_longditude",
        "production_area",
    ]
]
owner_capasity_location = owner_capasity_location.drop_duplicates(["location_name"])


owner_capasity_location.groupby("location_owner")

grouped_owner_capasity_location = owner_capasity_location.set_index(["location_owner"])
grouped_owner_capasity_location = grouped_owner_capasity_location.sort_index()

saved_owner_capasity = grouped_owner_capasity_location.groupby("location_owner")["location_capasity"].sum()
print(saved_owner_capasity)

list_saved_owner_capasity_nr = saved_owner_capasity.tolist()

print(list_saved_owner_capasity_nr)


list_saved_owner_capasity = saved_owner_capasity.index.values.tolist()

print(list_saved_owner_capasity)
new_list = []
for i in range(len(list_saved_owner_capasity)):
    new_list.append([list_saved_owner_capasity_nr[i], list_saved_owner_capasity[i]])

print(new_list)
"""

def from_dataframe_return_company_and_values(study_dataframe,value_column,mean=False):
    new_dataframe = pandas.DataFrame()
    returnable_datafame = pandas.DataFrame()
    new_dataframe["location_number"] = study_dataframe["location_number"]
    new_dataframe[value_column] = study_dataframe[value_column]
    saved_sum = new_dataframe.groupby("location_number")[value_column].sum()
    if mean == True:
        saved_sum =  saved_sum/len(saved_sum)
    else:
        saved_sum = saved_sum
    print(saved_sum.index.values)
    returnable_datafame[value_column] = saved_sum
    return returnable_datafame
    

licence_dataframe_location_capasity = from_dataframe_return_company_and_values(licence_dataframe,"location_capasity")
lice_dataframe_female_lice = from_dataframe_return_company_and_values(lice_dataframe, "lice_female_mature",mean=True)
sedimentation_dataframe_sedimentation_state = from_dataframe_return_company_and_values(sedimentation_dataframe,"location_state",mean=True)






new_dataframe = lice_dataframe_female_lice.merge(licence_dataframe_location_capasity, on="location_number")
new_dataframe = new_dataframe.merge(sedimentation_dataframe_sedimentation_state, on="location_number")

print(new_dataframe)


sizes = np.array([new_dataframe["location_capasity"]/1000])

new_dataframe.plot.scatter(x="lice_female_mature", y="location_state",s = sizes, c=np.random.rand(len(new_dataframe["location_capasity"]),3) )

print(new_dataframe)

def get_owner(location_number):
    location_df = licence_dataframe.loc[licence_dataframe['location_number'] == location_number]
    owner = location_df["location_owner"].to_list()
    return owner[0]

list_of_locationnumbers = new_dataframe.index.to_list()

def index_of_location(location_number):
    index_for_the_location = list_of_locationnumbers.index(location_number)
    return index_for_the_location


print(new_dataframe["lice_female_mature"].iloc[index_of_location(10029)])


def get_owner_columb(dataframe_with_no_owner):
    owner_list = []
    location_number_list = list(dataframe_with_no_owner.index.values)
    dataframe_with_owner_column = dataframe_with_no_owner

    for location_number in location_number_list:
        owner_list.append(get_owner(location_number))

    dataframe_with_owner_column["location_owner"] = owner_list

    return dataframe_with_owner_column

print(get_owner_columb(new_dataframe))

new_dataframe = new_dataframe.set_index("location_owner")
new_dataframe = new_dataframe.sort_index()

print(new_dataframe)