import pandas as pd

df_sortedLicence = pd.read_csv("../data/interim/sorted_licence.csv")
df_sortedLice = pd.read_csv("../data/interim/sorted_lice.csv")

# A function that takes input location ID and ColumbName (Index of collumb of interest)
def returnColumbData(LocationID,ColumbName,columbIndex):
    checkup = df_sortedLicence[df_sortedLicence["LOK_NR"]==LocationID]
    return (checkup[ColumbName][checkup.index[columbIndex]])



TitleDictOnetimeLicence= {
    "Location_Name" : "LOK_NAVN",
    "Location_Owner" : "NAVN",
    "Municipalty_Name" : "TILL_KOM",
    "Municipalty_Num" : "TILL_KOMNR",
    "MaxBiomassLicence" : "LOK_KAP",
    "ProductionArea": "PROD_OMR",
    "Latitude" : "N_GEOWGS84",
    "Longitude" : "Ø_GEOWGS84"
    
}
TitleDictEveryTime={
    "Instancetype" : "INSTANCETYPE",
    "Location_Name" :"Lokalitetsnavn",
    "Adult_Female_Lice" : "Voksne hunnlus",
    "Other_Mobile_Lice" : "Lus i bevegelige stadier",
    "Unmobile_Lice" : "Fastsittende lus"
}
# Create a list of the 1. element in each of the rows
# add the datalist together with the new list
# Create a list of the 2. element in each of the rows.

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


# Pseudocode completion 
dataList = []
# function that makes a pandas dataframe based on a locationnumber 
mainList = []

def appendOneTimeDataToList(LocationID):
    for key in TitleDictOnetimeLicence:
        dataList.append(returnColumbData(LocationID,TitleDictOnetimeLicence[key],0))
    return dataList
    

   
        


print(appendOneTimeDataToList(15196))
