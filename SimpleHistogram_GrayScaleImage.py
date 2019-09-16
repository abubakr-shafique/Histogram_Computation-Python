# This program is written by Abubakr Shafique (abubakr.shafique@gmail.com) 
import numpy as np	#This is to deal with numbers and arrays
import cv2 as cv	#This is to deal with images
from matplotlib import pyplot as plt

def Histogram_Computation(Image):
	Image_Height = Image.shape[0]
	Image_Width = Image.shape[1]
	
	Histogram = np.zeros([256], np.int32)
	
	for x in range(0, Image_Height):
		for y in range(0, Image_Width):
			Histogram[Image[x,y]] +=1
	
	return Histogram

def Plot_Histogram(Histogram):
	plt.figure()
	plt.title("GrayScale Histogram")
	plt.xlabel("Intensity Level")
	plt.ylabel("Intensity Frequency")
	plt.xlim([0, 256])
	plt.plot(Histogram)
	plt.savefig("Histogram_GrayScale.jpg")

def main():
	Input_Image = cv.imread("Test_Image.png",0) # This is to read Gray Scale Image
	
	Histogram_GrayScale = Histogram_Computation(Input_Image)
	
	#Now to print our output Histogram
	for i in range(0,len(Histogram_GrayScale)):
		print("Histogram[",i,"]: ", Histogram_GrayScale[i])
	Plot_Histogram(Histogram_GrayScale)
	input("Please Enter to Continue...")
	

if __name__ == '__main__':
	main()