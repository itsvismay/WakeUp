import numpy as np 
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

eyes_open =0
count =0
cap = cv2.VideoCapture(0)
while(True):
    ret, img =cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        if(len(eyes)>1):
            if(count<11):
                count+=1
        else:
            if(count>0):
                count-=1
        if(count>5):
            print("open")
        else:
            print("closed")
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    cv2.imshow('gray',img)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()



