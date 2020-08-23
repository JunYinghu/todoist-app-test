from src.mobilefunc.projectverify import ProjectFunc
from src.mobilefunc.taskverify import TaskFunc
from src.todoapi.todoistapi import TodoistAPIFunc

project_name = "ProjectCreation"


def test_create_verify_project(api_endpoint, api_token):
    # step to create a new project
    project_api = TodoistAPIFunc()

    # delete existing project which has the same or including the new created project string
    # project_api.project_delete_existing(api_token, api_endpoint, project_name)

    project_api.project_create(api_token, api_endpoint, project_name)

    # step to verify the new created project on mobile
    verify_project = ProjectFunc()
    verify_project.connection_mobile()
    verify_project.login_todolist()

    # expected_project = verify_project.project_list(project_name)

    # verify project on mobile and only 1 project showing in search result
    assert verify_project.verify_project(project_name) >= 1


def test_reopen_task(api_token, api_endpoint):
    task_api = TodoistAPIFunc()

    # go to mobile to add 1 task
    # return to task name
    task_mobile = TaskFunc()
    task_mobile.connection_mobile()
    task_mobile.login_todolist()
    task_name = task_mobile.create_task()

    # verify task via api task_id
    task_id = task_api.task_get(api_token, api_endpoint, task_name)
    assert task_id is not None

    # change to mobile and complete the task
    task_mobile.complete_task()
    # re-open the task via api
    task_api.task_reopen(api_token, api_endpoint, task_id)

    # verify re-opened task name on mobile showing
    assert task_mobile.verify_task_reopen() == task_name
