import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret:
        print("Unable to read from camera. Existing.")
        exit()

    # img = cv2.imread('./src/image1.jpeg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sift = cv2.SIFT_create()
    # kp, des = sift.detectAndCompute(gray, None)
    kp = sift.detect(gray, None)

    img = cv2.drawKeypoints(gray, kp, img)
    cv2.imshow("sift_keypoints.jpg", img)
    cv2.waitKey(16)
