from selenium.webdriver.common.alert import Alert
from locators.alerts_frame_windows_page_locators import *
from pages.base_page import BasePage
from URLs.urls import AlertsFrameWindowsUrls


class BrowserWindowsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url=AlertsFrameWindowsUrls.browser_windows_url)
        self.open()

    locators = BrowserWindowsPageLocators

    def check_new_tab_button(self):
        self.element_is_clickable(self.locators.NEW_TAB_BUTTON).click()
        self.switch_to_new_tab()
        self.switch_to_new_tab()
        return self.get_current_url()

    def check_new_window_button(self):
        self.element_is_clickable(self.locators.NEW_WINDOW_BUTTON).click()
        self.switch_to_new_tab()
        self.switch_to_new_tab()
        return self.get_current_url()

    def check_new_window_message_button(self):
        self.element_is_clickable(self.locators.NEW_WINDOW_MESSAGE_BUTTON).click()
        return len(self.driver.window_handles)
