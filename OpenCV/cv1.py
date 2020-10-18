import cv2
import numpy as np
i = cv2.imread(r'C:\Users\KIIT\Dropbox\Dropbox\My PC (SOUVIK)\Desktop\shapes.png')
#               image    conversion to grayscale
j = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
#cv2.imshow('i',j)#0 and 255
t,k = cv2.threshold(j,90,255,0)
#                    img    retrieval   approximation
cnts=cv2.findContours(k,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
count=0
X=[]
Y=[]
font=cv2.FONT_HERSHEY_COMPLEX
for cnt in cnts:
    m=cv2.moments(cnt)
    print(m['m00'])
    x=int((m['m10']/m['m00']))
    y=int((m['m01']/m['m00']))
    #          img  text   coord        color of text
    cv2.putText(i,'Centre',(x,y),font,1,(255,255,255))
    X.append(x)
    Y.append(y)
print(X,Y)
cv2.imshow('final',i)
    
    
