# This is the 8.th file in the project
# -*- coding: utf-8 -*-
# Authors: Taohong Liao and Nikolai Vestbøstad
# Date: 2022.10.25
# Updated: 2022.10.31
# *** File purpose ***#
""" 
Aim: The goal with this file is to put individual frames into one video.

How achived:
   use cv2 to achive production

What to improve:

looks like there might be some bugs
related to order in video, some dates are jumping around.

"""
# *** Importing Packages ***#


from functions_and_parameters import video_read_path, visualisation_path, os
import cv2

# *** Define parameters ***#

w = 1920
h = 1440
FPS = 14
videoname = "lice_in_norway"
format = "mp4"


# *** Defining Functions ***#
def createVideoFromPNG(videoname,image_folder,width,height,fps,format="mp4"):
    video_name = f"{videoname}.{format}"

    os.chdir(image_folder)
    images = []
    for i in os.listdir(image_folder):
        if i.endswith(".png"):
            images.append(i)
    images.sort()


    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), fps, (width,height))

    for i in range(len(images)):
        video.write(cv2.imread(images[i]))
        print("f08_videogenerator: frame", i+1, "of", len(images),"done")

    video.release()
    print(f"{videoname} video done")

# *** Load Data ***#
createVideoFromPNG(videoname,video_read_path,w,h,FPS)



# *** Save Data *** #

