import cv2
import numpy as np


def return_position_ball():
    cap = cv2.VideoCapture(0)
    while True:
        gray = cv2.medianBlur(cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY), 5)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10)  # ret=[[Xpos,Ypos,Radius],...]
        if circles is not None:
            print("circle")
            for circle in circles:
                #print(circle)
                print(circle[0][0], circle[0][1])
        cv2.imshow('video', gray)
        if cv2.waitKey(1) == 27:  # esc Key
            break
    cap.release()
    cv2.destroyAllWindows()

return_position_ball()