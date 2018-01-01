
"""
Created on Sun Dec 30 16:30:55 2017

@author: Neeraj Tiwari(SC16M031)

Code made for tracking

"""


import cv2
#inport cv

cap = cv2.VideoCapture('Megamind.avi')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.BackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    if ret == True:

       fgmask = fgbg.apply(frame)
       fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

       cv2.imshow('frame',fgmask)


       if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break


cap.release()
cv2.destroyAllWindows()