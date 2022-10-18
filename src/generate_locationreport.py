import pandas as pd

sl = pd.read_csv("../data/interim/sorted_licence.csv")


# A function that takes input location ID and ColumbName (Index of collumb of interest)
def checkupWithID(LocationID,ColumbName):
    checkup = sl[sl["LOK_NR"]==LocationID]
    return (checkup[ColumbName][checkup.index[0]])



TitleDict= {
    "Location_Name" : "LOK_NAVN",
    "Location_Owner" : "NAVN",
    "Municipalty_Name" : "TILL_KOM",
    "Municipalty_Num" : "TILL_KOMNR",
    "MaxBiomassLicence" : "LOK_KAP",
    "ProductionArea": "PROD_OMR",
    "Latitude" : "N_GEOWGS84",
    "Longitude" : "Ø_GEOWGS84",
    
}

#Generate The headers of the new dataset (width 12)
listTitrttles = ["LocationName",
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

"""
#Can we create a *WHAT IS THE NAME OF THE THING I AM THINKING ABOUT* to do this? 
#(since it is just repetition of data with one swap on every new collumb name)
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
dataList = []
# function that makes a pandas dataframe based on a locationnumber 


def appendDataToList(LocationID):
    for key in TitleDict:
        dataList.append(checkupWithID(LocationID,TitleDict[key]))
    return dataList
    

print(appendDataToList(15196))