from selenium import webdriver
import time
import pyautogui
import os


def main():
    # os.startfile("chromedriver.exe")
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://us05web.zoom.us/j/86958015618?pwd=MnR0NWVBdVVRZDlsYitxcmIweGFSQT09")
    # driver.switch_to.alert.accept()
    time.sleep(3)

    # To click
    mediaBtn = pyautogui.locateCenterOnScreen("click.png")
    pyautogui.moveTo(mediaBtn)
    pyautogui.click()
    time.sleep(1)

    # To Join
    mediaBtnss = pyautogui.locateCenterOnScreen("openzoom.png")
    pyautogui.moveTo(mediaBtnss)
    pyautogui.click()
    time.sleep(1)


main()

