import cv2 as cv

def rescaleFrame(frame, scale=0.75): # Images, Videos and Live Videos
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height): #Live Videos
    capture.set(3, width)
    capture.set(4, height)

#Image
img = cv.imread('Photos/cat.jpg')
img_resized = rescaleFrame(img)
cv.imshow('Cat', img)
cv.imshow('Cat Resized', img_resized)

#Video
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()