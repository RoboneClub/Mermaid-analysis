import cv2
from pathlib import Path
import numpy as np

base_folder = Path(__file__).parent.resolve()

counter = 1

#A loop to calculate the average NDVI of each image
while(counter <= 326):
    try:
        filename = f"{base_folder}\\color_map_img_{counter}.jpg"
        img_data = cv2.imread(filename)
        B, G, R = cv2.split(img_data)
        divisor = (R.astype(float) + B.astype(float))
        divisor[divisor == 0] = 0.01 # Making sure we don't divide by zero!
        ndvi = (((R.astype(float) - B.astype(float))) / divisor) 
        with open('NDVI.txt', 'a') as f:
            #Saving the average NDVI in a text file
            f.write(f"Mean NDVI of img_{counter}: {round(ndvi.mean(),2)}\n")
        counter = counter + 1
    except Exception as e:
        print(f"failed to classify image {counter}/n{e}")
        counter = counter + 1
    

