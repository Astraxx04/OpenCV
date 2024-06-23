import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'/Users/gagans/Documents/OpenCV/Face Recognition/train'
haar_cascade = cv.CascadeClassifier('Face Recognition/haar_face.xml')

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

            faces_react = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_react:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

print("Length of features list:", len(features))
print("Length of labels list:", len(labels))
print("Training Done!!!------------------------")

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and the labels list

face_recognizer.train(features, labels)

face_recognizer.save('Face Recognition/face_trained.yml')
np.save('Face Recognition/features.npy', features)
np.save('Face Recognition/labels.npy', labels)