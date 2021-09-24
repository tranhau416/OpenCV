import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/lady.jpg')
# cv.imshow('People', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


haar_cascade = cv.CascadeClassifier('data/haar_face.xml')
 

face_rect = haar_cascade.detectMultiScale(gray,  scaleFactor= 1.1, minNeighbors = 5)
print('Number of face(s) found: ',len(face_rect))

for(x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0,255,0), thickness=2)
cv.imshow('Detected Face(s)', img)

cv.waitKey(0)