import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/Cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], 'uint8')

#gray histogram
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixel')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# colour histogram
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# masked = cv.bitwise_and(img,img,mask=circle)
# cv.imshow('Mask', masked)

plt.figure('Colour Histogram')
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixel')
color = ('b','g','r')
for i, col in enumerate(color):
    hist = cv.calcHist([img], [i], circle, [256], [0,256])
    plt.plot(hist, color =col)
    plt.xlim([0,255])
plt.show()
cv.waitKey(0)