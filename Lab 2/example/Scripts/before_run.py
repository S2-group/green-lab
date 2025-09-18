from AndroidRunner.Device import Device


# noinspection PyUnusedLocal
def main(device: Device, *args: tuple, **kwargs: dict):
    
    current_run = kwargs["current_run"]
    video_res = current_run["experimentArg"]
    device.launch_activity(current_run["path"], 
                           activity=".StartActivity", 
                           action="android.intent.action.VIEW", 
                           data_uri=f"file:///sdcard/Download/videos/test_video_{video_res}.mp4")
