from queue import Queue
import threading
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from backend.camera import openCamera

# global queue for recognizer to grab frames from
frame_queue = Queue(maxsize=5)  # small buffer prevents lag
model_path = 'C:/Users/oscar/repositories/My-Presentation-Assistant/backend/model/gesture_recognizer.task'



# Gesture Recognizer configuration
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode


latest_gesture = None

# Logging function
def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):  # type: ignore
    global latest_gesture
    if result.gestures:
        gesture = result.gestures[0][0]  # First hand, top gesture
        print("GESTURE: " + gesture.category_name)
        print("CONFIDENCE: " + str(gesture.score))
        latest_gesture = gesture.category_name

# Create a gesture recognizer instance with the live stream mode:
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)

### Creates the GestureRecognizer object and runs a loop that grabs camera frames and analyzes them
def recognizeGesture(state):

    # start camera thread
    threading.Thread(
        target=openCamera,
        args=(0, frame_queue, state),
        daemon=True
    ).start()
    last_timestamp = -1 # starter value for timestamp check

    with GestureRecognizer.create_from_options(options) as recognizer:
        while True:
            try:
                frame, timestamp_ms = frame_queue.get()
            except:
                continue

            # ensure newest timestamp is always greater than previous timestamp
            if timestamp_ms <= last_timestamp:
                timestamp_ms = last_timestamp + 1
            last_timestamp = timestamp_ms


            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=frame
            )
            recognizer.recognize_async(mp_image, timestamp_ms)  # result handled by callback