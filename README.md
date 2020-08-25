# todoist-app-test

Welcome to the todoist app test project. this project is designed to test an application <todoist> on Android device only.

This project is recommend Python 3.8 with pytest framework

Test cases were tested successfully on 2 models (Android devices) with different display resolution but recommend high resolution

## Running test cases
 The recommended way to run your tests would be in Pytest framework:
```bash
pytest runtestcase.py
```

## Run test with Allure Report and Generated Allure Report
This project is integrated with Allure Report

```bash
   pytest runtestcase.py -v -s --alluredir="<allure report path>" 
```
```bash
   allure serve <allure report path>
```

## Running Conditions
In order to run test cases without breaks:  
1. you should have a registered account with email login method
2. Either deletion of existing project <**ProjectCreation** > or replacing of project name <**ProjectCreation**>
3. Delete existing task name with string <**testtask**>

```python
project_name = "ProjectCreation"
```


## Development & Running Setup
### Build Project
This project is recommend Python 3.8

Clone the repo and enter it:

    $ git clone git@github.com:JunYinghu/todoist-app-test.git

### Token and Url endpoint setup

pytest.ini
```python
API_TOKEN = <your todoist apitoken>
API_ENDPOINT = https://api.todoist.com/sync/v8/sync/?sync_token=*
```
### Email setup
runtestcase.py
```python
EMAIL_ID = "<your email id>"
PASSWORD = "<your email password>"
```

### Android Emulator

Android studio is recommended.

Android version 7.0 is recommend

basicstep.py

```python
APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '7.0'
DEVICE_NAME = 'TodoistAndroid_API_24'

    def connection_mobile(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': PLATFORM_VERSION, 'deviceName': DEVICE_NAME,
                        'appPackage': 'com.todoist', 'appActivity': 'com.todoist.activity.HomeActivity'}
        self.driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)
        self.driver.implicitly_wait(60)
```


### Appium 

Appium desktop Version 1.6.2 or above

### Allure Report
Allure Report 2.13.5

### Reference
##### [Install Python](https://www.python.org/downloads/)
##### [install Appium](https://github.com/appium/appium-desktop/releases/tag/v1.18.0-1)
##### [Install Android Studio](https://developer.android.com/studio)
##### [Install Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)
#### [Install Allure Report](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/)
##### Tested Android apk - you may get the tested Android apk from resource folder in this project
