from backend.mapper import mapper
from backend.audio import initiateAudio

def main(state):
    volume = initiateAudio()
    mapper(volume, state)

if __name__ == "__main__":
    main(state={})

