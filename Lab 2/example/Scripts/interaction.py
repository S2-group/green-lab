from AndroidRunner.Device import Device
import time

# noinspection PyUnusedLocal
def main(device: Device, *args: tuple, **kwargs: dict):
    sessions = device.shell("cmd media_session list-sessions")
    while "tag=VLC" in sessions:
        time.sleep(1)
        sessions = device.shell("cmd media_session list-sessions")

