import pandas as pd

data_path = directory_path / ".." / "data"
raw_path = data_path / "raw" / "FDIR"
own_path = data_path / "raw" / "OWN"
interim_path = data_path / "interim"


df_samlet = pd.merge(df_sortedLicence, df_sortedLice)

print(df_samlet)

df_samlet.to_csv("../data/interim/combined_raw_licence_lice.csv")
print("/combined_raw_licence_lice.csv is generated.")
