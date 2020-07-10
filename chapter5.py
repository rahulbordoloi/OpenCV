import cv2
import numpy as np
print('Package(s) Imported')

img = cv2.imread('Resources/cards.jpg')

width, height = 250, 350     # Dimensions of the new image
pts1 = np.float32([[171,38],[292,67],[133,207],[252,237]])     # Define four corner points of the card 
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # Define the reference corners wrt to pts1
matrix = cv2.getPerspectiveTransform(pts1, pts2)               # Transformation Matrix
imgOutput = cv2.warpPerspective(img, matrix, (width,height))   # Get output image based on the matrix

cv2.imshow('Cards', img)
cv2.imshow('Output', imgOutput)
cv2.waitKey(0)