from selenium.webdriver.common.by import By


class PracticeFormPageLocators:

    # Required fields

    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    MOBILE_INPUT = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    # Required to choose one of gender options
    MALE_RADIO_BUTTON = (By.CSS_SELECTOR, 'div[id="genterWrapper"] div div:nth-child(1)')
    FEMALE_RADIO_BUTTON = (By.CSS_SELECTOR, 'div[id="genterWrapper"] div div:nth-child(2)')
    OTHER_GENDER_RADIO_BUTTON = (By.CSS_SELECTOR, 'div[id="genterWrapper"] div div:nth-child(2)')

    # NOT required fields

    # Email
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    # Birthday calendar
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    # SELECT_DAY contains a list of up to 42 elements, 7 days for 6 weeks, including
    # (28-31 days of current month plus up to 12 of days of previous and next month on first and last week)
    SELECT_DAY = (By.CSS_SELECTOR, 'div[class="react-datepicker__week"] div')
    SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')

    # Subjects
    SUBJECTS_INPUT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    SUBJECTS_LIST = (By.CSS_SELECTOR, 'div[class*="subjects-auto-complete__menu-list"]')

    # Hobbies
    SPORTS_CHECKBOX = (By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]')
    SPORTS_CHECKBOX_INPUT = (By.CSS_SELECTOR, 'input[id="hobbies-checkbox-1"]')
    READING_CHECKBOX = (By.CSS_SELECTOR, 'label[for="hobbies-checkbox-2"]')
    READING_CHECKBOX_INPUT = (By.CSS_SELECTOR, 'input[id="hobbies-checkbox-2"]')
    MUSIC_CHECKBOX = (By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]')
    MUSIC_CHECKBOX_INPUT = (By.CSS_SELECTOR, 'input[id="hobbies-checkbox-3"]')

    # Picture
    CHOOSE_FILE_BUTTON = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')

    # Current address
    CURRENT_ADDRESS_INPUT = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')

    # State and City
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')

    # Submit
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    # Footer
    FOOTER = (By.CSS_SELECTOR, 'footer')

    # Student submitted form (locators for all the labels, to find the value, add '/following-sibling::*')
    STUDENT_NAME_LABEL = (By.XPATH, "//td[text()='Student Name']")
    STUDENT_EMAIL_LABEL = (By.XPATH, "//*[text()='Student Email']")
    GENDER_LABEL = (By.XPATH, "//tr/*[text()='Gender']")
    MOBILE_LABEL = (By.XPATH, "//tr/*[text()='Mobile']")
    DATE_OF_BIRTH_LABEL = (By.XPATH, "//tr/*[text()='Date of Birth']")
    SUBJECTS_LABEL = (By.XPATH, "//tr/*[text()='Subjects']")
    HOBBIES_LABEL = (By.XPATH, "//tr/*[text()='Hobbies']")
    PICTURE_LABEL = (By.XPATH, "//tr/*[text()='Picture']")
    ADDRESS_LABEL = (By.XPATH, "//tr/*[text()='Address']")
    STATE_AND_CITY_LABEL = (By.XPATH, "//tr/*[text()='State and City']")
    # list of locators for all the labels
    SUBMITTED_FORM_LABELS = [STUDENT_NAME_LABEL, STUDENT_EMAIL_LABEL, GENDER_LABEL, MOBILE_LABEL, DATE_OF_BIRTH_LABEL,
                             SUBJECTS_LABEL, HOBBIES_LABEL, PICTURE_LABEL, ADDRESS_LABEL, STATE_AND_CITY_LABEL]
