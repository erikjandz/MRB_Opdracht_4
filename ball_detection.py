import cv2
import time

left_most_value = 510
centre_value = 330
right_most_values = 160


def return_position_ball(cap):
    temptime = time.time()
    amount_of_iteration = 0
    while True:
        amount_of_iteration += 1
        temp = cap.read()[1]
        # temp = temp[200:350, 130:550]
        # if amount_of_iteration == 1:
        #     print("time to capture and crop is: " + str(time.time() - temptime))
        # print(type(temp[0][0]))
        gray = cv2.medianBlur(cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY), 5)
        # print(type(gray[0][0]))
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50,param2=30,minRadius=20,maxRadius=25)  # ret=[[Xpos,Ypos,Radius],...]
        if circles is not None:
            for circle in circles:
                print(circle[0][0])
                # print(circle[0][1])
                # print(circle[0][2])
                #print("amount of loops: " + str(amount_of_iteration))
                return circle[0][0]
        #cv2.imshow('video', gray)
        if cv2.waitKey(1) == 27:  # esc Key
            break


# return the average position of all pixels that are white
def return_position_ball2(cap):
    temptime = time.time()
    total = 0
    count = 0
    temp = cap.read()[1]
    temp = temp[200:350, 130:550]
    print("time to capture and crop is: " + str(time.time() - temptime))
    temptime = time.time()
    gray = cv2.medianBlur(cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY), 5)
    print("time to medianblur is: " + str(time.time() - temptime))
    temptime = time.time()
    for i in range(len(gray)):
        for j in range(len(gray[i])):
            if gray[i][j] > 220:
                total += j
                count += 1
    print("time to get average of white pixels is: " + str(time.time() - temptime))
    #cv2.imshow('video', gray)
    if count == 0:
        return 195
    result = total / count
    print(result)
    return result


# while True:
#     return_position_ball()
