from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def initiateAudio():
    device = AudioUtilities.GetSpeakers()
    interface = device._dev.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    print(f"Audio output: {device.FriendlyName}")
    print(f"- Muted: {bool(volume.GetMute())}")
    print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
    print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")

    return volume

def audioUp(volume):
    current_volume = volume.GetMasterVolumeLevel()
    max_volume = volume.GetVolumeRange()[1]
    increment = 1.0
    new_volume = min(current_volume + increment, max_volume)
    volume.SetMasterVolumeLevel(new_volume, None)

def audioDown(volume):
    current_volume = volume.GetMasterVolumeLevel()
    min_volume = volume.GetVolumeRange()[0]
    decrement = 1.0
    new_volume = max(current_volume - decrement, min_volume)
    volume.SetMasterVolumeLevel(new_volume, None)