import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Image
img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

#The reverse conversions is also possible but not directly

#BGR to GreyScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR TO LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#OpenCV uses BGR but others use RGB(like matplot)
plt.imshow(img)
plt.show()

plt.imshow(rgb)
plt.show()

cv.waitKey(0)