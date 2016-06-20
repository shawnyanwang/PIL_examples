import sys

import numpy as np
import cv2

im = cv2.imread('pitrain.png')
im3 = im.copy()

gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)
# cv2.waitKey(0)
blur = cv2.GaussianBlur(gray,(5,5),0)
# cv2.imshow('blur',blur)
# cv2.waitKey(0)
thresh = cv2.adaptiveThreshold(blur,255,1,1,11,3)
# cv2.imshow('thresh',thresh)
# cv2.waitKey(0)
#################      Now finding Contours         ###################

_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
#
# cv2.drawContours(im, contours, -1, (0,255,0), 3)
# cv2.imshow('thresh',im)
# cv2.waitKey(0)

# print contours[0]

samples =  np.empty((0,100))
responses = []
keys = [i for i in range(48,58)]
# print keys
for cnt in contours:
    if cv2.contourArea(cnt)>50:
        [x,y,w,h] = cv2.boundingRect(cnt)

        if  h>28:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            print roi
            cv2.imshow('norm',im)
            key = cv2.waitKey(0)

            if key == 27:  # (escape to quit ctrl+ [)
                sys.exit()
            elif key in keys:
                responses.append(int(chr(key)))
                sample = roismall.reshape((1,100))
                samples = np.append(samples,sample,0)


responses = np.array(responses,np.float32)
responses = responses.reshape((responses.size,1))
print "training complete"
#
#
# print samples
# print responses
np.savetxt('generalsamples.data',samples)
np.savetxt('generalresponses.data',responses)
