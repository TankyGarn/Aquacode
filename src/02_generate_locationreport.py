import pandas as pd
from functions_and_parameters import *
# Paths
raw_path = data_path / "raw" / "FDIR"
own_path = data_path / "raw" / "OWN"
interim_path = data_path / "interim"

# Parameters
licence_file = "licence.csv"
lice_file = "lice.csv"

#Functions

def get_list_of_all_lice_on_location(dataframe,location, identificaiton = "location_name"):
    location_dataframe = dataframe.loc[(df_merged[identificaiton] == location)]
    location_dataframe = location_dataframe.set_index(["location_time_year","location_time_week"])
    location_dataframe = location_dataframe.sort_index()
    location_lice_list = makeList(location_dataframe,"lice_female_mature")
    print(location_dataframe)
    print(location_lice_list)
    return location_lice_list

# Load data
df_licence = pull_data_frame(licence_file, interim_path, seperator=",")
df_lice = pull_data_frame(lice_file, interim_path, seperator=",")

# Merge df_lice and df_licence
df_merged = pandas.merge(df_lice, df_licence)
#reduce the columbs to data included in the naming list.
df_merged = df_merged[naming_list]

lice_soløya = get_list_of_all_lice_on_location(df_merged,"Sølvøyane")


#Export Data
push_data_frame("df_lice_and_licence.csv", df_merged, interim_path)

