# todoist-app-test

Welcome to the todoist app test project



## Running test cases
This project is recommend Python 3.8
```bash
pytest runtestcase.py
```

## Development & Running Setup
### Build Project
This project is recommend Python 3.8

Clone the repo and enter it:

    $ git clone git@github.com:JunYinghu/todoist-app-test.git

Token and Url endpoint setup

```python
apitoken =<your todoist apitoken>
apiendpoint = https://api.todoist.com/sync/v8/sync/?sync_token=*
```

Android Emulator

Android studio is recommended.

Android version 7.0 is recommend

change to your deviceName

```python
       def connection_mobile(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android' 
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'TodoListAndroid_API_24'
        desired_caps['appPackage'] = 'com.todoist'
        desired_caps['appActivity'] = 'com.todoist.activity.HomeActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)
```


Appium 

Appium desktop Version 1.6.2

