from src.mobilefunc.basicstep import BaseMobileFunc


class ProjectFunc(BaseMobileFunc):

    def project_list(self, project_name):
        self.change_view()
        el_project_expend = self.driver.find_element_by_android_uiautomator('text("Projects")')
        el_project_expend.click()

        el_project_manage = self.driver.find_element_by_android_uiautomator('text("Manage projects")')
        if el_project_manage.is_displayed():
            el_project_manage.click()
        else:
            self.driver.keyevent(93)
        el_project_name = self.driver.find_element_by_android_uiautomator('text(' + '\"' + project_name + '\"' + ')')
        if el_project_name.is_displayed():
            return el_project_name.text
        else:
            return "no found"

    def verify_project(self, project_name):
        return self.search_project(project_name)
