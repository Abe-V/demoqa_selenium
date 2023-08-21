import random
import time

from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# my directories imports
import locators.forms_page_locators
from generator.generator import generated_person
from pages.base_page import BasePage
from URLs.urls import FormsPagesUrls as url


# for each page-class respective URL will be assigned as url argument for BasePage,
# and page with respective URL will be opened


class PracticeFormPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=url.practice_form_url)
        self.open()

    locators = locators.forms_page_locators.PracticeFormPageLocators

    # methods to fill required fields
    def choose_gender(self):
        genders = [
            self.locators.MALE_RADIO_BUTTON,
            self.locators.FEMALE_RADIO_BUTTON,
            self.locators.OTHER_GENDER_RADIO_BUTTON
        ]
        button = self.element_is_visible(random.choice(genders))
        button.click()
        return button.text

    def fill_required_fields(self):
        person = next(generated_person())
        first_name = person.first_name
        last_name = person.last_name
        mobile = person.phone_number
        self.element_is_present(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
        self.element_is_present(self.locators.LAST_NAME_INPUT).send_keys(last_name)
        self.element_is_present(self.locators.MOBILE_INPUT).send_keys(mobile)
        gender = self.choose_gender()
        return first_name, last_name, mobile, gender

    # methods to randomly fill NOT required fields
    def fill_date_of_birth(self):
        # click on input field to open the calendar
        self.element_is_visible(self.locators.DATE_OF_BIRTH_INPUT).click()
        # choose random month
        select_months = self.element_is_present(self.locators.SELECT_MONTH)
        list_of_months = [i for i in select_months.text.split()]
        select_months.click()
        selected_month = random.choice(list_of_months)
        month = selected_month[:3]
        self.element_is_visible((By.XPATH, f"//option[text()='{selected_month}']")).click()
        # select random year
        select_year = self.element_is_visible(self.locators.SELECT_YEAR)
        list_of_years = [int(i) for i in select_year.text.split()]
        selected_year = random.choice(list_of_years)
        year = selected_year
        self.element_is_clickable((By.CSS_SELECTOR, f'option[value="{selected_year}"]')).click()
        # select week
        select_day = self.driver.find_elements(*self.locators.SELECT_DAY)
        selected_day = random.choice(select_day)
        day = selected_day.text
        selected_day.click()
        return f'{day} {month} {year}'

    def choose_subjects(self, number_of_subjects):
        if number_of_subjects > 10:
            raise Exception('Maximum number of subjects can be added is 10')
        alphabet = [chr(ord('a') + i) for i in range(26)]
        selected_subjects = []
        while len(selected_subjects) < number_of_subjects:
            self.element_is_visible(self.locators.SUBJECTS_INPUT).send_keys(random.choice(alphabet))
            try:
                subjects_list = self.element_is_present(self.locators.SUBJECTS_LIST, 1)
                subjects_options = subjects_list.text.split('\n')
            except StaleElementReferenceException:
                self.select_text(self.locators.SUBJECTS_INPUT)
                continue
            except TimeoutException:
                self.select_text(self.locators.SUBJECTS_INPUT)
                continue
            else:
                if subjects_options[0] == 'Loading...':
                    self.select_text(self.locators.SUBJECTS_INPUT)
                    continue
            subject = random.choice(subjects_options)
            selected_subjects.append(subject)
            self.select_text(self.locators.SUBJECTS_INPUT)
            self.element_is_visible(self.locators.SUBJECTS_INPUT).send_keys(subject)
            self.element_is_clickable(self.locators.SUBJECTS_INPUT).send_keys(Keys.RETURN)
        return selected_subjects

    def fill_random_unrequired_fields(self):
        person = next(generated_person())
        email = person.email

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
