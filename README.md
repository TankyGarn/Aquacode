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
│   ├── f00_mainfile.py
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

10 directories, 26 files
```


## Introduction

>In this project we are to clean, sort and utalize data coming from the salmonindustry in norway, we have three datasets which cover different aspects of sustainability. Ownership, Site Health and sealice data onsites. 
>
>The industry has a great data analysis tool that is called barentswatch/fiskehelse (https://www.barentswatch.no/fiskehelse/?lang=en) . On this cite you can get alot of data by scrolling around. By building some of these tools in python as well we could automate more processes since its quicker than using mouse and keyboard as user input. 
>Since both of us students are studying aquaculture we used this course to build tools that we could use in our future projects. 

Since we were to combine datasets we needed to find indipendent data that looked at different states of sustainability, we chose sealice data since it is the main metric of sustainability in the sector. The sealice data are collected on each location of salmonfarming every week. The way they do the test is by catching 20 salmon in each seapen (there are usually 8-12 seapens each location), and counting how many sealice there are on each salmon. Using the avrage number of salmon per fish they can comply with the government regulations of a set amount of female mature sealice per location. 

We also looked at sedimentation data of locations, this data comes from indipendent companies that grade the location sedimentation (https://www.leroyseafood.com/en/sustainability/sustainability-library/protect-our-oceans/momb/). MOM-analysis usually is seen at a microscale since it selects the locations where sedimentation does not accumulate.

The last reasearchdata was the licenceregister for aquaculture in norway. The other datasets does not show who ownes the locations, and therefore we needed to use this dataset to give the companies name in the combined datasets. The reason why we think its usefull to use company names during analysis is that is makes it possible to see if the companies do things different on a macro scale. 

### Research question
1) We want to compare enviormental impact of locations looking at salmon lice data and sedimentation analysis data. 
2) We want to look at how the sealice situation grows over time.
3) We want to compare locations to see the lice situation.

## conda env
Run this:

conda activate projecttep_envionment

## Datasets
Describe your datasets
* where do they come from?
The datasets come from "fiskeridirektoratet" witch is the directory of fisheries under the government in Norway. The data is easily available. One of the weaknesses of this data is that we chose data from one sole provider.

* * what version(s) are you using?
To download the same versions of the datasets we were using you need to use legacy data, the data should work with new downloads as well since the code has a correct level of abstraction. 

* * Dataset 1: 
    File: Fiskeridirektoratet/Historiske_B-undersøkelser.csv
    Downloaded(link/date): https://open-data-fiskeridirektoratet-fiskeridir.hub.arcgis.com/datasets/702d94e4835041d0a01be603862484b4/explore?location=64.359884%2C17.537900%2C7.09 / 07.10.2022
    TL:DR : File that documents the enviormental surveying close to aquaculturesites.

    Dataset 2: 
    File: Fiskeridirektoratet/Akvakulturregisteret.csv
    Downloaded(link/date):https://www.fiskeridir.no/Akvakultur/Registre-og-skjema/Akvakulturregisteret / 11.10.2022
    TL;DR: file that documents who owns the different licences on locations.

    Dataset 3: 
    File: Fiskeridirektoratet/Lakselus_per_fisk.csv
    Downloaded(link/date): https://www.barentswatch.no/nedlasting/fishhealth/lice / 11.10.2022
    TL;DR: file that documents every single salmoncount.

## script by script.
### f00_mainfile
This file is made so that you dont need to run every single script by hand. if you would do

'python f00_mainfile' the entire script should run and all visualisations should be created.

### f01_importdata.py
This file takes in the different raw datafile and rinses them so they could be used later.

The naming convention of the different datasets (columnnames) are homogenized so they are the samethroughout the system.

### f02_generate_locationreport.py
Aim:
The aim for this file is to be able to make a location report that
shows a plot of lice over the history of the location.

This file is used for creating a plot for a locations lice history during its entire lifespan. This is also a file that has been used in other subjects to discuss difrences between locations. In the beginning of the project we thought we would autogenerate some form of location report that took in all data and printed it to a latex / pdf structure so it could be read when looking at locations, we did not go forward with this idea, but this would be a lice building block for that project.

'plot_for_location(location_number)' is a good function to get the history of a location.

### f03_generate_locationreport.py
Aim: generate a location plot that shows salmon lice at a location one year

'plot_lice_year(Location_name, year)' plots out an image with lice for a location in a given year.

### f04_process_data.py
Aim: 
* The aim of this file is to create a dataset that
is suitable for a scatterplot that could show  if there
is some correlation between high lice and high sedimentation levels

This achived by mergeing two datasets and pulling out given columns.

### f05_studylocation.py
The aim of this file is to create two scatter plots.

1. Plot: How to all locations distribute in a 
sedimentation level x lice concentration plot.

2. like the first plot, but group the locations in by company.
this will give us a view if some companies are using tactics.
wich can be used to compare how the different companies
align them selves concidering sedimentationlevel
and licelevel. 

This is possible due to the work done in f04_process_data.py

'plt.show()' is recomended on this plot because you can zoom in and see the individual companies.

### f06_check up with standard
 (this was removed due some techincal issues)


### f07_lice_overtime.py
Aim: The goal with this file is to generate a map animation that shows the
lice situation over time. This map will be generated for all locations.
And will be saved as a png

How to use, this file takes in a dataframe, chooses the files it wants to study and thereafter
generates one plot per time unit specified.

To use this in other ways you could change the parameter we want to look at. In this scenario we
it to look at mature lice per time, but it could equally as easy show daily temperature over
different cities. 

### f08_video_generator.py
Aim: The goal with this file is to put individual frames into one video.

How to use: This file takes in a file of images, sorts the images by filename and then puts each individual frame into a video.

'createVideoFromPNG()' is the function we use to do this, this is per now not a abstract thing, but should work for videos up to 999images.


## Challenges
Clean data to same time method.
    *Change all time to week number.

Learning to get the data we wanted from pandas dataframe.

From the beginning we had issues with not knowing what to do, our coding became much easier to write when we chose what we wanted to look after.


We wanted to make a program that makes it posible to generate a location report that gives a report wich shows plots with relevant data like:

    * Owner of Location
    * map location
    * Sealice history
    * MOMB - data (seabed conditions) with timeline
    * Production capacity



## Visualisations

[Aldalen lice 2022](visualisation/lice_Aldalen_2022.png)
lice_Aldalen_2022.png shows the mature female lice per fish from week1 to week40 in 2022 in location of Aldalen.

[Nautvik lice 2022](visualisation/lice_Nautvik_2022.png)
lice_Nautvik_2022.png shows the mature female lice per fish from week1 to week40 in 2022 in location of Nautvik.

[Generated plot of sealice from location øyra](visualisation/34697Øyralice.png)
34697Øyralice.png shows the maature female lice per fihs for location of Øyra from 2012 to 2022

[Scatterplots that plots companies based on their avg sealice and avg sedimentaition level](visualisation/company_plots_sedimentaion_sealice.png)
Scatterplots that plots companies based on their avg sealice and avg sedimentaition level

[This video is generated out of the week by week plots generated in f07](visualisation/video/lice_in_norway.mp4)
This video is generated out of the week by week plots generated in f07


## Conclusion

From week1 to week25, the mature female lice per fish is low in 2022 in Aldalen, but it is sharply high from week26. The location of Nautvik is just the opposite, the mature female lice per fish is high in 2022 in Nautvik from week1 to week25, and after that it becomes low. The two cases present that the situation of mature female lice per fish does not depend on the seasons. 

Øyralice shows that they have had 7 periods of salmon at their location, and that they have not had that many lice at their location. 

Lice concentration vs sedimentation level shows that the salmon producer MOWI is an outlier, statistical analysis is required to say anything about this. It might be just because of size MOWI sticks out. 


###
keypoints from the project:
    - If you are to do pairprogramming, get into the same workflow environment, this was lacking during our programming.
    - Choose the plots before you start thinking about code. We did not have a clear goal with this project, wich resulted in alot of unclear code, "doing something"
    - Matplotlib is not easy.

/Nikolai & Taohong


