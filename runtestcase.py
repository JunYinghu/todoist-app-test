import allure
import pytest

from src.mobilefunc.projectverify import ProjectFunc
from src.mobilefunc.taskverify import TaskFunc
from src.todoapi.todoistapi import TodoistAPIFunc

CREATED_PROJECT_NAME = "Python Creation"
TASK_NAME = "Task Creation"
EMAIL_ID = ""
PASSWORD = ""


@allure.description("To test project created via API")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_verify_project(api_token, api_endpoint):
    project_api = TodoistAPIFunc()
    project_api.project_update_existing(api_token, api_endpoint, CREATED_PROJECT_NAME)
    project_api.project_create(api_token, api_endpoint, CREATED_PROJECT_NAME)

    verify_project = ProjectFunc()
    verify_project.connection_mobile()
    verify_project.login_todoist(EMAIL_ID, PASSWORD)

    # due to the update_existing method, to verify project count more than 1
    assert verify_project.verify_project(CREATED_PROJECT_NAME) >= 1

    verify_project.back_main_page_from_search()
    verify_project.change_view()
    verify_project.user_logout()
    verify_project.quit_driver()


@allure.description("To test verify task reopen via API")
@allure.severity(allure.severity_level.CRITICAL)
def test_reopen_task(api_token, api_endpoint):
    task_mobile = TaskFunc()
    task_mobile.connection_mobile()
    task_mobile.login_todoist(EMAIL_ID, PASSWORD)
    task_mobile.create_task(TASK_NAME)

    task_api = TodoistAPIFunc()
    task_id = task_api.task_get(api_token, api_endpoint, TASK_NAME)
    assert task_id is not None

    task_mobile.complete_task()
    task_api.task_reopen(api_token, api_endpoint, task_id)

    assert task_mobile.verify_task_reopen() == TASK_NAME

    task_mobile.change_view()
    task_mobile.user_logout()
    task_mobile.quit_driver()


if __name__ == "__main__":
    pytest.main(["-s", "runtestcase.py"])
