
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.namedWindow('cannyTrack')

def nothing(x):
    pass
cv2.createTrackbar('cannyTrack1', 'cannyTrack', 0, 255, nothing)
cv2.createTrackbar('cannyTrack2', 'cannyTrack', 0, 255, nothing)
switch  = "0 :OFF\n 1 :ON"
cv2.createTrackbar(switch, 'cannyTrack', 0, 1, nothing)


while(1):
    cv2.imshow('img', img)
    k = cv2.waitKey(1)
    if k == 27:
        break
    c1 = cv2.getTrackbarPos('cannyTrack1', 'cannyTrack')
    c2 = cv2.getTrackbarPos('cannyTrack2', 'cannyTrack')
    s = cv2.getTrackbarPos(switch, 'cannyTrack')
    if s==0:
        canny = cv2.Canny(img, 100, 200)
        cv2.imshow('cannyTrack', canny)
    else:
        canny = cv2.Canny(img, c1, c2)
        cv2.imshow('cannyTrack', canny)
        
cv2.destroyAllWindows()


