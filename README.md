# Researching Enviormental Impact arround Aquactulturesites 
## TEP4221 - Sustainability Analysis
### Tue , 11.10.2022

Nikolai Vesbøstad, nikolv@stud.ntnu.no
Taohong Liao, taohongl@stud.ntnu.no

# Keywords:
Aquaculture; 
Environmental impacts of Food production; 
Seabed monitoring; 
Salmon Lice; 
Marine Biology;

Sustainable Goal number 14 - Life Below Water

## Project overview
```
Per 31.10.2022
.
├── README.md
├── data
│   ├── auxiliary
│   ├── interim
│   │   ├── df_lice_and_licence.csv
│   │   ├── lice.csv
│   │   ├── lice_location_state_owner_dataframe.csv
│   │   ├── lice_location_state_owner_dataframe.py
│   │   ├── licence.csv
│   │   ├── reduced_lice_dataframe.csv
│   │   ├── sedimentation.csv
│   │   └── test.csv
│   └── raw
│       ├── FDIR
│       │   ├── Akvakulturregisteret.csv
│       │   ├── Historiske_B-undersøkelser.csv
│       │   └── lakselus_per_fisk.csv
│       └── OWN
├── docs
│   ├── Worklog.txt
│   └── requirements.txt
├── requirements.txt
├── src
│   ├── __pycache__
│   │   ├── f04_process_data.cpython-311.pyc
│   │   ├── f04_process_data.cpython-38.pyc
│   │   ├── f04_process_data.cpython-39.pyc
│   │   ├── functions_and_parameters.cpython-311.pyc
│   │   ├── functions_and_parameters.cpython-38.pyc
│   │   ├── functions_and_parameters.cpython-39.pyc
│   │   ├── loadingdata.cpython-38.pyc
│   │   ├── loadingdata.cpython-39.pyc
│   │   ├── timesorting02.cpython-38.pyc
│   │   └── timesorting02.cpython-39.pyc
│   ├── f00_mainfile
│   ├── f01_importdata.py
│   ├── f02_generate_locationreport.py
│   ├── f03_clean_data.py
│   ├── f04_process_data.py
│   ├── f05_studylocation.py
│   ├── f06_main.py
│   ├── f07_lice_over_time.py
│   ├── f08_video_generator.py
│   ├── functions_and_parameters.py
│   ├── generic_functions.py
│   ├── projecttep_envionment.yml
│   └── test.py
└── visualisation
    └── video
10 directories, 26 files
```


## Introduction
In this project we are to clean, sort and utalize data coming from the salmonindustry in norway, we have three datasets which cover different aspects of sustainability. Ownership, Site Health and sealice data onsites. 

### Research question
> We want to compare enviormental impact of locations looking at salmon lice data and sedimentation analysis data. Then we want to compare inbetween different locations, companies and regions, to find out if they could be used as a factor for "trafikklyssystemet".


## conda env
Run this:

conda activate projecttep_envionment







## Datasets
Describe your datasets
* where do they come from?
* * what version(s) are you using?
* what are they used for?
* * Dataset 1: 
    File: Fiskeridirektoratet/Historiske_B-undersøkelser.csv
    Downloaded(link/date): https://open-data-fiskeridirektoratet-fiskeridir.hub.arcgis.com/datasets/702d94e4835041d0a01be603862484b4/explore?location=64.359884%2C17.537900%2C7.09 / 07.10.2022
    TL:DR : File that documents the enviormental surveying close to aquaculturesites.
    How to download:/last ned/csv/Nedlastningsalternativer/Generer ny nedlastning med de nyeste dataene.
    

    Dataset 2: 
    File: Fiskeridirektoratet/Akvakulturregisteret.csv
    Downloaded(link/date):https://www.fiskeridir.no/Akvakultur/Registre-og-skjema/Akvakulturregisteret / 11.10.2022
    TL;DR: file that documents who owns the different licences on locations.
    How to download: scroll down, find "Akvakulturregisteret i nedlastbare filer.", then click the one with .csv.

    Dataset 3: 
    File: Fiskeridirektoratet/Lakselus_per_fisk.csv
    Downloaded(link/date): https://www.barentswatch.no/nedlasting/fishhealth/lice / 11.10.2022
    TL;DR: file that documents every single salmoncount.
    How to download:click "Alle lokaliteter med laksefisk", time from 1/2012 til today, chose format csv.

## Challenges
Clean data to same time method.
    *Change all time to week number.


Make a program that gives a plot wich shows the allowed production in different regions / companies
    subgoals:
        * 

Make a program that makes it posible to generate a location report that gives a report wich shows plots with relevant data like:

* Owner of Location
* map location
* Sealice history
* MOMB - data (seabed conditions) with timeline
* Production capacity
   



## Visualisations
Your figures and tables, including captions.

[Example of lice production over time.](visualisation/Aldalen_Voksne_hunnlus.png)
(how do i add images to .md files...)



## Conclusion
The main conclusions of your analysis and how they answer your research question.

Stuff to do before project is done:
    Clean up hiarchu

See [markdownguide.org](markdownguide.org/basic-syntax) for formatting help.