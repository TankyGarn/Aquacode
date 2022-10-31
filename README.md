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
├── Worklog.txt
├── data
│   ├── auxiliary
│   ├── interim
│   │   ├── combined_raw_licence_lice.csv
│   │   ├── sorted_lice.csv
│   │   ├── sorted_licence.csv
│   │   └── sorted_sedimentation.csv
│   └── raw
│       └── Fiskeridirektoratet
│           ├── Akvakulturregisteret.csv
│           ├── Historiske_B-undersøkelser.csv
│           └── lakselus_per_fisk.csv
├── docs
├── src
│   ├── 01_importdata.py
│   ├── 03_generate_locationreport.py
│   ├── __pycache__
│   │   ├── timesorting.cpython-38.pyc
│   │   └── timesorting.cpython-39.pyc
│   ├── structure
│   │   ├── 00_main.py
│   │   ├── 01_clean_data.py
│   │   ├── 02_process_data.py
│   │   ├── 03_analyse_data.py
│   │   └── generic_functions.py
│   ├── test.py
│   └── timesorting02.py
└── visualisation
    ├── Aldalen_Voksne_hunnlus.png
    ├── Fastsittende_lus.png
    ├── Lus_i_bevegelige stadier.png
    ├── Nautvik_Voksne_hunnlus.png
    ├── Voksne_hunnlus.png
    └── map.png

10 directories, 26 files


## Introduction
In this project we are to clean, sort and utalize data coming from the salmonindustry in norway, we have three datasets which cover different aspects of sustainability. Ownership, Site Health and sealice data onsites. 

### Research question
> 



## Datasets
Describe your datasets
* where do they come from?
* * what version(s) are you using?
* what are they used for?
* * Dataset 1: 
    File: Fiskeridirektoratet/Historiske_B-undersøkelser.csv
    Downloaded(link/date): https://www.fiskeridir.no/Tall-og-analyse/AApne-data / 11.10.2022
    TL:DR : File that documents the enviormental surveying close to aquaculturesites.

    Dataset 2: 
    File: Fiskeridirektoratet/Akvakulturregisteret.csv
    Downloaded(link/date):https://www.fiskeridir.no/Akvakultur/Registre-og-skjema/Akvakulturregisteret / 11.10.2022
    TL;DR: file that documents who owns the different licences on locations.

    Dataset 3: 
    File: Fiskeridirektoratet/Lakselus_per_fisk.csv
    Downloaded(link/date): https://www.barentswatch.no/nedlasting/fishhealth/lice / 11.10.2022
    TL;DR: file that documents every single salmoncount.


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