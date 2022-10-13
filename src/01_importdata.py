import pandas

#importing the csv files from "../data/raw/Fiskeridirektoratet/"

## i had some issues due to other format than the other csv files, made it work using the correct seperator and skipping the first row.
licence_registry = pandas.read_csv("../data/raw/Fiskeridirektoratet/Akvakulturregisteret.csv", sep=";" , skiprows=[0])
sedimentation = pandas.read_csv("../data/raw/Fiskeridirektoratet/Historiske_B-undersøkelser.csv",sep=";")
salmon_lice  = pandas.read_csv("../data/raw/Fiskeridirektoratet/lakselus_per_fisk.csv",sep=";")

# Sort out the licences with salmon (Biomass allowed is noted on the salmon values) we only want salmon and seawater
salmon_licences = licence_registry.loc[(licence_registry['ART']=="Laks") & (licence_registry["VANNMILJØ"]=="SALTVANN")]

###Sending Data to 0_interim
salmon_licences.to_csv("../data/interim/salmon_licence.csv") 

