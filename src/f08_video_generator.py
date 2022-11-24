from functions_and_parameters import video_read_path, os
import cv2

w = 1920
h = 1440
FPS = 26


image_folder = video_read_path
full_out_path = image_folder / "video"
video_name = "aaa.mp4"

os.chdir(image_folder)
images = []
for i in os.listdir(image_folder):
    if i.endswith(".png"):
        images.append(i)
images.sort()
print(images)

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), FPS, (w,h))

for i in range(len(images)):
    video.write(cv2.imread(images[i]))
    print("frame", i+1, "of", len(images),"done")


video.release()
print("video done")