# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:16:15 2019

@author: Anas
"""
import cv2

phone_cascade = cv2.CascadeClassifier('haarcascade_phone.xml')

def detect(gray, frame):
    phones = phone_cascade.detectMultiScale(gray,1.49, 10)
    for (x, y, w, h) in phones:
        print(x,y,w,h)
        if not (w < 100 or h < 100):
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.rectangle(frame, (x+int(w/2),y+int(h/2)), (x+int(w/2)+10,y+int(h/2)+10),(0,0,255),2) #center
        
    return frame

frame = cv2.imread('remote-phone34.png')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
canvas = detect(gray, frame)

cv2.imshow('image',canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()