import cv2 as cv

img = cv.imread('pic/bot.jpg')
cv.imshow('image',img)

# gray = cv.cvtColor(img,cv.COLOR_BAYER_BG2BGRA)
# cv.imshow('gray',gray)

# blu = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow('blu',blu)

canny = cv.Canny(img,125,175)
cv.imshow('canny',canny)

dilated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilated',dilated)

eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('eroded',eroded)

resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resized)

cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)