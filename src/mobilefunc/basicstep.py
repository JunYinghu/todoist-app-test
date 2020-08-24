import allure
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '7.0'
DEVICE_NAME = 'Pixel_XL_API_30'


# Pixel_XL_API_30
# TodoistAndroid_API_24

class BaseMobileFunc(object):

    @allure.step("build mobile connection")
    def connection_mobile(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': PLATFORM_VERSION, 'deviceName': DEVICE_NAME,
                        'appPackage': 'com.todoist', 'appActivity': 'com.todoist.activity.HomeActivity'}
        self.driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)
        self.driver.implicitly_wait(60)

    @allure.step("login todo ist with email method")
    def login_todoist(self, email_id, password):
        self.driver.find_element_by_id("com.todoist:id/btn_welcome_email").click()
        try:
            self.driver.find_element_by_id("com.google.android.gms:id/credential_primary_label").click()
            try:
                self.driver.find_element_by_id("android:id/button3").click()
            except NoSuchElementException:
                print("continue")
        except NoSuchElementException:
            el_login_email_id = self.driver.find_element_by_id("com.todoist:id/email_exists_input")
            el_login_email_id.send_keys(email_id)
            self.driver.find_element_by_id("com.todoist:id/btn_continue_with_email").click()
            self.driver.find_element_by_id("com.todoist:id/log_in_password").set_value(password)
            self.driver.find_element_by_id("com.todoist:id/btn_log_in").click()

    @allure.step("go to menu list")
    def change_view(self):
        el_change_view = self.driver.find_element_by_accessibility_id("Change the current view")
        el_change_view.click()

    @allure.step("search project based given project name")
    def search_project(self, searched_project):
        project_found_count = 0
        el_search_button = self.driver.find_element_by_id("com.todoist:id/menu_content_search")
        el_search_button.click()
        # el_search_project_item_button = self.driver.find_element_by_xpath(
        #    "//androidx.appcompat.app.ActionBar.c[@content-desc='Projects']/android.widget.TextView")
        el_search_project_item_button = self.driver.find_element_by_accessibility_id("Projects")
        el_search_project_item_button.click()
        el_search_project_keyword = self.driver.find_element_by_id("com.todoist:id/search_edit_text")
        el_search_project_keyword.set_value(searched_project)
        self.driver.keyevent(66)

        el_project_name_list = self.driver.find_elements_by_class_name('android.widget.TextView')
        for project in el_project_name_list:
            if project.text == searched_project:
                project_found_count = project_found_count + 1
        return project_found_count

    @allure.step("Open project from search result based on given project name")
    def open_project(self, open_project):
        el_project_name_list = self.driver.find_elements_by_class_name('android.widget.TextView')
        for project in el_project_name_list:
            if project.text == open_project:
                project.click()
                break

    @allure.step("Back to todoist home page from search page")
    def back_main_page_from_search(self):
        self.driver.find_element_by_id("com.todoist:id/action_mode_close_button").click()

    @allure.step("user logout")
    def user_logout(self):
        self.driver.find_element_by_android_uiautomator('text("Settings")').click()
        try:
            self.driver.find_element_by_android_uiautomator('text("Log out")').click()
        except NoSuchElementException:
            self.swipe_down()
        self.driver.find_element_by_android_uiautomator('text("Log out")').click()
        self.driver.find_element_by_id('android:id/button1').click()

    @allure.step("quit driver")
    def quit_driver(self):
        self.driver.quit()

    def swipe_down(self):
        count = 0
        while count < 12:
            self.driver.keyevent(20)
            count += 1