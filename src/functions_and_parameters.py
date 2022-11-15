import os
from pathlib import Path
import pandas
import datetime

directory_path = Path(os.getcwd())
data_path = directory_path / ".." / "data"

def pull_data_frame(name_of_file, folder_path, skiprow=False, seperator = ";"):
    """Takes in a filename and returns a pandas dataframe from the csv file.

    Args:
        name_of_file (str): takes in a file in the format (".csv").
        folder_path (pathlib.PosixPAth) : Takes the path to where the file is located.
        skiprow (bool, optional): takes the optional argument skiprow True/False, Defaults to False.

    Returns:
        pandas dataframe: returns a pandas dataframe.
    """
    if skiprow is True:
        new_dataframe = pandas.read_csv(
            folder_path / name_of_file, sep= seperator, skiprows=[0]
        )
        print("skiprow = True")
    else:
        new_dataframe = pandas.read_csv(folder_path / name_of_file, sep = seperator)
        print("Skiprow = False")
    return new_dataframe


def push_data_frame(name_of_file, name_of_function, folder_path):
    """Takes in name, dataframe and path and saves the dataframe as a .csv file.

    Args:
        name_of_file (str): What should the name of the file be?
        name_of_function (Pandas Dataframe): takes in a dataframe that should be converted to .csv
        folder_path (pathlib.PosixPath): takes in a folderpath, where the file shal be saved.

    Returns:
        pathlib.PosixPath: returns a path.
        none: Generates a .csv file
    """
    new_path = folder_path / name_of_file

    name_of_function.to_csv(new_path)
    print(f"{name_of_file} has been generated at {new_path}")
    return new_path


# make function to clean all off the files... right now not so useful..
def clean_dataset_char(chosen_dataframe, char_from, char_to, columb_title=None):
    """Takes in a columb with and unwanted char and swaps it with a wanted char

    Args:
        chosen_dataframe (pandas...DataFrame): The dataframe you want
        columb_title (str): The collumb name with unwanted char in a  "COLUMBTITLE" format
        char_from (str): The unwanted char in a "char" format
        char_to (str): The wanted char in a "char" format

    Returns:
        pandas.core.frame.DataFrame: The dataframe with edited columns.
    """

    chosen_dataframe[columb_title] = chosen_dataframe[columb_title].str.replace(
        char_from, char_to
    )
    # print(f"the dataframes columb with the name ''{columb_title}'' has had it characters swapped from ''{char_from}'', to ''{char_to}''")
    return chosen_dataframe

def makeList (dataframe,index_string):
    new_dataframe = list(dataframe[index_string])
    return new_dataframe
    


# Take away the time of day; input: "2007/09/18 + time", output: "2007/09/18"
def removetime(date_time):
    date_ymdt = date_time.split(" ")
    return date_ymdt[0]


# Split date into year, month, day; input : "2007/09/18", output [2007,09,18]
def datelist(date):
    datelist = date.split("/")
    return datelist


# Give a list with [year,month,date] returns the weeknumber:  input:  [2022,10,13] return: [41,2022]
def toWeek(datelist):
    week = datetime.date(
        int(datelist[0]), int(datelist[1]), int(datelist[2])
    ).isocalendar()[1]
    year = int(datelist[0])
    year_week = [year, week]
    return year_week


# A funciton to combine the other functions into a single input instead of multiple
def fromDateToWeek(inputdate):
    return toWeek(datelist(removetime(inputdate)))

    
# Translate data names into future data.
translation_dict_lice = {
    "NAVN": "location_owner",
    "Lokalitetsnummer": "location_number",
    "Lokalitetsnavn": "location_name",
    "NONE": "location_capasity",
    "NONE": "location_capasity_unit",
    "Kommune": "location_municipality",
    "NONE": "location_purpose",
    "NONE": "location_species",
    "Lat": "location_lattitude",
    "Lon": "location_longditude",
    "NONE": "location_reportbuisness",
    "NONE": "location_state",
    "Voksne hunnlus": "lice_female_mature",
    "Lus i bevegelige stadier": "lice_movables",
    "NONE": "location_report_url",
    "År": "location_time_year",
    "Uke": "location_time_week",
    "NONE": "time",
    "ProduksjonsområdeId": "production_area",
    "Sjøtemperatur": "temperature",
}
translation_dict_sediment = {
    "NONE": "location_owner",
    "loknr": "location_number",
    "navn": "location_name",
    "NONE": "location_capasity",
    "NONE": "location_capasity_unit",
    "kommune": "location_municipality",
    "NONE": "location_purpose",
    "NONE": "location_species",
    "X": "location_lattitude",
    "Y": "location_longditude",
    "prodorgnavn": "location_reportbuisness",
    "loktilstand": "location_state",
    "NONE": "lice_female_mature",
    "NONE": "lice_movables",
    "url": "location_report_url",
    "NONE": "location_time_year",
    "NONE": "location_time_week",
    "mu_dato": "time",
    "NONE": "production_area",
    "NONE": "temperature",
}
translation_dict_licence = {
    "NAVN": "location_owner",
    "LOK_NR": "location_number",
    "LOK_NAVN": "location_name",
    "LOK_ENHET": "location_capasity",
    "LOK_KAP": "location_capasity_unit",
    "TILL_KOM": "location_municipality",
    "PRODUKSJONSFORM": "location_purpose",
    "ART": "location_species",
    "N_GEOWGS84": "location_lattitude",
    "Ø_GEOWGS84": "location_longditude",
    "NONE": "location_reportbuisness",
    "NONE": "location_state",
    "NONE": "lice_female_mature",
    "NONE": "lice_movables",
    "NONE": "location_report_url",
    "NONE": "location_time_year",
    "NONE": "location_time_week",
    "NONE": "time",
    "NONE": "production_area",
    "NONE": "temperature",
}

naming_list= [
    "location_owner",
    "location_number",
    "location_name",
    "location_capasity",
    "location_capasity_unit",
    "location_municipality",
    "location_purpose",
    "location_species",
    "location_lattitude",
    "location_longditude",
    #"location_reportbuisness",
    #"location_state",
    "lice_female_mature",
    "lice_movables",
    #"location_report_url",
    "location_time_year",
    "location_time_week",
    #"time",
    "production_area",
    "temperature",
]