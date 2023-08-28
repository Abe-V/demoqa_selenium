# common imports
import os
import random
from datetime import datetime
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# my directories imports
import locators.forms_page_locators
from generator.generator import generated_person, generate_jpeg_file
from pages.base_page import BasePage
from URLs.urls import FormsPagesUrls as url


# For each page-class - respective URL will be assigned as a 'url' argument for BasePage,
# and page with respective URL will be opened, and ad and footer will be removed

class PracticeFormPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=url.practice_form_url)
        self.open()
        self.remove_ad_banner()
        self.remove_footer()

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
        return f'{first_name} {last_name}', gender, mobile

    # NOT required fields

    # method randomly fills 'Email' field, if not specified
    def fill_email(self, email=None, flag=1):
        if not flag:
            return ''
        if email is not None:
            return email
        person = next(generated_person())
        email = person.email
        self.element_is_clickable(self.locators.EMAIL_INPUT).send_keys(email)
        return email

    # method randomly fills 'Date of Birth' field, if not specified
    # birthday can be provided in '01 Jan 2000' or '01 January 2000' format
    def fill_date_of_birth(self, date_of_birth=None, flag=1):
        if not flag:
            date_value = self.element_is_present(self.locators.DATE_OF_BIRTH_INPUT).get_attribute('value')
            date_output = datetime.strptime(date_value, "%d %b %Y").strftime("%d %B %Y")
            day, month, year = (i for i in date_output.split())
            return f'{day} {month},{year}'
        # click on input field to open the calendar
        birthday_input = self.element_is_visible(self.locators.DATE_OF_BIRTH_INPUT)
        birthday_input.click()
        if date_of_birth is None:
            # select random year
            select_year = self.element_is_visible(self.locators.SELECT_YEAR)
            list_of_years = [int(i) for i in select_year.text.split()]
            select_year.click()
            self.element_is_clickable((By.CSS_SELECTOR, f'option[value="{random.choice(list_of_years)}"]')).click()
            # select random month
            select_months = self.element_is_present(self.locators.SELECT_MONTH)
            list_of_months = [i for i in select_months.text.split()]
            select_months.click()
            self.element_is_visible((By.XPATH, f"//option[text()='{random.choice(list_of_months)}']")).click()
            # select random day
            select_day = self.driver.find_elements(*self.locators.SELECT_DAY)
            selected_day = random.choice(select_day)
            selected_day.click()
            date_value = self.element_is_present(self.locators.DATE_OF_BIRTH_INPUT).get_attribute('value')
            date_of_birth = datetime.strptime(date_value, "%d %b %Y").strftime("%d %B %Y")
        else:
            # if birthday is provided as an argument, validate date format
            try:
                datetime.strptime(date_of_birth, "%d %B %Y")
            except ValueError:
                raise ValueError("Invalid date format. Please use '01 January 2000' format.")
            self.select_text(self.locators.DATE_OF_BIRTH_INPUT)
            birthday_input.send_keys(date_of_birth)
        day, month, year = (i for i in date_of_birth.split())
        return f'{day} {month},{year}'

    # method to choose random number of subjects, if not specified
    def choose_subjects(self, number_of_subjects=None, flag=1):
        if not flag:
            return ''
        # maximum number of subjects can be added on a site is 10
        if number_of_subjects is None:
            number_of_subjects = random.randint(1, 10)
        elif number_of_subjects > 10:
            raise Exception('Maximum number of subjects can be added is 10')
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
        return ', '.join(selected_subjects).strip()

    # check random hobbies by default, if not specified
    def choose_hobbies(self, *choose, flag=1):
        if not flag:
            return ''
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
        if not checked:
            return ''
        return ', '.join(checked).strip()

    def upload_jpeg_file(self, flag=1):
        if not flag:
            return ''
        # generating file on a local machine
        path = generate_jpeg_file()
        self.element_is_visible(self.locators.CHOOSE_FILE_BUTTON).send_keys(path)
        # delete file from a local machine
        os.remove(path)
        # get path of uploaded file ('C:\fakepath\{real_file_name.ext})
        uploaded = self.element_is_visible(self.locators.CHOOSE_FILE_BUTTON).get_attribute('value')
        return uploaded.split("\\")[-1]

    def fill_address(self, flag=1):
        if not flag:
            return ''
        person = next(generated_person())
        address = person.current_address
        self.element_is_visible(self.locators.CURRENT_ADDRESS_INPUT).send_keys(address)
        return address

    # select random State if not specified
    def select_state(self, state=None, flag=1):
        if not flag:
            return ''
        # scroll all the way down
        self.scroll_all_the_way_down()
        # click 'Select State' field
        self.element_is_clickable(self.locators.SELECT_STATE).click()
        num_of_elements = 0
        list_of_states = []
        # iterate over every state in a dropdown list and add it to list_of_states
        while True:
            try:
                element = self.element_is_present((By.CSS_SELECTOR, f'div[id="react-select-3-option-{num_of_elements}"]'), 1)
                list_of_states.append(element.text)
                num_of_elements += 1
            except TimeoutException:
                break
        # select random state and press 'ENTER'
        if state is None:
            selected_state = random.choice(list_of_states)
        else:
            selected_state = state
        # validate argument
        try:
            self.element_is_visible(self.locators.STATE_INPUT).send_keys(selected_state)
        except TypeError:
            print(f'Only next states available for choice: {list_of_states}')
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        return selected_state

    # select random State if not specified
    def select_city(self, city=None, flag=1):
        if not flag:
            return ''
        # click 'Select City' field
        self.element_is_clickable(self.locators.SELECT_CITY).click()
        self.scroll_all_the_way_down()
        num_of_elements = 0
        list_of_cities = []
        # iterate over every city in a dropdown list and add it to list_of_cities
        while True:
            try:
                element = self.element_is_present((By.CSS_SELECTOR, f'div[id="react-select-4-option-{num_of_elements}"]'), 1)
                list_of_cities.append(element.text)
                num_of_elements += 1
            except TimeoutException:
                # print(f'{num_of_elements} cities are presented')
                break
        # select random city
        if city is None:
            selected_city = random.choice(list_of_cities)
        # or specified city
        elif city in list_of_cities:
            selected_city = city
        # if specified city is not in a list of cities - raise error
        else:
            raise TypeError(f'Only next cities available for choice: {list_of_cities}')
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(selected_city)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        return selected_city

    def select_state_and_city(self, state=None, city=None, flag1=1, flag2=1):
        if not flag1:
            return ''
        state = self.select_state(state)
        if not flag2:
            return ''
        city = self.select_city(city, flag2)
        return f'{state} {city}'

    def fill_random_unrequired_fields(self):
        flag = random.randint
        email = self.fill_email(flag=flag(0, 1))
        date_of_birth = self.fill_date_of_birth(flag=flag(0, 1))
        subjects = self.choose_subjects(flag=flag(0, 1))
        hobbies = self.choose_hobbies(flag=flag(0, 1))
        jpeg_file = self.upload_jpeg_file(flag=flag(0, 1))
        address = self.fill_address(flag=flag(0, 1))
        state_and_city = self.select_state_and_city(flag1=flag(0, 1), flag2=flag(0, 1))
        return email, date_of_birth, subjects, hobbies, jpeg_file, address, state_and_city

    def fill_the_form_randomly(self):
        full_name, gender, mobile = self.fill_required_fields()
        email, date_of_birth, subjects, hobbies, picture, address, state_and_city = \
            self.fill_random_unrequired_fields()
        return [full_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture, address, state_and_city]

    def click_submit(self):
        self.scroll_all_the_way_down()
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()

    def check_the_form(self):
        all_fields_locators = self.locators.SUBMITTED_FORM_LABELS
        all_outputs = []
        for label in all_fields_locators:
            locator = (By.XPATH, f'{label[1]}/following-sibling::*')
            value = self.element_is_visible(locator).text
            all_outputs.append(value)
        return all_outputs
