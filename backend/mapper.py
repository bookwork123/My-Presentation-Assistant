import threading
import pyautogui
import recognizer
import os, signal
from recognizer import recognizeGesture
from audio import audioUp, audioDown
import time



def mapper(volume):
    pyautogui.FAILSAFE = False
    t = threading.Thread(
        target=recognizeGesture,
        daemon=True
    )
    t.start()

    # Helps prevent duplicate actions
    last_gesture = None


    while True:
        user_gesture = recognizer.latest_gesture # grabbed from recognizer

        # disallows gesture spam
        if user_gesture == last_gesture:
            continue

        # updates previous gesture to current
        last_gesture = user_gesture

        # prevent extra processing effort
        if user_gesture is None:
            continue

        # reset latest_gesture for next grab
        recognizer.latest_gesture = None
        if user_gesture == "Victory":
            time.sleep(0.8)
            
            # allows user to hold Victory without unpausing - some different gesture must be used to break this loop
            while recognizer.latest_gesture == "Victory" or recognizer.latest_gesture is None:
                recognizer.latest_gesture = None
                time.sleep(0.05)
            
            # once a diff. gesture has been used, a new Victory will unpause the program
            while True:
                new_gesture = recognizer.latest_gesture
                if new_gesture == "Victory":
                    recognizer.latest_gesture = None
                    time.sleep(0.8)
                    break
                time.sleep(0.05)

        elif user_gesture == "Thumb_Up":
            pyautogui.press('right')
            print("RIGHT!")
            time.sleep(0.8)
        elif user_gesture == "Thumb_Down":
            pyautogui.press('left')
            print("LEFT!")
            time.sleep(0.8)
        elif user_gesture == "Open_Palm":
            pyautogui.press('space')
            print('SPACE!')
            time.sleep(0.8)
        elif user_gesture == "Pointing_Up":
            audioUp(volume)
            time.sleep(0.8)
        elif user_gesture == "Closed_Fist":
            audioDown(volume)
            time.sleep(0.8)
        elif user_gesture == "ILoveYou":
            time.sleep (0.5)
            pid = os.getpid()
            os.kill(pid, signal.SIGTERM)