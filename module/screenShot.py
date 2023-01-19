import pyautogui
import time
import cv2
import numpy as np
from time import sleep as sleep

def readTemplate():
    start_time = time.perf_counter()
    global buttonCheck,buttonCorrectChoice,buttonCycle, buttonNext, buttonNextAct,buttonNextActMagenta,buttonTriangle,\
        iconCorrect,pageLineGreenDark,pageLineGreenNon, pageLineMagentaDark, pageLineMagentaLight, pageLineMagentaNon

    # อ่านรูปภาพ template ทั้งหมด
    buttonCheck             = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonCheck.png")
    buttonCorrectChoice     = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonCorrectChoice.png")
    buttonCycle             = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/ButtonCycle.png")
    buttonNext              = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonNext.png")
    buttonNextAct           = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonNextAct.png")
    buttonNextActMagenta    = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonNextActMagenta.png")
    buttonTriangle          = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonTriangle.png")
    iconCorrect             = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/iconCorrect.png")
    pageLineGreenDark       = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineGreenDark.png")
    pageLineGreenNon        = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineGreenNon.png")
    pageLineMagentaDark     = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaDark.png")
    pageLineMagentaLight    = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaLight.png")
    pageLineMagentaNon      = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaNon.png")

    end_time = time.perf_counter()
    print("\nreadTemplate \nTime taken: ", end_time - start_time)

def screenShotLR():

    global pageLeft,pageRight

    # Get the size of the screen
    screen_width, screen_height = pyautogui.size()

    # Take a screenshot of the left side of the screen and save it to a file
    pyautogui.screenshot("/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageLeft.png", region=(0, 0, screen_width / 2, screen_height))

    # Take a screenshot of the right side of the screen and save it to a file
    pyautogui.screenshot("/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageRight.png", region=(screen_width / 2, 0, screen_width / 2, screen_height))

    # อ่านภาพ screenShot ทั้งซ้ายขวา และประการเป็นตัวแปร global
    pageLeft    = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageLeft.png")
    pageRight   = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageRight.png")

def clickObject(object_img, img, strSide):
    start_time = time.perf_counter()

    # Get the size of the screen
    screen_width, screen_height = pyautogui.size()

    # Use cv2.matchTemplate to search for the object in the screenshot
    result = cv2.matchTemplate(img, object_img, cv2.TM_CCOEFF_NORMED)

    # Use cv2.minMaxLoc to find the coordinates of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # If the best match is above a certain threshold, click on the center of the object

    if max_val > 0.8:
        # Calculate the coordinates of the center of the object
        object_height, object_width = object_img.shape[:2]
        x, y = max_loc

        if strSide == "R":
            center_x = x + (screen_width/2) + object_width /2
            center_y = y + object_height / 2

        else:
            center_x = x + object_width / 2
            center_y = y + object_height / 2

        # Click on the center of the object
        pyautogui.click(center_x, center_y)

        # เวลาที่ fuctions ใช้
        end_time = time.perf_counter()

        print('clickObject',"Time taken:", end_time - start_time)
def clickDoubleObject(object_img, img, strSide):
    start_time = time.perf_counter()

    # Get the size of the screen
    screen_width, screen_height = pyautogui.size()

    # Use cv2.matchTemplate to search for the object in the screenshot
    result = cv2.matchTemplate(img, object_img, cv2.TM_CCOEFF_NORMED)

    # Use cv2.minMaxLoc to find the coordinates of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # If the best match is above a certain threshold, click on the center of the object

    if max_val > 0.8:
        # Calculate the coordinates of the center of the object
        object_height, object_width = object_img.shape[:2]
        x, y = max_loc

        if strSide == "R":
            center_x = x + (screen_width/2) + object_width /2
            center_y = y + object_height / 2

        else:
            center_x = x + object_width / 2
            center_y = y + object_height / 2

        # Click on the center of the object
        pyautogui.doubleClick(center_x, center_y)

        # เวลาที่ fuctions ใช้
        end_time = time.perf_counter()

        print('clickObject',"Time taken:", end_time - start_time)
def clickDoubleObject(object_img, img, strSide):
    start_time = time.perf_counter()

    # Get the size of the screen
    screen_width, screen_height = pyautogui.size()

    # Use cv2.matchTemplate to search for the object in the screenshot
    result = cv2.matchTemplate(img, object_img, cv2.TM_CCOEFF_NORMED)

    # Use cv2.minMaxLoc to find the coordinates of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # If the best match is above a certain threshold, click on the center of the object

    if max_val > 0.8:
        # Calculate the coordinates of the center of the object
        object_height, object_width = object_img.shape[:2]
        x, y = max_loc

        if strSide == "R":
            center_x = x + (screen_width / 2) + object_width / 2
            center_y = y + object_height / 2

        else:
            center_x = x + object_width / 2
            center_y = y + object_height / 2

        # Click on the center of the object
        pyautogui.click(center_x, center_y, click=3)

        # เวลาที่ fuctions ใช้
        end_time = time.perf_counter()

        print('clickObject', "Time taken:", end_time - start_time)

def countObject(object_img, img):

    # Use cv2.matchTemplate to search for the object in the screenshot
    result = cv2.matchTemplate(img, object_img, cv2.TM_CCOEFF_NORMED)

    # Use cv2.threshold to set a threshold for a good match
    threshold = 0.99
    loc = np.where(result >= threshold)

    # Count the number of occurrences of the object
    count = 0
    for pt in zip(*loc[::-1]):
        count += 1
    return count

def pagePresentation():
    start_time = time.perf_counter()
    print("\npagePresentation\nLoop...")
    while True:
        screenShotLR()
        clickObject(buttonNext, pageLeft, "L")
        clickObject(buttonNext, pageRight, "R")
        leftPLM_non     = countObject(pageLineMagentaNon,pageLeft)
        leftPLM_Light   = countObject(pageLineMagentaLight,pageLeft)
        leftPLM_Dark    = countObject(pageLineMagentaDark,pageLeft)

        rightPLM_non    = countObject(pageLineMagentaNon,pageRight)
        rightPLM_Light  = countObject(pageLineMagentaLight,pageRight)
        rightPLM_Dark   = countObject(pageLineMagentaDark,pageRight)

        sumLeft  = leftPLM_non + leftPLM_Light + leftPLM_Dark
        sumRight = rightPLM_non + rightPLM_Light + rightPLM_Dark

        if sumLeft != 0:
            clickDoubleObject(buttonNext, pageLeft, "L")
            clickDoubleObject(buttonNextAct, pageLeft, "L")

        if sumRight != 0 :
            clickDoubleObject(buttonNext,pageRight,"R")
            clickDoubleObject(buttonNextAct, pageRight, "R")

        if sumLeft + sumRight == 0:
            print(sumLeft , sumRight)
            break
    end_time = time.perf_counter()
    print("loopBreak\nTime taken: ", end_time - start_time)
    return True

def pageCyclechoice():
    start_time = time.perf_counter()
    while True :
        # screenShot หน้าจอ
        screenShotLR()
        clickObject(buttonCycle, pageLeft, "L")
        screenShotLR()
        clickObject(buttonCheck, pageLeft, "L")
        screenShotLR()

        #หากการตอบถูกต้องให้ตอบคำตอบเดิมกับภาพทางด้านขวาและออกจาก while loop
        if countObject(iconCorrect,pageLeft) > 0 :
            clickObject(buttonCorrectChoice, pageLeft, "R")
            screenShotLR()
            clickObject(buttonCheck, pageRight, "R")
            screenShotLR()
            clickObject(buttonNext, pageLeft, "L")
            clickObject(buttonNext, pageRight, "R")
            break
        else:
            break

    end_time = time.perf_counter()
    print("\nclickObject \nTime taken: ", end_time - start_time)

def pageTriangleChoice():
    pass

readTemplate()
screenShotLR()
while True:
    pagePresentation()
    pageCyclechoice()