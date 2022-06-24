import time
import numpy as np
import cv2
from random import randint


fgbg = cv2.createBackgroundSubtractorMOG2(history=20,varThreshold=16,detectShadows=False)


cap = cv2.VideoCapture('http://62.47.230.187:8080/?action=stream')
t = 10

while True:
    _, image = cap.read()

    fgmask = fgbg.apply(image)

    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(contours)
    if len(contours) > 0:
        for (i,contour) in enumerate (contours):

            (x,y,w,h) = cv2.boundingRect(contour)

            contour_valid = (w >= t) and (h >= t)
            if contour_valid:
                cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0),2)


    cv2.imshow("mask", fgmask)
    cv2.imshow('Camera', image)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
