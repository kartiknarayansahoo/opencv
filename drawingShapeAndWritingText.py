import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# paint the image a certain color
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# painting certain regions with certain colors
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('mixedColor', blank)

# drawing a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (140, 210, 135), thickness=2)
cv.imshow('Rectangle', blank)

cv.waitKey(0)
