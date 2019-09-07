##This Program is written by Abubakr Shafique (abubakr.shafique@gmail.com)
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#This Histogram Function Takes in a Mat Image and Calculate Histogram
def Calculate_Histogram(Image):
	Image_Height = Image.shape[1] #get the Height of the Image
	Image_Width = Image.shape[0] #get the Width of the Image

	HistB = np.zeros([256], np.int32) #Initialize an empty 256 array for Blue Channel
	HistG = np.zeros([256], np.int32) #Initialize an empty 256 array for Green Channel
	HistR = np.zeros([256], np.int32) #Initialize an empty 256 array for Red Channel
	
	for x in range(0,Image_Width): # loop through the Image
		for y in range(0,Image_Height):
			HistB[Image[x,y,0]] +=1 # increment the same intensity values in Blue Channel
			HistG[Image[x,y,1]] +=1 # increment the same intensity values in Green Channel
			HistR[Image[x,y,2]] +=1 # increment the same intensity values in Red Channel
	
	return HistB, HistG, HistR #return the histogram
	
def Plot_Histogram(Histogram_Blue, Histogram_Green, Histogram_Red):
	plt.figure()
	plt.title("BGR Histogram")
	plt.xlabel("Intensity Level")
	plt.ylabel("Intensity Frequency")
	plt.xlim([0, 256]) # Defined the limit of x-axis
	plt.plot(Histogram_Blue, 'b')
	plt.plot(Histogram_Green, 'g')
	plt.plot(Histogram_Red, 'r')
	plt.savefig("ColorImage_Histogram.jpg")

def main():
	Input_Image = cv.imread('Test_Image.png') #This will read an Image
	Histogram_Blue, Histogram_Green, Histogram_Red = Calculate_Histogram(Input_Image)

	for i in range(0,len(Histogram_Blue)):
		print('HistogramBlue[',i,']: ', Histogram_Blue[i])
	for i in range(0,len(Histogram_Green)):
		print('HistogramGreen[',i,']: ', Histogram_Green[i])
	for i in range(0,len(Histogram_Red)):
		print('HistogramRed[',i,']: ', Histogram_Red[i])
	Plot_Histogram(Histogram_Blue, Histogram_Green, Histogram_Red)	
	input("Press Enter to continue...")


if __name__ == '__main__':
	main() #Our main function