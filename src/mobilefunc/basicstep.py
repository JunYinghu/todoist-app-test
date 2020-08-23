from appium import webdriver


class BaseMobileFunc(object):

    def connection_mobile(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'TodoListAndroid_API_24'
        desired_caps['appPackage'] = 'com.todoist'
        desired_caps['appActivity'] = 'com.todoist.activity.HomeActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def login_todolist(self):
        el_login_with_email_button = self.driver.find_element_by_id("com.todoist:id/btn_welcome_email")
        el_login_with_email_button.click()
        el_login_with_email_select = self.driver.find_element_by_id(
            "com.google.android.gms:id/credential_primary_label")
        el_login_with_email_select.click()
        el_login_time_zone = self.driver.find_element_by_id("android:id/button3")
        if el_login_time_zone.is_displayed():
            el_login_time_zone.click()

    def change_view(self):
        el_change_view = self.driver.find_element_by_accessibility_id("Change the current view")
        el_change_view.click()

    def exit_todoist(self):
        self.change_view()
        el_setting_button = self.driver.find_element_by_android_uiautomator('text("Settings")')
        el_setting_button.click()
        el_setting_logout = self.driver.find_element_by_android_uiautomator('text("Log out")')
        el_setting_logout.click()

    def search_project(self, searched_project):
        project_found_count = 0
        el_search_button = self.driver.find_element_by_id("com.todoist:id/menu_content_search")
        el_search_button.click()
        el_search_project_item_button = self.driver.find_element_by_xpath(
            "//androidx.appcompat.app.ActionBar.c[@content-desc='Projects']/android.widget.TextView")
        el_search_project_item_button.click()
        el_search_project_keyword = self.driver.find_element_by_id("com.todoist:id/search_edit_text")
        el_search_project_keyword.set_value(searched_project)
        self.driver.keyevent(66)

        el_project_name_list = self.driver.find_elements_by_class_name('android.widget.TextView')
        for project in el_project_name_list:
            print(project.text)
            if project.text == searched_project:
                project_found_count = project_found_count + 1
        return project_found_count

    def open_project(self, open_project):
        # el_open_project = self.driver.find_element_by_android_uiautomator('text(' + '\"' + open_project + '\"' + ')')
        el_project_name_list = self.driver.find_elements_by_class_name('android.widget.TextView')
        for project in el_project_name_list:
            if project.text == open_project:
                project.click()
                break
