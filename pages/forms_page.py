# common imports
import os
import random
from datetime import datetime
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# my directories imports
import locators.forms_page_locators
from generator.generator import generated_person,generate_jpeg
from pages.base_page import BasePage
from URLs.urls import FormsPagesUrls as url


# For each page-class - respective URL will be assigned as a 'url' argument for BasePage,
# and page with respective URL will be opened
class PracticeFormPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=url.practice_form_url)
        self.open()

    locators = locators.forms_page_locators.PracticeFormPageLocators

    # gender is a required field. choose_gender() chooses random gender if not specified
    def choose_gender(self, gender=None):
        genders = {
            'male': self.locators.MALE_RADIO_BUTTON,
            'female': self.locators.FEMALE_RADIO_BUTTON,
            'other': self.locators.OTHER_GENDER_RADIO_BUTTON
        }
        if gender is None:
            button = self.element_is_visible(random.choice(list(genders.values())))
        elif gender.lower() in genders.keys():
            button = self.element_is_visible(genders[gender])
        else:
            raise ValueError("Only 'Male', 'Female' or 'Other' is allowed as an argument")
        button.click()
        return button.text

    # randomly fills all required fields
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

    # method randomly fills 'Date of Birth' field, if not specified
    # birthday can be provided in '01 Jan 2000' or '01 January 2000' format
    def fill_date_of_birth(self, date_of_birth=None):
        # click on input field to open the calendar
        birthday_input = self.element_is_visible(self.locators.DATE_OF_BIRTH_INPUT)
        birthday_input.click()
        if date_of_birth is None:
            # select random year
            select_year = self.element_is_visible(self.locators.SELECT_YEAR)
            list_of_years = [int(i) for i in select_year.text.split()]
            year = random.choice(list_of_years)
            self.element_is_clickable((By.CSS_SELECTOR, f'option[value="{year}"]')).click()
            # select random month
            select_months = self.element_is_present(self.locators.SELECT_MONTH)
            list_of_months = [i for i in select_months.text.split()]
            select_months.click()
            month = random.choice(list_of_months)
            self.element_is_visible((By.XPATH, f"//option[text()='{month}']")).click()
            # select random day
            select_day = self.driver.find_elements(*self.locators.SELECT_DAY)
            selected_day = random.choice(select_day)
            day = selected_day.text
            selected_day.click()
        else:
            # if birthday is provided as an argument, validate date format
            try:
                datetime.strptime(date_of_birth, "%d %b %Y")
            except ValueError:
                try:
                    datetime.strptime(date_of_birth, "%d %B %Y")
                except ValueError:
                    raise ValueError("Invalid date format. Please use '00 Mon 0000' format."
                                     "(e.g. '01 Jan 2000' or '01 January 2000')")
            self.select_text(self.locators.DATE_OF_BIRTH_INPUT)
            birthday_input.send_keys(date_of_birth)
            day, month, year = (i for i in date_of_birth.split())
        return f'{day} {month[:3]} {year}'

    # method to choose random number of subjects, if not specified
    def choose_subjects(self, number_of_subjects=None):
        # maximum number of subjects can be added on a site is 10
        if number_of_subjects > 10:
            raise Exception('Maximum number of subjects can be added is 10')
        if number_of_subjects is None:
            number_of_subjects = random.randint(10)
        # create alphabet
        alphabet = [chr(ord('a') + i) for i in range(26)]
        selected_subjects = []
        # unless desired number of subjects reached
        while len(selected_subjects) < number_of_subjects:
            # type random letter
            self.element_is_visible(self.locators.SUBJECTS_INPUT).send_keys(random.choice(alphabet))
            # and see if list of subjects containing this letter drop down
            try:
                subjects_list = self.element_is_present(self.locators.SUBJECTS_LIST, 1)
                # if there is a list, assign it to 'subjects_options'
                subjects_options = subjects_list.text.split('\n')
                # if there is no list of subjects available,
            except StaleElementReferenceException:
                # then select inputted letter,(so new letter input will overwrite existing),
                self.select_text(self.locators.SUBJECTS_INPUT)
                # and start loop over
                continue
                # NOTE: deleting all subjects and letters from this field leads to displaying fully empty (blank) page
            except TimeoutException:
                self.select_text(self.locators.SUBJECTS_INPUT)
                continue
            else:
                # if there is no subjects containing typed in letter,
                # a dropdown menu saying 'Loading...' appears for really short period of time (milliseconds)
                if 'Loading...' in subjects_options:
                    self.select_text(self.locators.SUBJECTS_INPUT)
                    continue
            # choose random subject from dropdown list
            subject = random.choice(subjects_options)
            selected_subjects.append(subject)
            # select all text in the field, so new text will fully overwrite existing text
            self.select_text(self.locators.SUBJECTS_INPUT)
            # enter full random subject name in the field
            self.element_is_visible(self.locators.SUBJECTS_INPUT).send_keys(subject)
            # and press ENTER
            self.element_is_clickable(self.locators.SUBJECTS_INPUT).send_keys(Keys.RETURN)
        return selected_subjects

    # check random hobbies by default, if not specified
    def choose_hobbies(self, *choose):
        checked = []
        hobbies = {
            'Sports':
                {'locator': self.locators.SPORTS_CHECKBOX, 'checked': None},
            'Reading':
                {'locator': self.locators.READING_CHECKBOX, 'checked': None},
            'Music':
                {'locator': self.locators.MUSIC_CHECKBOX, 'checked': None}
        }
        # if no arguments were received, create list of random values between (0, 1) for each hobby
        if not choose:
            for n, hobby in enumerate(hobbies):
                hobbies[hobby]['checked'] = random.randint(0, 1)
        # if checkboxes were chosen and received as a parameters
        else:
            # iterate over received parameters, capitalizing each
            for choice in choose:
                choice = choice.capitalize()
                # if spelling is correct, define 'checked' value as 1
                if choice in hobbies:
                    hobbies[choice]['checked'] = 1
                # if its misspelling, raise Error, printing available checkboxes
                else:
                    raise ValueError(f"Only {tuple(hobbies.keys())} checkboxes can be checked")
        # click every checkbox that has 'checked' value equal 1
        for hobby in hobbies:
            if hobbies[hobby]['checked']:
                self.element_is_clickable(hobbies[hobby]['locator']).click()
                checked.append(hobby)
        return checked

    def upload_jpeg_file(self):
        # generating file on a local machine
        path = generate_jpeg()
        self.element_is_visible(self.locators.CHOOSE_FILE_BUTTON).send_keys(path)
        # delete file from a local machine
        os.remove(path)
        # get path of uploaded file ('C:\fakepath\{real_file_name.ext})
        uploaded = self.element_is_visible(self.locators.CHOOSE_FILE_BUTTON).get_attribute('value')
        return path.split('/')[-1], uploaded.split("\\")[-1]

    def fill_address(self):
        person = next(generated_person())
        address = person.current_address
        # self.scroll_all_the_way_down()
        self.element_is_visible(self.locators.CURRENT_ADDRESS_INPUT).send_keys(address)
        return address

    # code below not ready yet
    def select_state_and_city(self):
        self.set_page_zoom(50)
        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))
        self.element_is_clickable(self.locators.SELECT_STATE).click()
        list_of_states = self.element_is_visible(self.locators.LIST_OF_STATES).text
        return list_of_states

    def fill_random_unrequired_fields(self):
        pass

    def fill_fields_to_submit(self):
        pass

    def click_submit(self):
        pass

    def check_the_form(self):
        pass
