#-*- condinf: utf-8 -*-

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread("lena.png")
cv2.namedWindow("trackbar",cv2.WINDOW_NORMAL)

cv2.createTrackbar("H_l", "trackbar", 0, 180, nothing)
cv2.createTrackbar("H_h", "trackbar", 0, 180, nothing)
cv2.createTrackbar("S_l", "trackbar", 0, 255, nothing)
cv2.createTrackbar("S_h", "trackbar", 0, 255, nothing)
cv2.createTrackbar("V_l", "trackbar", 0, 255, nothing)
cv2.createTrackbar("V_h", "trackbar", 0, 255, nothing)


while(1):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_l = cv2.getTrackbarPos("H_l", "trackbar")
    h_h = cv2.getTrackbarPos("H_h", "trackbar")
    s_l = cv2.getTrackbarPos("S_l", "trackbar")
    s_h = cv2.getTrackbarPos("S_h", "trackbar")
    v_l = cv2.getTrackbarPos("V_l", "trackbar")
    v_h = cv2.getTrackbarPos("V_h", "trackbar")
    
    lower = np.array([h_l, s_l, v_l])
    upper = np.array([h_h, s_h, v_h])
    img_mask_blue = cv2.inRange(hsv, lower, upper)
    img_color_blue = cv2.bitwise_and(img, img, mask=img_mask_blue)

    cv2.imshow("origin", img)
    cv2.imshow("mask_image", img_color_blue)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break
                
cv2.destroyAllWindows()
