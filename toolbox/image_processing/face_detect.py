""" Experiment with face detection and image filtering using OpenCV """

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/scott/SoftDesSp15/toolbox/image_processing/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21),'uint8')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    for (x,y,w,h) in faces:
        frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
        cv2.rectangle(frame,(x+w/8,y+h-h/3),(x+w-w/8,y+h-h/8),(0,0,0), thickness=5)
        cv2.line(frame, (x+w/5,y+h/8), (x+w/5,y+h/3), (0,0,0), thickness=5, lineType=8, shift=0)
        cv2.line(frame, (x+w-w/5,y+h/8), (x+w-w/5,y+h/3), (0,0,0), thickness=5, lineType=8, shift=0)
     # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
    
