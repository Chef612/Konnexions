import cv2
import time
import numpy as np
#fd=cv2.CascadeClassifier(r'C:\Users\KIIT\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
fd= cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
v=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
while True:
    r,i=v.read()
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(gray,1.3,7)
    print(f)
    #f1=fd1.detectMultiScale(gray,1.1,7)
    #f2=fd2.detectMultiScale(gray,1.1,7)
    #f3=fd3.detectMultiScale(gray,1.1,7)
    #f4=fd4.detectMultiScale(gray,1.1,7)
    print(len(f))
    for x,y,w,h in f:
            cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0), 2)
    '''for x,y,w,h in f1:
            cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0), 2)
    for x,y,w,h in f2:
            cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0), 2)
    #for x,y,w,h in f3:
    #    cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0), 2)
    for x,y,w,h in f4:
            cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0), 2)'''
    cv2.imshow('face',i)
    #cv2.imshow("Image", frame)
    k=cv2.waitKey(1)
    if(k==ord('q')):
            break

cv2.destroyAllWindows()
v.release()
