import time

import allure
import todoist


class TodoistAPIFunc(object):

    def project_create(self, api_token, api_endpoint, project_name):
        project_api = todoist.api.TodoistAPI(api_token, api_endpoint)
        project_api.sync()
        project_add = project_api.projects.add(project_name)
        project_api.commit()
        return project_add['id']

    # update_existing method has a randomly error that data showing on todolist but not retrieved
    @allure.step("update existing project which has the same or including the new created project string ")
    def project_update_existing(self, api_token, api_endpoint, project_name):
        api = todoist.api.TodoistAPI(api_token, api_endpoint)
        api.sync()
        for project in api.state['projects']:
            if (project['name'].find(project_name) != -1) or (project['name'] == project_name):
                self.project_update(api_token, api_endpoint, project['id'])

    @allure.step("update project name based on given project id")
    def project_update(self, api_token, api_endpoint, project_id):
        api = todoist.api.TodoistAPI(api_token, api_endpoint)
        project_update_api = api.projects.get_by_id(project_id)
        project_update_api.update(name='Autoupdate')
        api.commit()

    # this method to retrieve all items including 'completed'
    # this method can not retrieve the item created by mobile instantly
    @allure.step("retrieve all tasks and return an open task based on given task name")
    def task_get(self, api_token, api_endpoint, task_name):
        time.sleep(20)
        api = todoist.api.TodoistAPI(api_token, api_endpoint)
        api.sync()
        for task in api.state['items']:
            if (task['content'] == task_name) and (task['date_completed'] is None):
                # print(task)
                return task['id']

    @allure.step("re-opened a task based on given task id")
    def task_reopen(self, api_token, api_endpoint, task_id):
        api = todoist.api.TodoistAPI(api_token, api_endpoint)
        api.sync()
        item = api.items.get_by_id(task_id)
        item.update(date_completed={'date': 'None'})
        item.update(checked=0)
        item.update(in_history=0)
        api.commit()
        for task in api.state['items']:
            if task_id == task['id']:
                print(task)
