from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    # CLOSE_BANNER = (By.CSS_SELECTOR, "#close-fixedban > img")
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULTS = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADOIBUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADOIBUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADOIBUTTON = (By.CSS_SELECTOR, "label[for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablePageLocators:
    # add person info
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    # SELECT_5_ROWS = (By.CSS_SELECTOR, "option[value='5']")
    # SELECT_10_ROWS = (By.CSS_SELECTOR, "option[value='10']")
    # SELECT_20_ROWS = (By.CSS_SELECTOR, "option[value='20']")
    # SELECT_25_ROWS = (By.CSS_SELECTOR, "option[value='25']")
    # SELECT_50_ROWS = (By.CSS_SELECTOR, "option[value='50']")
    # SELECT_100_ROWS = (By.CSS_SELECTOR, "option[value='100']")

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    DYNAMIC_CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    DYNAMIC_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")
    ALL_CLICKED_BUTTONS_MESSAGE = (By.CSS_SELECTOR, "p[id]")


class LinksPageLocators:
    HOME_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    HOME_DYNAMIC_LINK = (By.CSS_SELECTOR, "a[id='dynamicLink']")
    CREATED_LINK = (By.CSS_SELECTOR, "a[id='created']")
    NO_CONTENT_LINK = (By.CSS_SELECTOR, "a[id='no-content']")
    MOVED_LINK = (By.CSS_SELECTOR, "a[id='moved']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, "a[id='unauthorized']")
    FORBIDDEN_LINK = (By.CSS_SELECTOR, "a[id='forbidden']")
    NOT_FOUND_LINK = (By.CSS_SELECTOR, "a[id='invalid-url']")
