import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# # Paint the image a certain color
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# blank[:] = 0, 0, 255
# cv.imshow('Red', blank)

# blank[200:300, 300:400] = 255, 0, 0
# cv.imshow('Blue', blank)

# Draw a Line
# cv.line(blank,(0, 0), (blank.shape[1]//2, 250), (255, 255, 255), thickness=2)
# cv.imshow('Circle', blank)

# Draw a Reactangle
# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, 250), (0, 255, 0), thickness=-1) # or use cv.FILLED
# cv.imshow('Reactangle', blank)

# Draw a Circle
# cv.circle(blank, (blank.shape[1]//2, 250), 40, (0, 255, 0), thickness=-1)
# cv.imshow('Circle', blank)

# Write Text
cv.putText(blank, 'Hello World', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)