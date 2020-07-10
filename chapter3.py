import cv2
import numpy as np
print('Package(s) Imported')

img = cv2.imread('Resources/lambo.jpg')
print(img.shape)

# Resize
imgResize = cv2.resize(img, (300,200))
print(imgResize.shape)

# Crop
imgCropped = img[200:300, 200:500]  # [Height,Width]

cv2.imshow('Lambooooooo', img)
cv2.imshow('Smol Lambooooooo', imgResize)
cv2.imshow('Image Cropped', imgCropped)
cv2.waitKey(0)