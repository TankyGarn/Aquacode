import pandas as pd
from loadingdata import *

# Paths
raw_path = data_path / "raw" / "FDIR"
own_path = data_path / "raw" / "OWN"
interim_path = data_path / "interim"

# Parameters
licence_file = "licence.csv"
lice_file = "lice.csv"


# Import Data
df_licence = pull_data_frame(licence_file, interim_path, seperator=",")
df_lice = pull_data_frame(lice_file, interim_path, seperator=",")


# Do something to the data
df_merged = pandas.concat([df_lice, df_licence], axis=0)
df_merged_reduced = df_merged[naming_list]

# Export Data

push_data_frame("df_lice_and_licence.csv", df_merged_reduced, interim_path)
