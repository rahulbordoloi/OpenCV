# Importing Package(s)
import cv2
print('Package(s) Imported')

'''
# Image
img = cv2.imread('Resources/me.jpg')
cv2.imshow('Output', img)
cv2.waitKey(0)  # 0 - Inf. Delay 
'''

# Video
# cap = cv2.VideoCapture('Resources/my_video.mp4')   # From Local Drive

cap = cv2.VideoCapture(0)   # 0 - Default, ID no. of the webcam
cap.set(3, 640)  # 3 - ID no. of Width 
cap.set(4, 480)  # 4 - ID no. of Height
cap.set(10, 100) # 10 - ID no. of Brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
