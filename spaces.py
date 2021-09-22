import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Resources/Photos/park.jpg')
cv.imshow("Park", img)

#BGR to Gray
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# #BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# #BGR to L*a*b
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('Lab',lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()

cv.waitKey(0)