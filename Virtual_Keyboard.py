import cv2
import mediapipe as mp
from pynput.keyboard import Controller
from time import sleep
import math
import numpy as np
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
from pynput.keyboard import Controller

def virtualKeyboard():
    camIndex=1
    cap=cv2.VideoCapture(camIndex)
    mpHands=mp.solutions.hands
    Hands=mpHands.Hands()
    mpDraw=mp.solutions.drawing_utils

    keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
            ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],[" "]]
    keyboard = Controller()

    class Store():
        def __init__(self,pos,size,text):
            self.pos=pos
            self.size=size
            self.text=text
        
    def draw(img,storedVar):
        for button in storedVar:
            x, y = button.pos
            w, h = button.size
            cv2.rectangle(img, button.pos, (x + w, y + h), (64, 64, 64), cv2.FILLED)
            cv2.putText(img, button.text, (x+10, y+43),cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)
        return img

    StoredVar = []
    for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            StoredVar.append(Store([60 * j + 10, 60 * i + 10], [50,50],key))



    while (cap.isOpened()):
        success_,img=cap.read()
        cvtImg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results=Hands.process(cvtImg)
        lmList=[]

        if results.multi_hand_landmarks:
            for img_in_frame in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, img_in_frame, mpHands.HAND_CONNECTIONS)
            for id,lm in enumerate(results.multi_hand_landmarks[0].landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
    
                lmList.append([cx,cy])

        if lmList:
            for button in StoredVar:
                x, y = button.pos
                w, h = button.size
    
                if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 0, 255), cv2.FILLED)
                    x1,y1=lmList[8][0],lmList[8][1]
                    x2,y2=lmList[12][0],lmList[12][1]
                    l=math.hypot(x2-x1-30,y2-y1-30)
                    print(l)
                    ## when clicked
        #             if l < 25:
        #                 keyboard.press(button.text)
        #                 cv2.rectangle(img, button.pos, (x + w, y + h),
        #                             (0, 255, 0), cv2.FILLED)
        #                 cv2.putText(img, button.text, (x + 20, y + 65),
        #                             cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
        #                 final_text += button.text
        #                 sleep(0.20)
        #             cv2.rectangle(img, (25,350), (700, 450),
        #             (255, 255, 255), cv2.FILLED)
        # cv2.putText(img, final_text, (60, 425),
        #             cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
                    if not l > 63:
                        keyboard.press(button.text)
                        cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 255, 0), cv2.FILLED)
                        sleep(0.15)


        img = draw(img, StoredVar)

        cv2.imshow("Keyboard",img)

        if cv2.waitKey(1)==ord('q'): #Q=113
            break
        if cv2.getWindowProperty("Keyboard", cv2.WND_PROP_VISIBLE) <1:
            break
    cap.release()
    cv2.destroyAllWindows()


    # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # cap.set(3, 1280)
    # cap.set(4, 720)

    # detector = HandDetector(detectionCon=0.8)
    # keyboard_keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    #                 ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    #                 ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

    # final_text = ""

    # keyboard = Controller()


    # def draw(img, buttonList):
    #     for button in buttonList:
    #         x, y = button.pos
    #         w, h = button.size
    #         cvzone.cornerRect(img, (button.pos[0], button.pos[1],
    #                                                 button.size[0],button.size[0]), 20 ,rt=0)
    #         cv2.rectangle(img, button.pos, (int(x + w), int(y + h)), (255, 144, 30), cv2.FILLED)
    #         cv2.putText(img, button.text, (x + 20, y + 65),
    #                     cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
    #     return img


    # def transparent_layout(img, buttonList):
    #     imgNew = np.zeros_like(img, np.uint8)
    #     for button in buttonList:
    #         x, y = button.pos
    #         cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1],
    #                                                 button.size[0],button.size[0]), 20 ,rt=0)
    #         cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
    #                                 (255, 144, 30), cv2.FILLED)
    #         cv2.putText(imgNew, button.text, (x + 20, y + 65),
    #                     cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)

    #     out = img.copy()
    #     alpaha = 0.5
    #     mask = imgNew.astype(bool)
    #     print(mask.shape)
    #     out[mask] = cv2.addWeighted(img, alpaha, imgNew, 1-alpaha, 0)[mask]
    #     return out


    # class Button():
    #     def __init__(self, pos, text, size=[85, 85]):
    #         self.pos = pos
    #         self.size = size
    #         self.text = text


    # buttonList = []
    # # mybutton = Button([100, 100], "Q")
    # for k in range(len(keyboard_keys)):
    #     for x, key in enumerate(keyboard_keys[k]):
    #         buttonList.append(Button([100 * x + 25, 100 * k + 50], key))


    # while True:
    #     success, img = cap.read()
    #     img = detector.findHands(img)
    #     lmList, bboxInfo = detector.findPosition(img)
    #     img = draw(img, buttonList)  # change the draw funtion to transparent_layout for transparent keys

    #     if lmList:
    #         for button in buttonList:
    #             x, y = button.pos
    #             w, h = button.size

    #             if x < lmList[8][0]<x+w and y < lmList[8][1] < y+h:
    #                 cv2.rectangle(img, button.pos, (x + w, y + h),
    #                             (0, 255, 255), cv2.FILLED)
    #                 cv2.putText(img, button.text, (x + 20, y + 65),
    #                             cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
    #                 l, _, _ = detector.findDistance(8,12, img, draw=False)
    #                 print(l)

    #                 if l < 25:
    #                     keyboard.press(button.text)
    #                     cv2.rectangle(img, button.pos, (x + w, y + h),
    #                                 (0, 255, 0), cv2.FILLED)
    #                     cv2.putText(img, button.text, (x + 20, y + 65),
    #                                 cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
    #                     final_text += button.text
    #                     sleep(0.20)

    #     cv2.rectangle(img, (25,350), (700, 450),
    #                 (255, 255, 255), cv2.FILLED)
    #     cv2.putText(img, final_text, (60, 425),
    #                 cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)

    #     # cv2.rectangle(img, (100,100), (200,200),
    #     #               (100, 255, 0), cv2.FILLED)
    #     # cv2.putText(img, 'Q', (120,180), cv2.FONT_HERSHEY_PLAIN, 5,
    #     #             (0, 0, 0), 5)

    #     # img = mybutton.draw(img)
    #     cv2.imshow("output", img)
    #     cv2.waitKey(1)
    #     if cv2.waitKey(1)==113: #Q=113
    #         break
    # cap.release()
    # cv2.destroyAllWindows()