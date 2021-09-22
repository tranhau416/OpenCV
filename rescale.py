import cv2 as cv
def re_scale(frame, scale = .75):
    #Image, Video and Live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    #Live video
    capture.set(3,width)
    capture.set(4,height)
#Reading videos

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF ==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
img = cv.imread('Resources/Photos/cat.jpg')

cv.imshow('Cat',img)
cv.imshow('Cat1', re_scale(img))
cv.waitKey(0)