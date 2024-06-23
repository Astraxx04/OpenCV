import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('Face Recognition/haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('Face Recognition/features.npy', allow_pickle=True)
# labels = np.load('Face Recognition/labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Face Recognition/face_trained.yml')

img = cv.imread('/Users/gagans/Documents/OpenCV/Face Recognition/val/elton_john/1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person', gray)

# Detect the face in the image

faces_rect = haar_cascade.detectMultiScale(img, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print("Label: ",people[label]," with confidence: ", confidence)

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Image', img)
cv.waitKey(0)