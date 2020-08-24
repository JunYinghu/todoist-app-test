import pytest

from appium import webdriver


def pytest_addoption(parser):
    parser.addoption("--endpoint", help="Set up the test endpoint")
    parser.addini("API_ENDPOINT", help="Set up the test endpoint")
    parser.addoption("--token", help="Set up the API token")
    parser.addini("API_TOKEN", help="Set up the API token")
    parser.addini('DEVICE_NAME', help='Set up the device name')
    parser.addini('PLATFORM_VERSION', help='Setup the device version')
    parser.addini("APPIUM_LOCAL_HOST_URL", help='Setup the appium server url')


@pytest.fixture
def api_endpoint(request):
    endpoint = request.config.getini("API_ENDPOINT")
    if not endpoint:
        endpoint = request.config.getoption("--endpoint")
    if not endpoint:
        raise RuntimeError(
            "Test endpoint not defined. Please use the "
            '--endpoint commandline option, or the "API_ENDPOINT" '
            "attribute in your pytest.ini"
        )
    return endpoint


@pytest.fixture
def api_token(request):
    token = request.config.getini("API_TOKEN")
    if not token:
        token = request.config.getoption("--token")
    if not token:
        raise RuntimeError(
            "API token not defined. Please use the --token "
            'commandline option, or the "API_TOKEN" attribute in '
            "your pytest.ini"
        )
    return token


@pytest.fixture
def device_name(request):
    return request.config.getoption('DEVICE_NAME')


@pytest.fixture
def platform_version(request):
    return request.config.getoption('PLATFORM_VERSION')


@pytest.fixture
def appium_server(request):
    return request.config.getoption('APPIUM_LOCAL_HOST_URL')


android_caps = [{
    'deviceName': device_name,
    'platformName': 'Android',
    'platformVersion': platform_version,
    'appPackage': 'com.todoist',
    'appActivity': 'com.todoist.activity.HomeActivity'
}]


@pytest.fixture(params=android_caps)
def connection_mobile(request):
    desired_caps = request.param
    driver = webdriver.Remote(appium_server, desired_caps)
    driver.implicitly_wait(60)
    return driver
