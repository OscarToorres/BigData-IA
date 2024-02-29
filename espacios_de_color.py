import cv2 as cv
import numpy as np
image = cv.imread('test.png')
print(image.shape)
cv.imshow('img',image)
cv.waitKey(0)