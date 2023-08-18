import time

import locators.forms_page_locators
from pages.base_page import BasePage
from URLs.urls import FormsPagesUrls as url

# for each page-class respective URL will be assigned as url argument for BasePage,
# and page with respective URL will be opened


class PracticeFormPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=url.practice_form_url)
        self.open()

    locators = locators.forms_page_locators.PracticeFormPageLocators

    def fill_all_required_fields(self):
        pass

    def fill_random_unrequired_fields(self):
        pass

    def upload_file(self):
        pass

    def fill_fields_to_submit(self):
        pass
        # current_zoom = self.check_current_zoom()
        # all_zooms = [current_zoom]
        # for i in range(0, 8):
        #     zoom = current_zoom - 10
        #     self.set_page_zoom(zoom)
        #     current_zoom = self.check_current_zoom()
        #     all_zooms.append(current_zoom)
        #     time.sleep(1)
        # return all_zooms

    def click_submit(self):
        pass

    def check_the_form(self):
        pass
