##This Program is written by Abubakr Shafique (abubakr.shafique@gmail.com)
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#This Histogram Function Takes in a Mat Image and Calculate Histogram
def Calculate_Histogram(Image):
	Image_Height = Image.shape[1] #get the Height of the Image
	Image_Width = Image.shape[0] #get the Width of the Image

	Hist = np.zeros([256], np.int32) #Initialize an empty 256 array
	
	for x in range(0,Image_Width): # loop through the Image
		for y in range(0,Image_Height):
			Hist[Image[x,y]] +=1 # increment the same intensity values
	
	return Hist #return the histogram

def Plot_Histogram(Histogram_GrayScale):
	plt.figure()
	plt.title("Grayscale Histogram")
	plt.xlabel("Intensity Level")
	plt.ylabel("Intensity Frequency")
	plt.xlim([0, 256]) # Defined the limit of x-axis
	plt.plot(Histogram_GrayScale)
	plt.savefig("GrayScale_Histogram.jpg")

def main():
	Input_Image = cv.imread('Test_Image.png',0) #This will read a GrayScale Image (Even if it is RGB it will read GrayScale)
	Histogram_GrayScale = Calculate_Histogram(Input_Image)

	for i in range(0,len(Histogram_GrayScale)):
		print('Histogram[',i,']: ', Histogram_GrayScale[i])
		
	Plot_Histogram(Histogram_GrayScale)
	input("Press Enter to continue...")

if __name__ == '__main__':
	main() #Our main function