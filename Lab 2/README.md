# Lab Setup
We provide an example experiment config that will be discussed during the lab. Copy this to your own install of android-runner if you want to test it out, otherwise create a new experiment that you can work with.

⚠️ Note that this lab was tested mainly on linux, however essentially all of these tools should additionally work through WSL or OSX. Just note that there might be some difficulties especially if you want to view the screen of your emulator.

### Follow the instructions for setting up android-runner
- Clone the [android-runner](https://github.com/S2-group/android-runner) repository
- Install python & java dependencies
- Install [adb](https://developer.android.com/tools/adb) (android debug bridge)
- Install [sdkmanager](https://developer.android.com/tools/sdkmanager) (android software development kit)
- For more in-depth instructions refer to the [android-runner wiki](https://github.com/S2-group/android-runner/wiki/Setup)

### Dependencies for emulation
- [avdmanager](https://developer.android.com/tools/avdmanager) (android virtual device manager)
- [emulator](https://developer.android.com/studio/run/emulator-commandline) (command line tool)

Installing these dependencies can differ between operating systems, however these tools are generally included in the android [cmdline-tools package](https://developer.android.com/tools). These tools can also be installed through the sdkmanager. Check which method is best for your system.

# EX 1 - Setting up a Device or Emulator
For this warm up exercise you will finalize your installation and configuration of android-runner by connecting either your own device, or an emulator if you don't have an android.

## Setting up a physical device
- [Enable developer mode](https://developer.android.com/studio/debug/dev-options) on the device, as well as debug over usb functionality.
- Connect it to your computer, and make sure the device is on and unlocked.
- Use `adb devices` to show the id of your connected device, which is needed to configure android-runner.

Now everything is setup, and you should be able to run commands on your device using `adb shell`. Test this out with any host of linux commands you should be familiar with, for example: `adb shell ls`.

## Setting up an emulator
- Use `sdkmanager --list` to display available kits, we want to select an entry with tagged with 'system-images'.
- Once you have a system image selected, install it as follows: `sdkmanager "system-images;android-34;google_apis;x86_64"`
- And lastly, create the virtual device with `avdmanager create avd -n test -k "system-images;android-34;google_apis;x86_64"`

Now you should have a avd created! To verify this we can use the `avdmanager list avd` command, you should see something like below:

```
Available Android Virtual Devices:
    Name: pixel_6
  Target: Default Android System Image
          Based on: Android 15.0 ("VanillaIceCream") Tag/ABI: default/x86_64
  Sdcard: 512 MB
```

To start your device, we use the android emulator with the -avd argument, and the name of our device. For example: `emulator -avd pixel_6`.

Now that the avd is started, we can use adb as expected. Run any command using adb to verify, like: `adb shell ls`.

# EX 2 - Measuring a New Target
In this exercise you will choose a new target to measure, and interface with that target. The goal for this phase should be to launch that app on the device you connected in the previous exercise.

There are many targets to choose from, you might already have some installed!

### Target ideas:
- Browsers (chrome firefox ect.) 
- Video playback (streaming vs. downloaded) 
- Games 
- Different device configurations (power saving mode ect.), with some workload 

## Installing apps
To install your desired app on a physical device, simply use the app store. 

If you are emulating, you will have to download the package as an apk onto your host system first. Sites like [apkpure.com](https://apkpure.com/) provide a wide selection of android apks, including versions for older android machines. 

⚠️ Note: We do not recommend installing apps like this on your personal devices, for security reasons.

## Starting your app via the command line
Once you have your target selected and installed, we want to determine how to launch this application. For this you need the application id, we can list all the installed packages using the command: `adb shell pm list packages`. You should get a long list of application ids as follows:

```
...
package:com.android.se
package:com.android.systemui.emulation.pixel_7a
package:com.android.pacprocessor
package:com.android.messaging
...
```

The next step is starting the desired application, for this we use the android utility `am` which lets us start an application using androids intent system. This is a form of IPC that allows apps to request actions from each other.

To get the default activity for an app we can use the following command: `adb shell cmd package resolve-activity --brief <app id>`. This should provide something similar to the following output.

```
priority=0 preferredOrder=0 match=0x108000 specificIndex=-1 isDefault=true
com.android.messaging/.ui.conversationlist.ConversationListActivity
```

We can then use this activity to start the app instance, if we wanted to open the messaging app we could use the command:

```bash
adb shell am start -n com.android.messaging/.ui.conversationlist.ConversationListActivity
```

## Starting apps through android-runner
Android runner defines an interface to make programatically interacting with adb a bit easier. Each python script from the Scripts directory is executed at a different stage of the experiment, and they each pass a Device object for you to use. Take a quick look through the definition of the Device class, many helpful functions are defined like `pull` and `push` to move files between your computer and device.

Any apps you specify in the 'apps' section of the **config.json** will be treated as test cases, and auto started at the same point as 'before_run'. You can then interact with the app yourself, or define actions using the android command line tool input. For instance `device.shell("input tap 100 200")`, which taps the screen at x=100, y=200.

If you want to start the app yourself, you can disable auto start by adding `"autostart_subject": false` to your **config.json** file. Then you are responsible for starting the application yourself. In the example experiment the VLC app is started as follows:

```python
device.launch_activity("org.videolan.vlc", 
                       activity=".StartActivity", 
                       action="android.intent.action.VIEW", 
                       data_uri=f"file:///sdcard/Download/videos/test_video_480.mp4")
```

Many android apps can take a data_uri argument which allows you to specify something for the app to interact with, such as a web address for a browser.

## Callbacks in android-runner
Android runner uses a callback system to structure experiments. This means that the experiment is broken down into a set of events. Each event calls a function you define in the scripts directory. Its not necessary to define all callbacks. Only the ones that you need are required to be defined, and referenced within your `config.json` file.

The following callbacks are available:
- `before_experiment` is run once **before any** experiments are executed. This can be used to setup the environment on the device.
- `before_run` is executed once **for each run** in the experiment. This can be used to setup any dependencies, or start applications manually.
- `after_launch` is executed once **for each run**, after the application has been launched.
- `interaction` is executed once **while each run** in the experiment is ongoing. Leave this empty if no user interaction is needed.
- `before_close` is executed once **for each run** before the application being tested is closed. This can be used to manually close applications, or remove dependencies.
- `after_run` is executed once **after each run** in the experiment has been completed.
- `after_experiment` is executed once **after all runs** in the experiment have been completed. This can be used to break down the environment, and uninstall any applications no longer needed.

For each script you have defined, a corresponding entry can be made in your `config.json`. For example:
```json
"scripts": {
    "before_experiment": "Scripts/before_experiment.py",
    "before_run": "Scripts/before_run.py",
    "after_launch": "Scripts/after_launch.py",
    "interaction": [
      {
        "type": "python3",
        "path": "Scripts/interaction.py",
        "timeout": 500,
        "logcat_regex": "some keyword"
      }
    ],
    "before_close": "Scripts/before_close.py",
    "after_run": "Scripts/after_run.py",
    "after_experiment": "Scripts/after_experiment.py"
  },
```
# EX 3 - Using Profilers
In this last exercise you will implement a different profiler, or parameters for perfetto. Make sure to configure your target workload to run long enough to be properly measured, adding a sleep into the code and interacting with the device yourself is fine for this lab, and complex interactions like games.

## Working with Perfetto
Perfetto is the default tool for android system tracing since android 9. Its a powerful tool for collecting metrics, nd supports a wide range of different data sources. The example experiments uses the `android.power` and `linux.sys_stats` sources, but many more are available. Perfetto will only measure the stats that you tell it to. You can read more about available sources and stats [here](https://perfetto.dev/docs/concepts/config) (under Android Data Sources in the sidebar). The **perfetto_config.pbtx** in the example experiment can be used as a starting point.

A full definition for the perfetto pbtx file can be found [here](https://perfetto.dev/docs/reference/trace-config-proto), use this when you want to configure your new data sources or modify existing ones.

As an output perfetto generates a binary file containing all of the data it collected, this file will be placed in the automatically created 'output' folder once the experiment has been run. There are two ways of interacting with this file:

- Using the website [ui.perfetto.dev](https://ui.perfetto.dev), which provides a GUI. 
- Or it can be programatically interacted with using the [TraceProcessor](https://perfetto.dev/docs/analysis/trace-processor-python) python library. 

Below is an example of how you can convert these traces to csv format, also included in the example experiment.
```python
for perfetto_trace_file in os.listdir(path):
    tp = TraceProcessor(trace=os.path.join(path, perfetto_trace_file))
    
    # The basic perfetto tables are: slices, counters, and tracks
    data = tp.query("SELECT * FROM counters").as_pandas_dataframe()
    data.to_csv(os.path.join(path, f"{perfetto_trace_file.split(".")[0]}_aggregated.csv"))
```

## Selecting a new profiler
Android-runner also provides a host of other profilers if perfetto does not have the stats you want, or if you just want to experiment. To specify a profiler, change the "profilers" section of the **config.json** file to include the profiler you want, and any other relevant configuration like the sample interval. The android-runner repository has many more extensive examples.

### Available profilers:
- Android profiler
- BatteryManager 
- Frametimes 
- Garbage collection 
- Perfetto 
- Perfume js 

As a small demonstration, if I wanted to add the Android profiler to measure cpu and memory, this is done with the following entry:

```json
"Android": {
  "subject_aggregation": "none",
  "experiment_aggregation" : "none",
  "sample_interval": 0,
  "data_points": ["cpu", "mem"]
}
```

### ⚠️ A note on Batterymanager:
This profiler requires installing an apk on the host system, and interfaces with the profiler provided with android-runner. The batterymanager apk can be found [here](https://github.com/S2-group/batterymanager-companion).

## Running you experiment
After this step is done, your new experiment should be ready to run! 

This can be done by running the following command from your project root directory: `python . <path/to/my/config.json>`. This should generate an output directory containing generated csv file and whatever other artifacts you export.

