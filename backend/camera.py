### Camera Opening & Operation
import numpy as np
import cv2 as cv
import time
from queue import Queue

### Opens the webcam and adds frames to the global queue
def openCamera(camType, frame_queue, state):
    #NOTE: camType relates to a value between 0 and 4, 
    #      which itself correlates to the specific camera used by the computer.
    #      If the computer has 1 camera, the value is typically 0.
    capture = cv.VideoCapture(camType, cv.CAP_DSHOW)
    if not capture.isOpened():
        print("ERROR: Camera never opened.")
        state["cam"] = False

    while True:
        ret, frame = capture.read()

        if not ret:
            state["cam"] = False
            print("ERROR: Cannot receive frame. Exiting...")
        
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        timestamp_ms = int(time.monotonic() * 1000)

        if frame_queue.full():
            try:
                frame_queue.get_nowait()
            except:
                pass


        frame_queue.put((frame, timestamp_ms))
