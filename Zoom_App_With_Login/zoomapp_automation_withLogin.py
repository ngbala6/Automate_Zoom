## @Author : Bala Murugan N G
import time
import pyautogui
import os
from configparser import ConfigParser
import schedule

configurations = ConfigParser()

configurations.read("config.conf")

print(configurations.get('Time', 'Start_Time'))

class ZoomApp_Automation:

    def __init__(self):
        # job =
        print(configurations.get("Time", "Start_Time"))

        schedule.every().day.at(configurations.get("Time", "Start_Time")).do(self.signIn, configurations.get('Authentication', 'MeetingID'), configurations.get('Authentication', 'Passcode'))
        # schedule.every().day.at(configurations.get("Time", "Start_Time")).do(self.ss, "super")

        while True:
            schedule.run_pending()
            # time.sleep(5)

    def signIn(self, meeting_id, password):
        # Open's Zoom Application from the specified location
        os.startfile(configurations.get('Application', 'Application_Path'))
        time.sleep(5)

        # Click's join button
        joinbtn = pyautogui.locateCenterOnScreen("screens/joinbutton.png")
        pyautogui.moveTo(joinbtn)
        pyautogui.click()
        time.sleep(3)

        # Type the meeting id
        meetingidbtn = pyautogui.locateCenterOnScreen("screens/meetinglink.png")
        pyautogui.moveTo(meetingidbtn)
        pyautogui.write(meeting_id)
        time.sleep(2)

        ## @Author : Bala Murugan N G

        # Mute Audio
        mediaBtn = pyautogui.locateCenterOnScreen("screens/audio.png")
        pyautogui.moveTo(mediaBtn)
        pyautogui.click()
        time.sleep(1)

        # # Type the Name
        # meetingnamebtn = pyautogui.locateCenterOnScreen("screens/names.png")
        # pyautogui.moveTo(meetingnamebtn)
        # pyautogui.write(configurations.get('Authentication', 'Name'))
        # time.sleep(2)

        # Turn off Video
        videoBtn = pyautogui.locateCenterOnScreen("screens/video.png")
        pyautogui.moveTo(videoBtn)
        pyautogui.click()
        time.sleep(1)

        # To join
        join = pyautogui.locateCenterOnScreen("screens/join.png")
        pyautogui.moveTo(join)
        pyautogui.click()
        time.sleep(10)

        # Meeting Password
        passcode = pyautogui.locateCenterOnScreen("screens/meetingpasscode.png")
        pyautogui.moveTo(passcode)
        pyautogui.write(password)
        time.sleep(1)
        ## @Author : Bala Murugan N G

        # Click's on join button
        joinmeeting = pyautogui.locateCenterOnScreen("screens/joinmeeting_final.png")
        pyautogui.moveTo(joinmeeting)
        pyautogui.click()
        time.sleep(1)


insclass = ZoomApp_Automation()

# @Author : Bala Murugan N G
