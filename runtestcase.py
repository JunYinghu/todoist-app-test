import unittest

from src.mobilefunc.taskverify import TaskFunc
from src.mobilefunc.projectverify import ProjectFunc
from src.todoapi.todoistapi import TodoistAPIFunc

project_name = "TestProjectPython"
project_verify_errorMessage = "not found created project" + project_name


def create_verify_project(api_endpoint, api_token):
    # step to create a new project
    api_token = api_token
    api_endpoint = api_endpoint
    project_api = TodoistAPIFunc()
    project_api.project_create(api_token, api_endpoint, project_name)
    project_api.project_get(api_token, api_endpoint, project_name)

    # step to verify the new created project on mobile
    verify_project = ProjectFunc()
    verify_project.connection_mobile()
    verify_project.login_todolist()
    # expected_project = verify_project.project_list(project_name)
    assert verify_project.verify_project(project_name) >= 1


def test_reopen_task(api_endpoint, api_token):
    task_mobile = TaskFunc()
    task_mobile.connection_mobile()
    task_mobile.login_todolist()
    task_mobile.create_task(project_name)
    task_api = TodoistAPIFunc()
    task_api.task_get(project_name)

# task_mobile.complete_task(project_name)
# task_api.task_reopen()
# task_mobile.verify_task_reopen(project_name)
