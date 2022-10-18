import pandas as pd

sl = pd.read_csv("../data/interim/sorted_licence.csv")

#Generate The headers of the new dataset (width 12)
listTitles = ["LocationName",
"LocationNumber",
"Owner",
"ProductionAreaNumber",
"Municipality",
"MaxBiomassLicence",
"MaxBiomassLocation",
"InstaceType",
"WeekNR",
"Year",
"SedimentationLevel",
"Licecount",
"SedimentationAlarmLevel",
"LiceAlarmLevel",
"IsFish",
"Latitude",
"Longditude",
"URLmom",
"SeaTemperature",
"SealiceLimit"
]


# We need to write the fetching code for each of these, some will need to be done for every single new line, others will be done for each new location

# Lets begin with the one time to storage data


#Can we create a object to do this????? (since it is just repetition of data with one swap on every new collumb name)
def getLocationName(LocationID):
    #Checkup if there is a location number and return a df with every single location with that id
    checkup = sl[sl["LOK_NR"]==LocationID]
    #Return the first Location number in that list.
    return(checkup["LOK_NAVN"][checkup.index[0]])

def getOwner(LocationID):
    checkup = sl[sl["NAVN"]==LocationID]
    return(checkup["NAVN"][checkup.index[0]])

def getLatitude(LocationID):
    checkup = sl[sl["N_GEOWGS84"]==LocationID]
    return(checkup["N_GEOWGS84"][checkup.index[0]])


"""
LocationName = 
LocationNumber = 
Owner = 
ProductionAreaNumber = 
Municipality = 
MaxBiomassLicence =
MaxBiomassLocation =
InstanceType = 
WeekNr =
Year =
SedimentationLevel = 
Licecount = 
SedimentationAlarmLevel =
LiceAlarmLevel = 
IsFish =
Latitude =
Longditude =
URLmom =
SeaTemperature =
SealiceLimit =
"""

# Pseudocode completion 

# function that makes a pandas dataframe based on a locationnumber 
def generateDataList(LocationID):
    dataList = []
    dataList.append(getLocationName(LocationID))

    print(dataList)
    return dataList


generateDataList(10256)