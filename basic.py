import cv2 as cv

#Image
img = cv.imread('Photos/park.jpg')
cv.imshow('Cat', img)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


#Blurring
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny',canny)

#Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding the image
erode = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroding', erode)

#Resize
resize = cv.resize(img, (500, 500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resize', resize)

#Croping
crop = img[50:200, 200:400]
cv.imshow('Crop', crop)


cv.waitKey(0)