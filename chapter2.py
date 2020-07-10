# Importing Package(s)
import cv2
import numpy as np
print('Package(s) Imported')

# Basic Functions
img = cv2.imread('Resources/me.jpg')
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Gray Scaled Image
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)    # Blurred Image, (7,7) - Kernel Size (always Odd), 0 - SigmaX
imgCanny = cv2.Canny(img, 100, 100) # Edge Detector
imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1) # Dialate the Image
imgEroded = cv2.erode(imgDialation, kernel, iterations = 1) # Erode the Image (opposite of dialation)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)