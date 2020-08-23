##from todoist.api import TodoistAPI
import todoist

from src.utility.commonfunc import CommonFunc


# api_token = 'df2f60dd323adfdede87b1dda718812dd0197da6'
# api_endpoint = 'https://api.todoist.com/sync/v8/sync/?sync_token=*'

class TodoistAPIFunc(object):

    def project_create(self, api_token, api_endpoint, project_name):
        project_api = todoist.api.TodoistAPI(api_token, api_endpoint)
        project_api.sync()
        project_add = project_api.projects.add(project_name, color=30)
        project_api.commit()
        print(project_add)

    def project_get(self, api_token, api_endpoint, project_name):
        api = todoist.api.TodoistAPI(api_token, api_endpoint)
        api.sync()
        for project in api.state['projects']:
            print(project['name'])

    def task_get(self, api_token, api_endpoint):
            api = todoist.api.TodoistAPI(api_token, api_endpoint)
            api.sync()

            item1 = api.items.add("Item1")
            api.commit()

            item1.update(content="UpdatedItem1")
            response = api.commit()
            assert response["items"][0]["content"] == "UpdatedItem1"
            assert "UpdatedItem1" in [i["content"] for i in api.state["items"]]
            assert api.items.get_by_id(item1["id"]) == item1

            item1.delete()
            api.commit()

    def task_reopen(self, api_token, api_endpoint):
            api = todoist.api.TodoistAPI(api_token, api_endpoint)
            api.sync()

            item1 = api.items.add("Item1")
            api.commit()

            item1.update(content="UpdatedItem1")
            response = api.commit()
            assert response["items"][0]["content"] == "UpdatedItem1"
            assert "UpdatedItem1" in [i["content"] for i in api.state["items"]]
            assert api.items.get_by_id(item1["id"]) == item1

            item1.delete()
            api.commit()
