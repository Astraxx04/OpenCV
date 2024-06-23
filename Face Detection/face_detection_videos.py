import cv2 as cv

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    haar_cascade = cv.CascadeClassifier('Face Detection/haar_face.xml')

    faces_react = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    print("Numbers of faces found: ", len(faces_react))

    for (x,y,w,h) in faces_react:
        print(x, y, w, h)
        cv.rectangle(frame, (x,y) ,(x+w,y+h), (0, 255, 0), thickness=2)

    cv.imshow('Faces Detected', frame)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyallWindows()