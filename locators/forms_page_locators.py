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
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    # SELECT_DAY contains a list of up to 42 elements, 7 days for 6 weeks, including
    # (28-31 days of current month plus up to 12 of days of previous and next month on first and last week)
    SELECT_DAY = (By.CSS_SELECTOR, 'div[class="react-datepicker__week"] div')
    SUBJECTS_INPUT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    SUBJECTS_LIST = (By.CSS_SELECTOR, 'div[class*="subjects-auto-complete__menu-list"]')
    SPORTS_CHECKBOX = (By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]')
    SPORTS_CHECKBOX_INPUT = (By.CSS_SELECTOR, 'input[id="hobbies-checkbox-1"]')
    READING_CHECKBOX = (By.CSS_SELECTOR, 'label[for="hobbies-checkbox-2"]')
    READING_CHECKBOX_INPUT = (By.CSS_SELECTOR, 'input[id="hobbies-checkbox-2"]')
    MUSIC_CHECKBOX = (By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]')
    MUSIC_CHECKBOX_INPUT = (By.CSS_SELECTOR, 'input[id="hobbies-checkbox-3"]')
    CHOOSE_FILE_BUTTON = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS_INPUT = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    SELECT_STATE = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    # LIST_OF_STATES is dynamic element and has same locator as LIST_OF_CITIES
    # since only one of them can appear at a time
    LIST_OF_STATES = (By.CSS_SELECTOR, 'div[id="state"]>div:nth-child(2)>div')
    SELECT_CITY = (By.XPATH, '//div[text()="Select City"]')
    LIST_OF_CITIES = (By.CSS_SELECTOR, 'div[class$="-menu"] div')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')
