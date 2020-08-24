import allure

from src.mobilefunc.basicstep import BaseMobileFunc


class ProjectFunc(BaseMobileFunc):

    @allure.step("returned project count from searching result ")
    def verify_project(self, project_name):
        return self.search_project(project_name)
