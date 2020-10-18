import cv2
import numpy as np
i=cv2.imread(r'C:\Users\KIIT\Dropbox\Dropbox\My PC (SOUVIK)\Desktop\shapes.png')
j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
c,k=cv2.threshold(j,70,255,0)
#cv2.imshow('image',k)
cnts=cv2.findContours(k,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print('Total number of contours',len(cnts))
count=0
count1=0
count2=0
count3=0
font=cv2.FONT_HERSHEY_COMPLEX
for cnt in cnts:
    approx=cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(i, [approx], 0, (0), 5)
    if len(approx)== 3:
        count=count+1
        x=approx.ravel()[2]
        y=approx.ravel()[3]
        cv2.putText(k,'Triangle',(x,y),font,1,(183))
    if len(approx)== 12:
        count1=count1+1
        x=approx.ravel()[6]
        y=approx.ravel()[7]
        cv2.putText(k,' Oval',(x,y),font,1,(0))
    if len(approx)>= 16:
        count3=count3+1
        x=approx.ravel()[6]
        y=approx.ravel()[7]
        cv2.putText(k,' Circle',(x,y),font,1,(0))    
    if len(approx)== 4:
        count2=count2+1
        x=approx.ravel()[2]
        y=approx.ravel()[3]
        cv2.putText(k,'  Rectangle',(x,y),font,1,(0))
cv2.imshow('image',k)
print('Triangles',count)
print('Circles',count1)
print('Rectangles',count2)
print('Ovals',count3)
