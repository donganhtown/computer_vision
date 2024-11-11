import cv2 as cv
import numpy as np

blank = np.zeros((1000,1000,3),dtype='uint8')
# cv.imshow('blank',blank)

# #paint
# blank[:] = 0,0,225
# cv.imshow('color',blank)
#draw 
# cv.rectangle(blank,(0,0),(250,250),(0,225,0),thickness=2)
# cv.imshow('rectangle',blank)

# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,0),thickness=-1)
# cv.imshow('circle',blank)

# cv.line(blank,(100,250),(200,100),(225,225,225),thickness=3)
# cv.imshow('line',blank)

cv.putText(blank,'hello nìn cái gì',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,225,0),2)
cv.imshow('Text',blank)
# img = cv.imread('pic/bot2.jpg')
# cv.imshow('bot',img)

cv.waitKey(0)