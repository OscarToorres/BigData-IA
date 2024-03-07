import numpy as np
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pylab
#Obtener las imagenes
pylab.rcParams["figure.figsize"] = (8,5.0)

piedra = cv.imread("piedra.jpg")
piedra_hsv = cv.cvtColor(piedra,cv.COLOR_BGR2HSV)
cv.namedWindow("piedra_hsv")
cv.imshow('piedra_hsv',piedra_hsv)
cv.waitKey(0)
print(piedra_hsv.shape)

papel = cv.imread("papel.jpg")
tigera = cv.imread("tigera.jpg")
