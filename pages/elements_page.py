import base64
import os
import time
import random
import requests
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_file
from URLs.urls import AllURLs
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators


class TextBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url=AllURLs.TextBoxPage_URL)
        self.open()

    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.scroll_to_element(self.locators.SUBMIT)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = \
            self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url=AllURLs.CheckBoxPage_URL)
        self.open()

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULTS)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=AllURLs.RadioButtonPage_URL)
        self.open()

    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADOIBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADOIBUTTON,
                   'no': self.locators.NO_RADOIBUTTON}

        radio = self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=AllURLs.WebTablePage_URL)
        self.open()

    locators = WebTablePageLocators()

    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_clickable(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(Keys.HOME)
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(Keys.HOME)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(Keys.HOME)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(Keys.HOME)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(Keys.HOME)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(Keys.HOME)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for person in people_list:
            data.append(person.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(Keys.HOME)
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(Keys.HOME)
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    def delete_person_info(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        rows_per_page_button = self.element_is_present(self.locators.COUNT_ROW_LIST)
        count = [int(i) for i in rows_per_page_button.text.split() if i.isnumeric()]
        data = []
        for x in count:
            count_row_button = self.element_is_present(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=AllURLs.ButtonsPage_URL)
        self.open()

    locators = ButtonsPageLocators()

    def double_click_button(self):
        self.action_double_click(self.element_is_clickable(self.locators.DOUBLE_CLICK_BUTTON))
        return 'You have done a double click'

    def right_click_button(self):
        self.action_right_click(self.element_is_clickable(self.locators.RIGHT_CLICK_BUTTON))
        return 'You have done a right click'

    def dynamic_click_button(self):
        self.element_is_clickable(self.locators.DYNAMIC_CLICK_BUTTON).click()
        return 'You have done a dynamic click'

    def get_clicked_buttons(self):
        clicked_buttons = self.element_is_present(self.locators.ALL_CLICKED_BUTTONS_MESSAGE).text
        # data = []
        # for message in clicked_buttons:
        #     data.append(message.text)
        return clicked_buttons


class LinksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url=AllURLs.LinksPage_URL)
        self.open()

    locators = LinksPageLocators()

    def try_follow_the_link(self, locator):
        current_link = self.element_is_visible(locator)
        link_href = current_link.get_attribute('href')
        try:
            request = requests.get(link_href)
        except:
            return link_href, "NOT VALID", "no_status_code"
        else:
            current_link.click()
            self.switch_to_new_tab()
            current_url = self.driver.current_url
            return link_href, current_url, request.status_code


class UploadAndDownloadPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=AllURLs.UploadAndDownload_URL)
        self.open()

    locators = UploadAndDownloadPageLocators

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_FILE).text
        return file_name.split('/')[-1], text.split('\\')[-1]

    def download_file(self):
        link =  self.element_is_clickable(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = f"/Users/abeazovsky/Desktop/automation_qa_course/filetest{random.randint(0,999)}.jpeg"
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
            os.remove(path_name_file)
        return check_file
