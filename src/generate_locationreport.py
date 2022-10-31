import pandas as pd

df_sortedLicence = pd.read_csv("../data/interim/sorted_licence.csv")
df_sortedLice = pd.read_csv("../data/interim/sorted_lice.csv")
df_sortedLicence.rename(columns = {'LOK_NR':'Lokalitetsnummer', 'LOK_NAVN':'Location_Name', 'TILL_NR':'Licence_Id', 'ORG-NR/PERS.NR':'Buisness_Id', 'NAVN':'Buisness_Name', 'Adresse':'Adress', 'POSTNR':'Area_Code', 'POSTSTED':'Area_Name','TILDELINGSPUNKT':'Licence_Startdate', 'LOK_KOMNR':'Municipality_ID','LOK_KOM':'Municipality_Name', 'LOK_KAP':'Municipality_Capacity',    }, inplace = True)

# A function that takes input location ID and ColumbName (Index of collumb of interest)
def returnColumbData(LocationID,ColumbName,columbIndex):
    checkup = df_sortedLicence[df_sortedLicence["LOK_NR"]==LocationID]
    return (checkup[ColumbName][checkup.index[columbIndex]])
# not sure if usefull.
def returnColumbDataLice(LocationID,ColumbName,columbIndex):
    checkup = df_sortedLice[df_sortedLice["Lokalitetsnummer"]==LocationID]
    return (checkup[ColumbName][checkup.index[columbIndex]])

df_samlet = pd.merge(df_sortedLicence,df_sortedLice)
print(df_sortedLice)
print(df_sortedLicence)
print(df_samlet)

df_sortedLice.to_csv("../data/interim/combined_raw_licence_lice.csv")

"""
DictFromLicence={
    "Location_Name" : "LOK_NAVN",
    "Location_Owner" : "NAVN",
    "Municipalty_Name" : "TILL_KOM",
    "Municipalty_Num" : "TILL_KOMNR",
    "MaxBiomassLicence" : "LOK_KAP",
    "ProductionArea": "PROD_OMR",
    "Latitude" : "N_GEOWGS84",
    "Longitude" : "Ø_GEOWGS84"
    
}
DictFromLice={
    "Instancetype" : "INSTANCETYPE",
    "Location_Name" :"Lokalitetsnavn",
    "Adult_Female_Lice" : "Voksne hunnlus",
    "Other_Mobile_Lice" : "Lus i bevegelige stadier",
    "Unmobile_Lice" : "Fastsittende lus"
}
# Create a list of the 1. element in each of the rows
# add the datalist together with the new list
# Create a list of the 2. element in each of the rows.

keysList = list(DictFromLicence.keys())+list(DictFromLice.keys())

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
mainList = pd.DataFrame(columns=keysList)

def appendOneTimeDataToList(LocationID):
    for key in DictFromLicence:
        dataList.append(returnColumbData(LocationID,DictFromLicence[key],0))
    return dataList

def LappendOneTimeDataToList(LocationID):
    for key in DictFromLice:
        dataList.append(returnColumbDataLice(LocationID,DictFromLice[key],0))
    return dataList
   
def addLocationDataToMainList(LocationID):
    LappendOneTimeDataToList(LocationID)
    appendOneTimeDataToList(LocationID)
    mainList.append(dataList)

addLocationDataToMainList(30096)

print(mainList)

"""