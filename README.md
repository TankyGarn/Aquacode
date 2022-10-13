# Researching Enviormental Impact arround Aquactulturesites 
## TEP4221 - Sustainability Analysis
### Tue , 11.10.2022

Nikolai Vesbøstad, nikolv@stud.ntnu.no


# Keywords:
Aquaculture; 
Environmental impacts of Food production; 
Seabed monitoring; 
Salmon Lice; 
Marine Biology;

Sustainable Goal number 14 - Life Below Water

## Project overview
```
Per 13.10.2022

├── README.md
├── data
│   ├── auxiliary
│   ├── interim
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
│   └── 02_timesorting.py
└── visualisation

8 directories, 9 files
```


## Introduction
Introduction to your project. Thoughts behind your research question and why it relates to sustainability.

### Research question
> Write your research question here
 
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

## Conclusion
The main conclusions of your analysis and how they answer your research question.


See [markdownguide.org](markdownguide.org/basic-syntax) for formatting help.