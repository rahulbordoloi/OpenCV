import cv2
import numpy as np
print('Package(s) Imported')

img = np.zeros((512,512,3), np.uint8)  # 0 - Black

'''print(img.shape)
img[:] = 255,0,0  # Colours the Image as Blue
# img[200:300, 40:200] = 255,0,0'''

# Draw a Line
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0))  # Image, Starting pt, Ending Pt, Colour of Line (Green Here).  
# Draw a Rectangle
cv2.rectangle(img, (0,0), (250,350), (0,0,255), cv2.FILLED)  # can replace cv2.FILLED with any numeric value for thickness
# Draw a Circle
cv2.circle(img, (400,50), 30, (255,255,0), 5)  # 30 is radius here, (255,255,0) - Blue
# Input Text
cv2.putText(img, " OPENCV ", (300,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 1) # scale, colour, thickness


cv2.imshow('Image', img)
cv2.waitKey(0)