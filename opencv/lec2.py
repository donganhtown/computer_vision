import cv2 as cv

img = cv.imread('pic/bot1.jpg')
# cv.imshow('bot',img)
def kichthuoc(frame, scale=0.5):
    # ảnh,video,live
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale) 
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def phangiai(width,height):
    #live
    capture.set(3,width)
    capture.set(4,height)
change_imga=kichthuoc(img)
cv.imshow('bot',change_imga)
capture = cv.VideoCapture('vio/video2.mp4')
while True:
    isTrue, frame = capture.read()
    
    if not isTrue:
        break
    
    frame_quay90 = cv.rotate(frame,cv.ROTATE_90_COUNTERCLOCKWISE)
    frame_change = kichthuoc(frame_quay90)
    cv.imshow('Video', frame)        
    cv.imshow('videom', frame_change)    
    
    if cv.waitKey(20) & 0xFF == ord('v'):
        break

capture.release()
cv.destroyAllWindows()
