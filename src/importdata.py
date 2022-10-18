from timesorting import fromDateToWeek
import pandas

#importing the csv files from "../data/raw/Fiskeridirektoratet/"

## i had some issues due to other format than the other csv files, made it work using the correct seperator and skipping the first row.
licence = pandas.read_csv("../data/raw/Fiskeridirektoratet/Akvakulturregisteret.csv", sep=";" , skiprows=[0])
sedimentation = pandas.read_csv("../data/raw/Fiskeridirektoratet/Historiske_B-undersøkelser.csv",sep=";")
lice  = pandas.read_csv("../data/raw/Fiskeridirektoratet/lakselus_per_fisk.csv",sep=";")

#Cleaning caracters pre sorting
licence["LOK_KAP"] = licence["LOK_KAP"].str.replace(',','.')
licence["LOK_KAP"] = licence["LOK_KAP"].str.replace(' ','')



#*** Sorting ***#


# Sort out the licences with salmon (Biomass allowed is noted on the salmon values) we only want salmon and seawater
cleaned_licence = licence.loc[(licence['ART']=="Laks") & (licence["VANNMILJØ"]=="SALTVANN")]



# Sort by location name and number
sorted_licence = cleaned_licence.set_index(["LOK_NAVN","LOK_NR"]).sort_index()
sorted_sedimentation = sedimentation.set_index(["navn","loknr"]).sort_index()
sorted_lice = lice.set_index(["Lokalitetsnavn","Lokalitetsnummer"]).sort_index()

#change time in sedimentation data to week
sorted_sedimentation["mu_dato"] = sorted_sedimentation["mu_dato"].apply(fromDateToWeek)

###Sending Data to 0_interim
sorted_licence.to_csv("../data/interim/sorted_licence.csv") 
sorted_sedimentation.to_csv("../data/interim/sorted_sedimentation.csv")
sorted_lice.to_csv("../data/interim/sorted_lice.csv")