#Importing libraries
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Reading the csv file
df = pd.read_csv("data_new.csv")


#Filtering the magnetic field data to reduce noise
df['gaussian_MagX'] = gaussian_filter1d(df['MagneticField_X'],sigma=30,mode='nearest')
df['gaussian_MagZ'] = gaussian_filter1d(df['MagneticField_Z'],sigma=30,mode='nearest')
df['median_MagY'] = df['MagneticField_Y'].rolling(3000).median()

#Creating an array with the average NDVI of each image
mean_ndvi = [0.61, 0.65, 0.62, 0.61, 0.63, 0.37, 0.57, 0.58, 0.6, 0.29, 0.25, 0.14, 0.14, 0.1, 0.06, 0.09, 0.09, 0.11, 0.11, 0.17, 0.14, 0.16, 0.12, 0.13, 0.11, 0.16, 0.19, 0.21, 0.26, 0.39, 0.59, 0.54, 0.6, 0.62, 0.58, 0.63, 0.64, 0.61, 0.59, 0.48, 0.57, 0.32, 0.2, 0.15, 0.15, 0.16, 0.24, 0.21, 0.18, 0.16, 0.16, 0.14, 0.15, 0.1, 0.14, 0.17, 0.12, 0.31, 0.16, 0.24, 0.2, 0.16, 0.27, 0.21, 0.18, 0.24, 0.28, 0.32, 0.27, 0.24, 0.34, 0.21, 0.16, 0.17, 0.2, 0.25, 0.16, 0.12, 0.15, 0.16, 0.16, 0.11, 0.09, 0.11, 0.09, 0.11, 0.1, 0.1, 0.11, 0.14, 0.14, 0.12, 0.17, 0.13, 0.13, 0.14, 0.12, 0.22, 0.33, 0.4, 0.55, 0.61, 0.42, 0.19, 0.16, 0.21, 0.44, 0.51, 0.34, 0.41, 0.2, 0.18, 0.44, 0.41, 0.33, 0.49, 0.58, 0.53, 0.16, 0.1, 0.18, 0.28, 0.46, 0.38, 0.1, 0.17, 0.14, 0.13, 0.16, 0.49, 0.4, 0.14, 0.37, 0.4, 0.44, 0.48, 0.17, 0.33, 0.28, 0.33, 0.4, 0.11, 0.57, 0.42, 0.39, 0.29, 0.43, 0.45, 0.16, 0.41, 0.28, 0.49, 0.48, 0.52, 0.48, 0.31, 0.33, 0.41, 0.32, 0.36, 0.46, 0.34, 0.52, 0.45, 0.47, 0.47, 0.52, 0.55, 0.53, 0.51, 0.51, 0.5, 0.42, 0.49, 0.52, 0.57, 0.65, 0.69, 0.66, 0.59, 0.58, 0.55, 0.6, 0.62, 0.52, 0.63, 0.59, 0.63, 0.58, 0.57, 0.53, 0.48, 0.44, 0.37, 0.37, 0.29, 0.3, 0.11, 0.27, 0.29, 0.18, 0.21, 0.28, 0.34, 0.34, 0.38, 0.39, 0.38, 0.39, 0.41, 0.4, 0.43, 0.4, 0.41, 0.44, 0.47, 0.48, 0.44, 0.5, 0.56, 0.55, 0.51, 0.51, 0.5, 0.48, 0.53, 0.56, 0.63, 0.56, 0.55, 0.32, 0.12, 0.12, 0.14, 0.11, 0.11, 0.1, 0.15, 0.25, 0.44, 0.15, 0.16, 0.18, 0.3, 0.2, 0.5, 0.25, 0.48, 0.51, 0.51, 0.51, 0.32, 0.33, 0.19, 0.29, 0.26, 0.29, 0.17, 0.31, 0.2, 0.35, 0.45, 0.24, 0.41, 0.49, 0.61, 0.67, 0.67, 0.66, 0.61, 0.56, 0.51, 0.49, 0.48, 0.41, 0.32, 0.37, 0.34, 0.39, 0.35, 0.42, 0.5, 0.54, 0.61, 0.62, 0.56, 0.55, 0.51, 0.5, 0.51, 0.54, 0.47, 0.52, 0.5, 0.51, 0.55, 0.53, 0.46, 0.54, 0.47, 0.52, 0.52, 0.43, 0.31, 0.21, 0.32, 0.32, 0.21, 0.19, 0.17, 0.17, 0.16, 0.1, 0.1, 0.13, 0.12, 0.11, 0.17, 0.07, 0.03, 0.04, -0.01, 0.0, 0.73, 0.01]

#Making a mask for data with images
mask = []
for i in df['Image_Id']:
    if type(i) is type(0.75):
        mask.append(False)
    elif  int(i.split("_")[1]) >=326:
        mask.append(False)
    else:
        mask.append(True)



#A function to create scatter plots of filtered magnetic feild strength
def plot ():

  plt.scatter(x=mean_ndvi,y= df['gaussian_MagX'][mask], color = "b" )
  plt.title("Magnetic Feild X")
  plt.xlabel("NDVI")
  plt.ylabel("Magnetic Feild Strength/T")
  plt.savefig('NDVI_and_MagX.png')
  plt.show()

  plt.scatter(x=mean_ndvi,y=df['median_MagY'][mask], color = "r" )
  plt.title("Magnetic Feild Y")
  plt.xlabel("NDVI")
  plt.ylabel("Magnetic Feild Strength/T")
  plt.savefig('NDVI_and_MagY.png')
  plt.show()

  plt.scatter(x=mean_ndvi,y=df['gaussian_MagZ'][mask], color = "g" )
  plt.title("Magnetic Feild Z")
  plt.xlabel("NDVI")
  plt.ylabel("Magnetic Feild Strength/T")
  plt.savefig('NDVI_and_MagZ.png')
  plt.show()

#Running the function
plot()