# Instruction for MacOS

## How to install android runner

***Fork and Git Clone***

- 1. Click on the Fork icon in the top right hand corner once you're logged into Github.
- 2. Once it finishes loading, click on the green Code button. Run
  ```
  git clone git@github.com:[your_username]/android-runner.git
  ```
- 3. Type `cd android-runner` to enter the framework's main directory.


## Set up environment and dependencies

**Set up virtual environment**

Create a virtual environment: `python3 -m venv /path/`
This can be anywhere on your machine. Activate it with `source /path/bin/activate`

**Install dependencies (MacOS)**

1. Make sure you have [Homebrew](https://brew.sh/) installed
```
brew --version
```
  
2. Install OpenJDK8, sdk, and platform tools

Option 1: (for Emulation) Install OpenJDK 8, Android Studio and Platform Tools:
  ```
  brew install --cask temurin@8 android-studio android-platform-tools
  ```
  Option 2: (for Android Phone) Install OpenJDK 8, CommandLineTools and Platform Tools:
  ```
  brew install --cask temurin@8 android-commandlinetools android-platform-tools
  ```
  *If you meet the notice of outdated formulae, can `brew update && brew upgrade && brew cleanup` to upgrade all installed packages, and clean outdated ones.*


3. Install libxml2:
```
brew install libxml2
```

4. Check Java version:
   java -version, if you are running a different version than 1.8/8, `brew install jenv`
- Run `/usr/libexec/java_home -V` to see the location of your Java environments
- Copy the location of your AdoptOpenJDK8 environment:
  ```
  Run jenv add <AdoptOpenJDK8_path>
  Run jenv global 1.8
  ```
- Restart terminal and verify your Java version with java -version, it should output openjdk version "1.8.0_265"
- Install the requirements, under the android-runner: `pip install -r requirements.txt`

## Install the [Android Studio](https://developer.android.com/studio/install)
**NOT support Windows machines with ARM-based CPUs**

1. After installation, create a new project, preferly with less cumulative distribution (minimum SDK settings).
2. Run the created device, it would take a while to finish.
3. Check the running emulator ID：`adb devices`, it typically displays:
```
List of devices attached 
emulator-5554 device
```
4. Change the `devices` settings in `config.json` file using the displayed device identifier (with mapping to key-value pairs in `devices.json`).

