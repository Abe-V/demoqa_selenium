from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_WINDOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, 'button[id="messageWindowButton"]')
    WINDOW_MESSAGE_TEXT = (By.CSS_SELECTOR, 'body')
