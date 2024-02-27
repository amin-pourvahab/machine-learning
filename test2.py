# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:48:23 2024

@author: Poorvahab
"""



import cv2
import numpy as np
#define a video capture object
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
vid=cv2.VideoCapture(0,cv2.CAP_DSHOW)
vid.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)   

while vid.isOpened(): 
      
    # Capture the video frame 
    # by frame 
    ret, frame =vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.5,4)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(frame,  
    #             'TEXT ON VIDEO',  
    #             (50, 50),  
    #             font, 1,  
    #             (0, 255, 255),  
    #             2,  
    #             cv2.LINE_4)

    # Display the resulting frame 
    cv2.imshow('live recognition', frame)
    
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
































