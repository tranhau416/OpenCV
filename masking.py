import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/Cats.jpg')
# cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
print((blank.shape[1]//2),(blank.shape[0]//2))

rectangle = cv.rectangle(blank.copy(), (int(blank.shape[1]//2-50),int(blank.shape[0]//2-50)),(int(blank.shape[1]//2+50),int(blank.shape[0]//2+50)),255, -1)
cv.imshow('Rectangle', rectangle)

mask = cv.bitwise_and(img, img, mask=rectangle)
cv.imshow('Mask', mask)

cv.waitKey(0)