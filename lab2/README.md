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
***Set up virtual environment***
Create a virtual environment: `python3 -m venv /path/`
This can be anywhere on your machine. Activate it with `source /path/bin/activate`

***Install dependencies(MacOS)***

- Make sure you have [Homebrew](https://brew.sh/) installed
- Install OpenJDK 8, Android SDK and Platform Tools:
  ```
  brew install --cask temurin@8 android-sdk android-platform-tools
  ```
  
*If want to update outdated formulae, can `brew update && brew upgrade && brew cleanup` to upgrade and all installed packages, clean outdated ones.*


- Install libxml2: `brew install libxml2`
- Check Java version: java -version, if you are running a different version than 1.8/8, `brew install jenv`
Run `/usr/libexec/java_home -V` to see the location of your Java environments
Copy the location of your AdoptOpenJDK8 environment
`Run jenv add <AdoptOpenJDK8_path>`
`Run jenv global 1.8`
Restart terminal and verify your Java version with java -version, it should output openjdk version "1.8.0_265"
Verify that monkeyrunner works with monkeyrunner --version, it should output unrecognized argument and no other errors
Install the requirements, under the android-runner: `pip install -r requirements.txt`


