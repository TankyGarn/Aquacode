# The goal of this file is to pull licence data, and find out the production tonnage of each company.
from functions_and_parameters import*
licence_file = "licence.csv"


licence_dataframe = pull_data_frame(licence_file,interim_path,seperator=",")

print(licence_dataframe.columns)
"""licence_dataframe.pop(['location_name', 'location_number', 'TILL_NR', 'ORG.NR/PERS.NR', 'ADRESSE', 'POSTNR', 'POSTSTED',
       'TILDELINGSTIDSPUNKT', 'TIDSBEGRENSET','TILL_KOMNR', 'FORMÅL', 'location_purpose',
       'location_species', 'TILL_KAP', 'TILL_ENHET', 'LOK_KOMNR', 'LOK_KOM',
       'LOK_PLASS', 'VANNMILJØ','location_capasity_unit'])
"""
owner_capasity_location = licence_dataframe[['location_name','location_owner','location_capasity','location_lattitude','location_longditude','production_area']]
owner_capasity_location = owner_capasity_location.drop_duplicates(['location_name'])


owner_capasity_location.groupby('location_owner')

grouped_owner_capasity_location = owner_capasity_location.set_index(['location_owner'])
grouped_owner_capasity_location=  grouped_owner_capasity_location.sort_index()

saved_owner_capasity = grouped_owner_capasity_location.groupby("location_owner")["location_capasity"].sum()
print(saved_owner_capasity)

list_saved_owner_capasity_nr = saved_owner_capasity.tolist()

print(list_saved_owner_capasity_nr)



list_saved_owner_capasity = saved_owner_capasity.index.values.tolist()

print(list_saved_owner_capasity)
new_list = []
for i in range(len(list_saved_owner_capasity)):
    new_list.append([list_saved_owner_capasity_nr[i], list_saved_owner_capasity[i]])
1
print(new_list)