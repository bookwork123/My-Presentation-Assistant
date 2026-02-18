### Camera Opening & Operation
import numpy as np
import cv2 as cv
import time

### Opens the webcam and adds frames to the global queue
def openCamera(camType, frame_queue):
    #NOTE: camType relates to a value between 0 and 4, 
    #      which itself correlates to the specific camera used by the computer.
    #      If the computer has 1 camera, the value is typically 0.
    capture = cv.VideoCapture(camType, cv.CAP_DSHOW)
    if not capture.isOpened():
        print("ERROR: Camera never opened.")
        return 1 #NOTE: This value will tell the GUI what error message to throw
    try:
        while True:
            ret, frame = capture.read()

            if not ret:
                print("ERROR: Cannot receive frame. Exiting...")
                return 2
            
            timestamp_ms = int(time.monotonic() * 1000)

            frame_queue.put((frame, timestamp_ms))
    except KeyboardInterrupt:
        #NOTE: Press Ctrl+C to end the program at the moment. GUI implementation will add a stop button.
        capture.release()
        cv.destroyAllWindows