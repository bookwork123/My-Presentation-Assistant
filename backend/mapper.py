import threading
import pyautogui
import recognizer
from recognizer import recognizeGesture
import time



def mapper():
    t = threading.Thread(
        target=recognizeGesture,
        daemon=True
    )
    t.start()

    # Helps prevent duplicate actions
    last_gesture = None

    while True:
        user_gesture = recognizer.latest_gesture

        if user_gesture == last_gesture:
            continue

        last_gesture = user_gesture

        if user_gesture is None:
            continue

        recognizer.latest_gesture = None
        if user_gesture == "Thumb_Up":
            pyautogui.press('right')
            print("RIGHT!")
            time.sleep(0.8)
        elif user_gesture == "Thumb_Down":
            pyautogui.press('left')
            print("LEFT!")
            time.sleep(0.8)


