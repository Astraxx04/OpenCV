import cv2 as cv
import numpy as np

#Image
img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Laplatian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)
sobel_comb = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel', sobel_comb)

#Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny',canny)

cv.waitKey(0)