import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
# img = np.zeros((300,512,3), np.uint8)
img1 = cv2.imread('apple.jpg')
imgzero = np.zeros(img1.shape, np.uint8)
img = np.zeros(img1.shape, np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)
# bi = np.array(img[:,:,0])+10
# cv2.imshow('b',bi)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')+np.array(img1[:,:,2])
    g = cv2.getTrackbarPos('G','image')+np.array(img1[:,:,1])
    b = cv2.getTrackbarPos('B','image')+np.array(img1[:,:,0])
    s = cv2.getTrackbarPos(switch,'image')
    if s == 0:
        img = imgzero
    else:
        img[:,:,0] = b
        img[:,:,1] = g
        img[:,:,2] = r
# print r
cv2.destroyAllWindows()
