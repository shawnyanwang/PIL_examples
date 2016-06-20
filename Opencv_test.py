import cv2
import numpy as np

# img = cv2.imread('messi5.jpg')
# # print image size
# print img.size
# # print pixel value
# px = img[100,100]
# print px
# # accessing only blue pixel
# blue = img[100,100,0]
# print blue
# # modify the pixel values
# print img[100,100]
# img[100,100] = [255,255,255]
# print img[100,100]
# # modifying RED value
# img.itemset((10,10,2),100)
# print img.item(10,10,2)
# #ROI
#  ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball
# # Splitting and Merging Image Channels
# b,g,r = cv2.split(img)
# img = cv2.merge((b,g,r))

# img1 = cv2.imread('Luf.jpg')
# img2 = cv2.imread('Luf1.jpg')
# img3 = cv2.imread('Luf02.jpg')
# img4 = cv2.imread('Luf03.jpg')
# imgs = [img1,img2,img3,img4]
# import common
# print img1.shape
# res = common.mosaic(3, imgs)
#
# print len(res),len(res[0]),len(res[0][0])
# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)
# cv2.imshow('img3',img3)
# cv2.imshow('img4',img4)
# cv2.imshow('res',res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print ret
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
