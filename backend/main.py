from backend.mapper import mapper
from backend.audio import initiateAudio
import comtypes

def main(state):
    comtypes.CoInitialize()
    try:
        volume = initiateAudio()
        mapper(volume, state)
    finally:
        comtypes.CoUninitialize()  # clean up COM when done

if __name__ == "__main__":
    main(state={})

