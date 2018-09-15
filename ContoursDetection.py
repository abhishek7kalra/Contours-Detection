# -*- coding: utf-8 -*-
"""
Created on Thu Aug 09 19:16:44 2018

@author: Abhishek
"""
import cv2
cap = cv2.VideoCapture(0)
while(True):
    if cap.grab():
        flag, img = cap.retrieve()
    #ret, img = cv2.imread('circle.jpg')
    #clone = copy.copy(frame)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_image,127,255,1)
    

    #contours,h = cv2.findContours(thresh,1,2)

    _, contours, h = cv2.findContours(thresh,1,2)

    for cnt in contours:
            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            print len(approx)
            if len(approx)>=12:
                cv2.drawContours(img,[cnt],0,(0,255,0, 1),2)

    # Display the resulting frame
    cv2.imshow('frame', img)
    cv2.imshow('thresh', thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
