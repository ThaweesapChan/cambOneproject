import pyautogui
import time

def screenShotLR():
    start_time = time.perf_counter()

    # Get the size of the screen
    screen_width, screen_height = pyautogui.size()

    # Take a screenshot of the left side of the screen and save it to a file
    pyautogui.screenshot("/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageLeft.png", region=(0, 0.23*screen_height, screen_width / 2, screen_height))

    # Take a screenshot of the right side of the screen and save it to a file
    pyautogui.screenshot("/Users/thaweesap/CodingProject/cambOneProject/img/screenShot/pageRight.png", region=(screen_width / 2, 0.23*screen_height, screen_width / 2, screen_height))

    end_time = time.perf_counter()
    print("\nscreenShotLR \nTime taken: ", end_time - start_time)


screenShotLR()