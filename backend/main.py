from mapper import mapper
from audio import initiateAudio

def main():
    volume = initiateAudio()
    mapper(volume)

main()

