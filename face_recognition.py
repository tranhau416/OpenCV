import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier('data/haar_face.xml')

people=['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
features = np.load('features.npy',allow_pickle=True)
labels = np.load('labels.npy',allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'E:\Opencv\learn\Resources\Faces\val\ben_afflek\2.jpg')
# cv.imshow('Image', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


#Detect the face in image

face_rest = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)
for (x, y, w, h) in face_rest:
    face_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(face_roi)
    cv.putText(img, str(people[label]), (x-10, y-10), cv.FONT_HERSHEY_COMPLEX,.5, (0,255,0), thickness=2)
    cv.rectangle (img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
cv.imshow('Detected Face', img)


cv.waitKey(0)