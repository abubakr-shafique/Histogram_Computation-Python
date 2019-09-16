# This Program is written by Abubakr Shafique (abubakr.shafique@gmail.com)
import numpy as np	#This is to deal with nimbers and arrays
import cv2 as cv	#This is to deal with Images
from matplotlib import pyplot as plt

def Histogram_Computation(Image):
	
	Image_Height = Image.shape[0]
	Image_Width = Image.shape[1]
	Image_Channels = Image.shape[2]
	
	Histogram = np.zeros([256, Image_Channels], np.int32)
	
	for x in range(0, Image_Height):
		for y in range(0, Image_Width):
			for c in range(0, Image_Channels):
					Histogram[Image[x,y,c], c] +=1
	
	return Histogram

def Plot_Histogram(Histogram):
	plt.figure()
	plt.title("Color Image Histogram")
	plt.xlabel("Intensity Level")
	plt.ylabel("Intensity Frequency")
	plt.xlim([0, 256])
	plt.plot(Histogram[:,0],'b') # This is to Plot Blue Channel with Blue Color
	plt.plot(Histogram[:,1],'g') # This is to Plot Green Channel with Green Color
	plt.plot(Histogram[:,2],'r') # This is to Plot Red Channel with Red Color
	plt.savefig("Color_Histogram.jpg")


def main():
	Input_Image = cv.imread("Test_Image.png") #This will read a color Images
	
	Histogram = Histogram_Computation(Input_Image)

	#Now to print our result
	for i in range(0, Histogram.shape[0]):
		for c in range(0, Histogram.shape[1]):
			print("Histogram[", i, ", ", c, "]: ", Histogram[i,c])
			
	Plot_Histogram(Histogram)
	input("Please Enter to Continue...")
if __name__ == '__main__':
	main()
