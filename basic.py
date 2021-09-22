import cv2 as cv

# img = cv.imread('Resources/Photos/Cat.jpg')
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow("Image", img)

#Converting to grayscale
# gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

#Blur - Làm mờ
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

#Edge Cascade - Phát hiện cạnh
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

#Dilating in image - Sự giãn nở 
dilated = cv.dilate(canny,(7,7), iterations=1)
# cv.imshow('Dilated',dilated)

#Eroding - Xói mòn( giảm nhiễu)
eroded = cv.erode(dilated,(3,3), iterations=1)
# cv.imshow("Eroded", eroded)

#Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

#Cropping
cropped = img[0:200,0:400, 2] # img[startY:endY, startX:endX]
cv.imshow('Cropped', cropped)

cv.waitKey(0)