import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Image
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

#Averaging
averaging = cv.blur(img, (7, 7))
cv.imshow('Average Blur',averaging)

#Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blur', gauss)

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

#Bilateral Blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Filter', bilateral)


cv.waitKey(0)