import cv2 as cv
import numpy as np

#Image
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow('Mask', mask)

wierd_shape = cv.bitwise_and(rectangle, circle)
cv.imshow('Wierd Shape', wierd_shape)

masked = cv.bitwise_and(img, img, mask=wierd_shape)
cv.imshow('Masked', masked)

cv.waitKey(0)