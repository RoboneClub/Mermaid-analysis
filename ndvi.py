import cv2
import numpy as np
from fastiecm import fastiecm
from pathlib import Path

# Function to increase contrast in an image
def contrast_stretch(im):
  in_min = np.percentile(im, 5)
  in_max = np.percentile(im, 95)

  out_min = 0.0
  out_max = 255.0

  out = im - in_min
  out *= ((out_min - out_max) / (in_min - in_max))
  out += in_min

  return out

# Function to calculate NDVI
def calc_ndvi(image):
  b, g, r = cv2.split(image)
  bottom = (r.astype(float) + b.astype(float))
  bottom[bottom == 0] = 0.01
  ndvi = (b.astype(float) - r) / bottom
  return ndvi
# Function to color map an image
def color_map(img):
  color_mapped_prep = img.astype(np.uint8)
  return cv2.applyColorMap(color_mapped_prep, fastiecm)

# Function to apply NDVI
def ndvi(img_full_path):
  original = cv2.imread(img_full_path)
  contrasted = contrast_stretch(original)
  ndvi = calc_ndvi(contrasted)
  ndvi_contrasted = contrast_stretch(ndvi)
  color_mapped_image = color_map(ndvi_contrasted)
  return color_mapped_image  

"""A loop to apply NDVI to the images and save them"""
base_folder = Path(__file__).parent.resolve()

counter = 1
while(counter <= 326):
    try:
        y = ndvi(f"{base_folder}\\image_{counter}.jpg")
        cv2.imwrite(f"color_map_img_{counter}.jpg",y)
        print(f"Succeded in opening image {counter}")
        counter = counter + 1
    except Exception as e:
        print(f"failed to open image {counter}/n{e}")
        counter = counter + 1