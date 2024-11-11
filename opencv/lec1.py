import cv2 as cv

img = cv.imread('pic/bot.jpg')
cv.imshow('bot',img)
cv.waitKey(0)

capture = cv.VideoCapture('vio/video2.mp4')
while True:
    isTrue, fame = capture.read()
    cv.imshow('Video',fame)
    
    if cv.waitKey(20) & 0xFF==ord('v'):
        break
capture.release()
cv.destroyAllWindows()


