import cv2
import numpy as np

def motionD():
    cap=cv2.VideoCapture(0)
    _,f1=cap.read()
    _,f2=cap.read()
    while cap.isOpened():
        diff =cv2.absdiff(f1,f2)
        gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gray,(5,5),0)
        _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh,None,iterations=3)
        contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x,y,w,h)=cv2.boundingRect(contour)
            if cv2.contourArea(contour)<2000:
                continue
            cv2.rectangle(f1,(x,y),(x+w,y+h) ,(0,255,0),2)
            cv2.putText(f1,"Status:()".format('movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

        cv2.imshow("feed",f1)
        f1=f2
        _,f2=cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()
