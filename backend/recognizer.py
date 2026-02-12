from queue import Queue
import threading
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from camera import openCamera

frame_queue = Queue(maxsize=5)  # small buffer prevents lag
model_path = 'C:/Users/oscar/repositories/My-Presentation-Assistant/backend/model/gesture_recognizer.task'

# start camera thread
threading.Thread(
    target=openCamera,
    args=(0, frame_queue),
    daemon=True
).start()


BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a gesture recognizer instance with the live stream mode:
def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):  # type: ignore
    print('gesture recognition result: {}'.format(result))

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
with GestureRecognizer.create_from_options(options) as recognizer:
    while True:
        frame, timestamp_ms = frame_queue.get()

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=frame
        )

        recognizer.recognize_async(mp_image, timestamp_ms)

    
