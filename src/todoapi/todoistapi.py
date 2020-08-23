import todoist


class TodoistAPIFunc(object):

    def project_create(self, api_token, api_endpoint, project_name):
        project_api = todoist.api.TodoistAPI(api_token, api_endpoint)
        project_api.sync()
        project_add = project_api.projects.add(project_name)
        project_api.commit()
        print(project_add)
        return project_add['id']

    def project_delete_existing(self, api_token, api_endpoint, project_name):
        api = todoist.api.TodoistAPI(api_token, api_endpoint)
        api.sync()
        for project_item in api.state['projects']:
            # if project_item["name"] != "Inbox":
            #     project_item.delete()
            print(project_item)

    def project_delete(self, api_token):
        api = todoist.api.TodoistAPI(api_token)
        api.sync()
        project_deleted_api = api.projects.get_by_id('$316258e5-e378-11ea-a382-00e18c41a16c')
        project_deleted_api.delete()
        api.commit()

    def task_get(self, api_token, api_endpoint, task_name):
        api = todoist.api.TodoistAPI(api_token, api_endpoint)
        api.sync()
        for task in api.state['items']:
            if task['content'] == task_name:
                return task['id']
                break

    def task_reopen(self, api_token, api_endpoint, task_id):
        api_token = api_token
        api_endpoint = api_endpoint
        api = todoist.api.TodoistAPI(api_token, api_endpoint)
        api.sync()
        item = api.items.get_by_id(task_id)
        # item.update(date_completed=None)
        item.update(checked=0)
        item.update(in_history=0)
        api.commit()
        for task in api.state['items']:
            print(task)
