import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('Face Detection/haar_face.xml')

faces_react = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print("Numbers of faces found: ", len(faces_react))

for (x,y,w,h) in faces_react:
    cv.rectangle(img, (x,y) ,(x+w,y+h), (0, 255, 0), thickness=2)

cv.imshow('Faces Detected', img)

cv.waitKey(0)