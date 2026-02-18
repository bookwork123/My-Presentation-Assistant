import threading
from recognizer import recognizeGesture


def mapper():
    # start recognizer thread
    t = threading.Thread(
        target=recognizeGesture,
        daemon=True
    )

    t.start()

    t.join()

