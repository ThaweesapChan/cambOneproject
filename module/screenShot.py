import pyautogui
import time
import cv2
import numpy as np

def screenShotLR():
    start_time = time.perf_counter()

    # Get the size of the screen
    screen_width, screen_height = pyautogui.size()

    # Take a screenshot of the left side of the screen and save it to a file
    pyautogui.screenshot("/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageLeft.png", region=(0, 0, screen_width / 2, screen_height))

    # Take a screenshot of the right side of the screen and save it to a file
    pyautogui.screenshot("/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageRight.png", region=(screen_width / 2, 0, screen_width / 2, screen_height))

    end_time = time.perf_counter()
    print("\nscreenShotLR \nTime taken: ", end_time - start_time)


def clickObject(object_img, img):
    start_time = time.perf_counter()

    # Get the size of the screen
    screen_width, screen_height = pyautogui.size()

    # Load the object image and the screenshot image

    object_image = cv2.imread(object_img)
    screenshot = cv2.imread(img)

    # Use cv2.matchTemplate to search for the object in the screenshot
    result = cv2.matchTemplate(screenshot, object_image, cv2.TM_CCOEFF_NORMED)

    # Use cv2.minMaxLoc to find the coordinates of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # If the best match is above a certain threshold, click on the center of the object
    end_time = time.perf_counter()
    print("\nclickObject \nTime taken: ", end_time - start_time)

    if max_val > 0.8:
        # Calculate the coordinates of the center of the object
        object_height, object_width = object_image.shape[:2]
        x, y = max_loc

        if img == "/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageRight.png":
            center_x = x + (screen_width/2) + object_width /2
            center_y = y + object_height / 2

        else:
            center_x = x + object_width / 2
            center_y = y + object_height / 2

        # Click on the center of the object
        pyautogui.click(center_x, center_y)

        # เวลาที่ fuctions ใช้

        print('Object found and clicked at', (center_x, center_y))
    else:
        print('Object not found')

def countObject(object_img, img):
    start_time = time.perf_counter()
    # Load the object and search images
    object_img = cv2.imread(object_img)
    search_img = cv2.imread(img)

    # Convert the images to grayscale
    object_gray = cv2.cvtColor(object_img, cv2.COLOR_BGR2GRAY)
    search_gray = cv2.cvtColor(search_img, cv2.COLOR_BGR2GRAY)

    # Use the matchTemplate function to find the object in the search image
    result = cv2.matchTemplate(search_gray, object_gray, cv2.TM_CCOEFF_NORMED)

    # Use the threshold function to filter out weak matches
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Count the number of matches found
    object_count = len(loc[0])

    end_time = time.perf_counter()
    print("\ncountObject\nTime taken: ", end_time - start_time)

    print(object_count)
    return object_count

screenShotLR()
countObject("/Users/thaweesap/CodingProject/cambOneProject/img/template/th.png","/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageRight.png")