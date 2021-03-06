import cv2 as cv
import numpy as np

img_path = r'../images/blob.png'

img = cv.imread(img_path, cv.IMREAD_COLOR)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_red = np.array([0, 235, 235]) 
upper_red = np.array([0, 255, 255])
 
lower_purple = np.array([130, 153, 178])
upper_purple= np.array([140, 210, 229])


lower_green = np.array([38, 204, 250])
upper_green = np.array([44, 210, 255])

mask_red = cv.inRange(hsv, lower_red, upper_red)
mask_purple = cv.inRange(hsv, lower_purple, upper_purple)
mask_green = cv.inRange(hsv, lower_green, upper_green)

cv.imshow("test", img)

cv.imshow("red mask", mask_red)
cv.imshow("purple mask", mask_purple)
cv.imshow("green mask", mask_green)

cv.imshow("hsv image", hsv)
cv.waitKey(0)

cv.destroyAllWindows()
