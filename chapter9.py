import cv2

faceCascade = cv2.CascadeClassifier('D:\Studies (Contd.)\Projects\OpenCV\Resources\haarcascades\haarcascade_frontalface_default.xml')
img = cv2.imread('Resources/me.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)    # 1.1 - Scale Factor, 4 - Minimum Neighbours

for (x,y,w,h) in faces:                                # for boxes around faces 
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)