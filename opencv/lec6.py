import mediapipe as mp
import cv2 
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mp_draw = mp.solutions.drawing_utils

cTime = 0
pTime = 0 


while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img,str(fps),(10,78),cv2.CAP_PROP_FRAME_HEIGHT,3,(255,255,0),3)
    
    cv2.imshow("Image" , img)
    cv2.waitKey(1)
