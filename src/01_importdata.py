# *** Importing ***#
# imports from the loadingdata.py

from loadingdata import *



raw_path = data_path / "raw" / "FDIR"
own_path = data_path / "raw" / "OWN"
interim_path = data_path / "interim"


# Defining the names of the files we want to read, found in raw_path:
licence_file = "Akvakulturregisteret.csv"
sedimentation_file = "Historiske_B-undersøkelser.csv"
lice_file = "lakselus_per_fisk.csv"

# create dataframe from csv file
# raw data
licence = pull_data_frame(licence_file, raw_path, True)
sedimentation = pull_data_frame(sedimentation_file, raw_path)
lice = pull_data_frame(lice_file, raw_path)

# rename the columns we want to study more
licence.rename(columns=translation_dict_licence, inplace=True)
lice.rename(columns=translation_dict_lice, inplace=True)
sedimentation.rename(columns=translation_dict_sediment, inplace=True)

print(licence.head())
print(sedimentation.head())
print(lice.head())


# Clean Dataset characters, want to add the option to do change ("char1" with "char2" and only suply file)

clean_dataset_char(licence, ",", ".", "location_capasity")
clean_dataset_char(licence, " ", "", "location_capasity")
clean_dataset_char(licence, ",", ".", "TILL_KAP")
clean_dataset_char(licence, " ", "", "TILL_KAP")


# Add Type Of Data to files

lice["instance_type"] = "Lusetelling"
sedimentation["instance_type"] = "sedimentation"

# *** Sorting ***#
# Sort out the licences with salmon (Biomass allowed is noted on the salmon values) we only want salmon and seawater
licence = licence.loc[
    (licence["location_species"] == "Laks") & (licence["VANNMILJØ"] == "SALTVANN")
]


# Sort by location name and number
licence = licence.set_index(["location_name", "location_number"]).sort_index()
sedimentation = sedimentation.set_index(["location_name", "location_number"]).sort_index()
lice = lice.set_index(["location_name", "location_number"]).sort_index()

# change time in sedimentation data to week
sedimentation["time"] = sedimentation["time"].apply(fromDateToWeek)

print(licence.head())
print(sedimentation.head())
print(lice.head())

# Saving data into the interim_path
push_data_frame("licence.csv", licence, interim_path)
push_data_frame("sedimentation.csv", sedimentation, interim_path)
push_data_frame("lice.csv", lice, interim_path)
