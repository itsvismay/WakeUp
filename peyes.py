import numpy as np 
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

eyes_open =0
time =0
cap = cv2.VideoCapture(0)
while(True):
    ret, img =cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)
    if(len(eyes)>1):
        time =0
        #EYES DETECTED
        #DO SOMETHING Here
        print("eyes")
    else:
        #EYES NOT DETECTED
        print("Not")
        
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()



