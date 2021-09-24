import cv2 as cv
import numpy as np
import os

DIR = "E:/Opencv/learn/Resources/Faces/train"

people =[]
for person in os.listdir(DIR):
    people.append(person)
# print(people)
# people=['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']


haar_cascade = cv.CascadeClassifier('data/haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            face_rest = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

            for (x, y, w, h) in face_rest:
                face_roi = gray[y:y+h,x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()
# print('Length of feaures: ', len(features))
# print('Length of labels: ',len(labels))
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)