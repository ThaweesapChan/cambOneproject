import pyautogui
import time
import cv2
import numpy as np
from time import sleep as sleep

def readTemplate():
    start_time = time.perf_counter()
    global buttonCheck, buttonNext, buttonNextAct, pageLineMagentaDark, pageLineMagentaLight, pageLineMagentaNon

    # อ่านรูปภาพ template ทั้งหมด
    buttonCheck             = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonCheck.png")
    buttonNext              = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonNext.png")
    buttonNextAct           = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonNextAct.png")
    pageLineMagentaDark     = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaDark.png")
    pageLineMagentaLight    = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaLight.png")
    pageLineMagentaNon      = cv2.imread("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaNon.png")

    end_time = time.perf_counter()
    print("\nreadTemplate \nTime taken: ", end_time - start_time)

def screenShotLR():

    start_time = time.perf_counter()
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

    end_time = time.perf_counter()
    print("\nscreenShotLR \nTime taken: ", end_time - start_time)

def clickObject(object_img, img, strSide):
    start_time = time.perf_counter()

    # Get the size of the screen
    screen_width, screen_height = pyautogui.size()

    # Use cv2.matchTemplate to search for the object in the screenshot
    result = cv2.matchTemplate(img, object_img, cv2.TM_CCOEFF_NORMED)

    # Use cv2.minMaxLoc to find the coordinates of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # If the best match is above a certain threshold, click on the center of the object
    end_time = time.perf_counter()
    print("\nclickObject \nTime taken: ", end_time - start_time)

    if max_val > 0.8:
        # Calculate the coordinates of the center of the object
        object_height, object_width = object_img.shape[:2]
        x, y = max_loc

        if strSide == "pageRight":
            center_x = x + (screen_width/2) + object_width /2
            center_y = y + object_height / 2
            print("if")

        else:
            center_x = x + object_width / 2
            center_y = y + object_height / 2
            print("else")

        # Click on the center of the object
        pyautogui.doubleClick(center_x, center_y)

        # เวลาที่ fuctions ใช้

        print('Object found and clicked at', (center_x, center_y))
    else:
        print('Object not found')

def countObject(object_img, img):
    # Load the object image and the screenshot image
    screenshot = cv2.imread(img)

    # Use cv2.matchTemplate to search for the object in the screenshot
    result = cv2.matchTemplate(screenshot, object_img, cv2.TM_CCOEFF_NORMED)

    # Use cv2.threshold to set a threshold for a good match
    threshold = 0.99
    loc = np.where(result >= threshold)

    # Count the number of occurrences of the object
    count = 0
    for pt in zip(*loc[::-1]):
        count += 1
    print(count)
    return count

def pagePresentation():
    start_time = time.perf_counter()
    screenShotLR()
    leftPLM_non     = countObject("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaNon.png",
                                  "/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageLeft.png")
    leftPLM_Light   = countObject("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaLight.png",
                                  "/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageLeft.png")
    leftPLM_Dark    = countObject("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaDark.png",
                                  "/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageLeft.png")

    rightPLM_non    = countObject("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaNon.png",
                                  "/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageRight.png")
    rightPLM_Light   = countObject("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaLight.png",
                                  "/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageRight.png")
    rightPLM_Dark    = countObject("/Users/thaweesap/CodingProject/cambOneProject/img/template/pageLineMagentaDark.png",
                                  "/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageRight.png")

    sumLeft  = leftPLM_non + leftPLM_Light + leftPLM_Dark
    sumRight = rightPLM_non + rightPLM_Light + rightPLM_Dark

    if sumLeft == sumRight :
        clickObject("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonNext.png",
                    "/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageLeft.png")
        sleep(0.2)
        clickObject("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonNext.png",
                    "/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageRight.png")
        sleep(0.2)
        clickObject("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonNextAct.png",
                    "/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageLeft.png")
        sleep(0.2)
        clickObject("/Users/thaweesap/CodingProject/cambOneProject/img/template/buttonNextAct.png",
                    "/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageRight.png")

    end_time = time.perf_counter()
    print("\nclickObject \nTime taken: ", end_time - start_time)

readTemplate()
screenShotLR()
clickObject(buttonNext,pageRight,"pageRight")