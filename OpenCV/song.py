import cv2,vlc
import time
v=cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(r'C:\Program Files\Python37\Lib\site-packages\cv2\data\haarcascade_eye.xml')
m=vlc.MediaPlayer(r'C:\Users\KIIT\Desktop\1.mp3')
time.sleep(3)
m.play()
flag=1
while True:
    r,i=v.read()
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(gray,1.1,5)
    for x,y,w,h in f:
        #print(x,y)
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,255,0),2)
    print(len(f))
    if(len(f)>0):
        m.play()
        flag=0
    elif(flag==0):
        m.pause()
        flag=1
    cv2.imshow('f',i)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        m.stop()
        break
cv2.destroyAllWindows()
v.release
        
    
        
