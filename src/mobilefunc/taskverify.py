import time

import allure

from src.mobilefunc.basicstep import BaseMobileFunc


class TaskFunc(BaseMobileFunc):

    @allure.step("crete task and returned created task name")
    def create_task(self, task_name):
        el_existing_task_list = self.driver.find_elements_by_class_name("android.widget.CheckBox")
        if len(el_existing_task_list) != 0:
            for task_checkbox in el_existing_task_list:
                task_checkbox.click()
        el_create_task_button = self.driver.find_element_by_id("com.todoist:id/fab")
        el_create_task_button.click()
        self.driver.find_element_by_id("android:id/message").set_value(task_name)
        el_create_task_add = self.driver.find_element_by_accessibility_id("Add")
        el_create_task_add.click()
        self.driver.keyevent(4)

    @allure.step("completed task")
    def complete_task(self):
        el_complete_task = self.driver.find_element_by_accessibility_id("Complete")
        el_complete_task.click()
        time.sleep(10)

    @allure.step("return a task name")
    def verify_task_reopen(self):
        el_reopen_task_verify = self.driver.find_element_by_id("com.todoist:id/text")
        # to show re-opened task on mobile
        time.sleep(10)
        return el_reopen_task_verify.text
