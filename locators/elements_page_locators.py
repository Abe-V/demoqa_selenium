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
    TREE_NODES = (By.CSS_SELECTOR, ".rc-tree-treenode")
    TREE_TITLE = (By.CSS_SELECTOR, ".rc-tree-title")
    TREE_CHECKBOX = (By.CSS_SELECTOR, ".rc-tree-checkbox")
    CLOSED_SWITCHER = (By.CSS_SELECTOR, ".rc-tree-switcher_close")
    RESULT = (By.CSS_SELECTOR, "#result")
    RESULT_ITEMS = (By.CSS_SELECTOR, "#result .text-success")
    TREE_NODE_BY_TITLE = (
        By.XPATH,
        "//span[@class='rc-tree-title' and normalize-space()='{title}']/ancestor::div[contains(@class,'rc-tree-treenode')]",
    )


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[for='noRadio']")
    # list of all button's locators
    BUTTONS = [YES_RADIOBUTTON, IMPRESSIVE_RADIOBUTTON, NO_RADIOBUTTON]
    # list of locators expected to fail
    EXPECTED_TO_FAIL = [NO_RADIOBUTTON]
    # displayed clicked button name
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
    TABLE_ROWS = (By.CSS_SELECTOR, "div.web-tables-wrapper table tbody tr")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = (By.XPATH, ".//ancestor::tr")
    NO_ROWS_FOUND = (By.XPATH, "//*[contains(text(), 'No rows found')]")
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
    # Buttons
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    DYNAMIC_CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    # Messages, appeared after respective button was clicked as per instruction
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    DYNAMIC_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")
    # List of all buttons clicked messages
    ALL_CLICKED_BUTTONS_MESSAGE = (By.CSS_SELECTOR, "p[id]")


class LinksPageLocators:
    # path to interactive links presented on a page
    HOME_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    HOME_DYNAMIC_LINK = (By.CSS_SELECTOR, "a[id='dynamicLink']")
    CREATED_LINK = (By.CSS_SELECTOR, "a[id='created']")
    NO_CONTENT_LINK = (By.CSS_SELECTOR, "a[id='no-content']")
    MOVED_LINK = (By.CSS_SELECTOR, "a[id='moved']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, "a[id='unauthorized']")
    FORBIDDEN_LINK = (By.CSS_SELECTOR, "a[id='forbidden']")
    NOT_FOUND_LINK = (By.CSS_SELECTOR, "a[id='invalid-url']")
    # list of locators expected to fail due to invalid href link
    EXPECTED_FAIL_LOCATORS = [
                                CREATED_LINK,
                                NO_CONTENT_LINK,
                                MOVED_LINK,
                                BAD_REQUEST,
                                UNAUTHORIZED_LINK,
                                FORBIDDEN_LINK,
                                NOT_FOUND_LINK
                             ]


class UploadAndDownloadPageLocators:
    # choose file button path
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    # fake path appeared in browser - C:\fakepath\filename.ext
    UPLOADED_FILE = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
    # download button path
    DOWNLOAD_FILE =(By.CSS_SELECTOR, 'a[id="downloadButton"]')


class DynamicPropertiesPageLocators:
    # simple text path
    TEXT_WITH_RANDOM_ID = (By.XPATH, "//p[contains(text(), 'This text has random Id')]")
    # "Will enable 5 seconds" button
    WILL_ENABLE_5_SECONDS_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
    # 'Color change' button
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    # "Visible after 5 seconds" button
    VISIBLE_AFTER_5_SECONDS_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')
