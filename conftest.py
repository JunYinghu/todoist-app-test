import pytest
import todoist


def pytest_addoption(parser):
    parser.addoption("--endpoint", help="Set up the test endpoint")
    parser.addini("apiendpoint", help="Set up the test endpoint")
    parser.addoption("--token", help="Set up the API token")
    parser.addini("apitoken", help="Set up the API token")


@pytest.fixture
def cleanup(api_endpoint, api_token):
    _cleanup(api_endpoint, api_token)


@pytest.fixture
def api_endpoint(request):
    endpoint = request.config.getini("apiendpoint")
    if not endpoint:
        endpoint = request.config.getoption("--endpoint")
    if not endpoint:
        raise RuntimeError(
            "Test endpoint not defined. Please use the "
            '--endpoint commandline option, or the "endpoint" '
            "attribute in your pytest.ini"
        )
    return endpoint


@pytest.fixture
def api_token(request):
    token = request.config.getini("apitoken")
    if not token:
        token = request.config.getoption("--token")
    if not token:
        raise RuntimeError(
            "API token not defined. Please use the --token "
            'commandline option, or the "token" attribute in '
            "your pytest.ini"
        )
    return token


def _cleanup(api_endpoint, api_token):
    api = todoist.api.TodoistAPI(api_token, api_endpoint)
    api.sync()
    for item in api.state["items"][:]:
        item.delete()
    api.commit()
    for project in api.state["projects"][:]:
        if project["name"] != "Inbox":
            project.delete()
    api.commit()
