import cv2
import numpy as np

image = cv2.imread('circulos.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1.3, .9)


if circles is not None:

   circles = np.round(circles[0, :]).astype("int")

   for (x, y, r) in circles:
      cv2.circle(image, (x, y), r, (0, 0, 255), 7, cv2.LINE_AA)

cv2.imshow("circle",image)
cv2.waitKey(0)
