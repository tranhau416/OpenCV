import cv2 as cv
import numpy as np

# img = cv.imread('Resources/Photos/Cat.jpg')
# cv.imshow('Cat', img)


black = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Black', black)

#1. Paint the image a certain colour
# black[200:300, 400:500] = 0,0,255
# cv.imshow('Green', black)

#2. Draw a Rectangle              
# cv.rectangle(black, (100,200), (300,400), (0,0,255),thickness=2)
cv.rectangle(black, (0,0), (black.shape[0]//2, black.shape[1]//2), (0,0,255),thickness=cv.FILLED)

#3. Draw a circle
cv.circle(black, (black.shape[0]//2, black.shape[1]//2), 40,(0,255,0), thickness = -1)

#4. Draw line
cv.line(black, (0,0), (black.shape[0]//2, black.shape[1]//2), (255,255,255),thickness=2)

#5. Draw text
# cv.putText(black, "Hello")
cv.putText(black, "Hello",(255,255),cv.FONT_HERSHEY_PLAIN,1.0,(255,255,255),thickness=2)
# #Color is by default black
cv.imshow('Rectangle', black)
cv.waitKey(0)