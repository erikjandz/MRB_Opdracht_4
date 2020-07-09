import cv2
import numpy as np

left_most_value = 380
centre_value = 195
right_most_values = 30


def return_position_ball():
    cap = cv2.VideoCapture(0)
    while True:
        temp = cap.read()[1]
        temp = temp[200:400, 130:550]
        gray = cv2.medianBlur(cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY), 5)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50,param2=30,minRadius=20,maxRadius=25)  # ret=[[Xpos,Ypos,Radius],...]
        if circles is not None:
            for circle in circles:
                cap.release()
                cv2.destroyAllWindows()
                print(circle[0][0])
                return circle[0][0]
        #cv2.imshow('video', gray)
        if cv2.waitKey(1) == 27:  # esc Key
            break

while True:
    return_position_ball()
