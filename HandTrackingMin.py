import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

#Creating an object for the class "Hands"
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode = False, max_num_hands = 2, model_complexity = 1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #To check if something was detected or not
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # To get the landmark information from each hand
            # each landmark has an id and its correspondent x and y positions
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                
                """ #To highligh a specific finger, change the "id" number according to the hand landmarks figure (https://mediapipe.dev/images/mobile/hand_landmarks.png)
                if id == 4: # 4 == thumb tip
                    cv2.circle(img, (cx,cy), 15, (255,0,0), cv2.FILLED)
                if id == 8: # 8 == Index finger tip
                    cv2.circle(img, (cx,cy), 15, (255,0,0), cv2.FILLED) """
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,255), 3) 

    cv2.imshow("Image", img)
    cv2.waitKey(1)