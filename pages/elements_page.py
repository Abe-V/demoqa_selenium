import base64
import os
import random
import tempfile
import time
import requests
from requests.exceptions import InvalidSchema
from selenium.common import TimeoutException
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from data.checkbox_tree import CHECKBOX_TREE, EXPANDABLE_FOLDERS
from generator.generator import generated_person, generate_txt_file
from URLs.urls import ElementsPagesUrls
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators

# for each class respective URL will be assigned as 'url' argument for BasePage,
# and page with respective URL will be opened


class TextBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url=ElementsPagesUrls.text_box_page_url)
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
        super().__init__(driver, url=ElementsPagesUrls.check_box_page_url)
        self.open()
        try:
            self.remove_ad_banner()
            self.remove_footer()
        except Exception:
            pass

    locators = CheckBoxPageLocators()

    @staticmethod
    def normalize_name(title: str) -> str:
        return title.replace(' ', '').replace('.doc', '').lower()

    def get_all_tree_nodes(self):
        nodes = []
        for treenode in self.elements_are_present(self.locators.TREE_NODES):
            titles = treenode.find_elements(*self.locators.TREE_TITLE)
            if not titles:
                continue
            title = titles[0].text
            checkbox = treenode.find_element(*self.locators.TREE_CHECKBOX)
            aria_checked = checkbox.get_attribute('aria-checked')
            classes = treenode.get_attribute('class') or ''
            is_visible = treenode.is_displayed()
            if 'rc-tree-treenode-switcher-open' in classes:
                is_expanded = True
            elif 'rc-tree-treenode-switcher-close' in classes:
                is_expanded = False
            else:
                is_expanded = None
            nodes.append({
                'title': title,
                'aria_checked': aria_checked,
                'is_expanded': is_expanded,
                'is_visible': is_visible,
            })
        return nodes

    def _folder_exists_in_dom(self, title):
        locator = (
            self.locators.TREE_NODE_BY_TITLE[0],
            self.locators.TREE_NODE_BY_TITLE[1].format(title=title),
        )
        return bool(self.driver.find_elements(*locator))

    def _get_node_by_title(self, title):
        locator = (
            self.locators.TREE_NODE_BY_TITLE[0],
            self.locators.TREE_NODE_BY_TITLE[1].format(title=title),
        )
        return self.element_is_present(locator)

    def _expand_folder_if_closed(self, folder):
        if not self._folder_exists_in_dom(folder):
            return
        treenode = self._get_node_by_title(folder)
        classes = treenode.get_attribute('class') or ''
        if 'rc-tree-treenode-switcher-close' in classes:
            switcher = treenode.find_element(*self.locators.CLOSED_SWITCHER)
            self.go_to_element(switcher)
            switcher.click()
            time.sleep(0.2)

    def _get_closed_expandable_folders(self):
        closed = []
        for folder in EXPANDABLE_FOLDERS:
            if not self._folder_exists_in_dom(folder):
                continue
            treenode = self._get_node_by_title(folder)
            classes = treenode.get_attribute('class') or ''
            if 'rc-tree-treenode-switcher-close' in classes:
                closed.append(folder)
        return closed

    def expand_random_folders(self, count=None):
        if count is None:
            count = random.randint(0, 6)
        if count == 0:
            return
        to_expand = random.sample(EXPANDABLE_FOLDERS, min(count, len(EXPANDABLE_FOLDERS)))
        to_expand.sort(key=lambda name: EXPANDABLE_FOLDERS.index(name))
        for folder in to_expand:
            for node in self._get_ancestors_to_expand(folder):
                self._expand_folder_if_closed(node)

    def _get_ancestors_to_expand(self, folder):
        ancestors = []
        for parent, children in CHECKBOX_TREE.items():
            if folder in children:
                ancestors = self._get_ancestors_to_expand(parent) + [parent]
                break
        return ancestors + [folder]

    def get_visible_checkboxes(self):
        checkboxes = []
        for treenode in self.elements_are_present(self.locators.TREE_NODES):
            if treenode.is_displayed():
                checkboxes.append(treenode.find_element(*self.locators.TREE_CHECKBOX))
        return checkboxes

    def click_random_visible_checkboxes(self, count=None):
        visible_titles = [
            node['title'] for node in self.get_all_tree_nodes() if node['is_visible']
        ]
        if not visible_titles:
            return
        if count is None:
            count = random.randint(0, len(visible_titles))
        if count == 0:
            return
        for title in random.sample(visible_titles, count):
            treenode = self._get_node_by_title(title)
            checkbox = treenode.find_element(*self.locators.TREE_CHECKBOX)
            self.go_to_element(checkbox)
            checkbox.click()
            time.sleep(0.3)

    def get_result_text(self):
        result_items = self.driver.find_elements(*self.locators.RESULT_ITEMS)
        return [self.normalize_name(item.text) for item in result_items]

    def assert_parent_aria_states(self, nodes):
        nodes_by_title = {node['title']: node for node in nodes}
        for parent, children in CHECKBOX_TREE.items():
            if parent not in nodes_by_title:
                continue
            if not all(child in nodes_by_title for child in children):
                continue
            parent_node = nodes_by_title[parent]
            child_states = {nodes_by_title[child]['aria_checked'] for child in children}
            if child_states == {'false'}:
                expected = 'false'
            elif child_states == {'true'}:
                expected = 'true'
            else:
                expected = 'mixed'
            actual = parent_node['aria_checked']
            assert actual == expected, (
                f"Folder '{parent}': expected aria-checked='{expected}', got '{actual}'"
            )

    def _is_fully_checked(self, title, nodes_by_title):
        if title in nodes_by_title:
            return nodes_by_title[title]['aria_checked'] == 'true'
        for parent, children in CHECKBOX_TREE.items():
            if title in children:
                return self._is_fully_checked(parent, nodes_by_title)
        return False

    def _build_expected_result(self, nodes):
        nodes_by_title = {node['title']: node for node in nodes}
        expected = []

        def walk(title):
            if self._is_fully_checked(title, nodes_by_title):
                expected.append(self.normalize_name(title))
            for child in CHECKBOX_TREE.get(title, []):
                walk(child)

        walk('Home')
        return expected

    def assert_result_matches_checked_nodes(self, nodes):
        expected = self._build_expected_result(nodes)
        actual = self.get_result_text()
        assert sorted(actual) == sorted(expected), (
            f"Result mismatch: expected {expected}, got {actual}"
        )


class RadioButtonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=ElementsPagesUrls.radio_button_page_url)
        self.open()

    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, locator):
        button = self.element_is_visible(locator)
        button.click()
        return button.text

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=ElementsPagesUrls.web_table_page_url)
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
        rows = self.elements_are_present(self.locators.TABLE_ROWS)
        last_row = rows[-1]
        cells = last_row.find_elements(By.TAG_NAME, "td")
        return [cell.text for cell in cells[:6]]

    def search_some_person(self, key_word):
        search_input = self.element_is_visible(self.locators.SEARCH_INPUT)
        search_input.click()
        search_input.clear()
        search_input.send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        cells = row.find_elements(By.TAG_NAME, "td")
        return [cell.text for cell in cells[:6]]

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
        rows = self.driver.find_elements(*self.locators.TABLE_ROWS)
        return len(rows) == 0

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
        super().__init__(driver, url=ElementsPagesUrls.buttons_page_url)
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
        return clicked_buttons


class LinksPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=ElementsPagesUrls.links_page_url)
        self.open()

    locators = LinksPageLocators()

    def try_follow_the_link(self, locator):
        current_link = self.element_is_visible(locator)
        link_href = current_link.get_attribute('href')
        try:
            request = requests.get(link_href)
        except InvalidSchema:
            return link_href, "NOT VALID", "no_status_code"
        else:
            current_link.click()
            self.switch_to_new_tab()
            current_url = self.driver.current_url
            return link_href, current_url, request.status_code


class UploadAndDownloadPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=ElementsPagesUrls.upload_and_download_url)
        self.open()

    locators = UploadAndDownloadPageLocators

    def upload_file(self):
        # generating file on a local machine
        file_name, path = generate_txt_file()
        # send created file's path as a chosen file
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        # delete file from a local machine
        os.remove(path)
        # text = 'C:\fakepath\{real_file_name.ext}
        text = self.element_is_present(self.locators.UPLOADED_FILE).text
        return file_name.split('/')[-1], text.split('\\')[-1]

    def download_file(self):
        # gets links for downloading file
        link = self.element_is_clickable(self.locators.DOWNLOAD_FILE).get_attribute('href')
        # decodes base64 href into raw jpeg bytes
        link_b = base64.b64decode(link)
        # create new JPEG file on a local machine
        fd, path_name_file = tempfile.mkstemp(suffix='.jpeg', prefix='filetest')
        os.close(fd)
        # open created file and insert base16 code
        with open(path_name_file, 'wb+') as f:
            # '\xff\xd8' is a start of jpeg code (always)
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            # check_file = True if file exists and False if it doesn't exist
            check_file = os.path.exists(path_name_file)
            f.close()
            os.remove(path_name_file)
        return check_file


class DynamicPropertiesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=ElementsPagesUrls.dynamic_properties_url)
        self.open()

    locators = DynamicPropertiesPageLocators

    # Method gets text with dynamic ID
    def get_text(self):
        return self.element_is_present(self.locators.TEXT_WITH_RANDOM_ID).text

    # returns True if "Will enable 5 seconds" is clickable and False if not clickable (wait = 1 sec)
    def check_will_enable_5_seconds_button_clickability(self):
        try:
            self.element_is_clickable(self.locators.WILL_ENABLE_5_SECONDS_BUTTON, 0)
        except TimeoutException:
            return False
        return True

    # returns True if "Visible after 5 seconds" is clickable and False if not clickable (wait = 1 sec)
    def check_visible_after_5_seconds_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_5_SECONDS_BUTTON, 0)
        except TimeoutException:
            return False
        return True

    # returns current color of 'Color change' button
    def check_color_change_button_color(self):
        return self.element_is_present(self.locators.COLOR_CHANGE_BUTTON, 1).value_of_css_property('color')
