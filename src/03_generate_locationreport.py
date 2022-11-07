import pandas as pd

df_sortedLicence = pd.read_csv("../data/interim/sorted_licence.csv")
df_sortedLice = pd.read_csv("../data/interim/sorted_lice.csv")
df_sortedLicence.rename(
    columns={
        "LOK_NR": "Lokalitetsnummer",
        "LOK_NAVN": "Location_Name",
        "TILL_NR": "Licence_Id",
        "ORG-NR/PERS.NR": "Buisness_Id",
        "NAVN": "Buisness_Name",
        "Adresse": "Adress",
        "POSTNR": "Area_Code",
        "POSTSTED": "Area_Name",
        "TILDELINGSPUNKT": "Licence_Startdate",
        "LOK_KOMNR": "Municipality_ID",
        "LOK_KOM": "Municipality_Name",
        "LOK_KAP": "Municipality_Capacity",
    },
    inplace=True,
)


df_samlet = pd.merge(df_sortedLicence, df_sortedLice)

print(df_samlet)

df_samlet.to_csv("../data/interim/combined_raw_licence_lice.csv")
print("/combined_raw_licence_lice.csv is generated.")
