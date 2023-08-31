from pages.alerts_frame_wondows_page import BrowserWindowsPage


class TestBrowserWindow:
    sample_page_url = 'https://demoqa.com/sample'

    def test_new_tab_button(self, driver):
        browser_window_page = BrowserWindowsPage(driver)
        browser_window_page.check_new_tab_button()
        url = browser_window_page.get_current_url()
        assert url == self.sample_page_url, 'New tab has not been opened'

    def test_new_window_button(self, driver):
        browser_window_page = BrowserWindowsPage(driver)
        browser_window_page.check_new_window_button()
        url = browser_window_page.get_current_url()
        assert url == self.sample_page_url, 'New window has not been opened'

    def test_new_window_message_button(self, driver):
        browser_window_page = BrowserWindowsPage(driver)
        windows = browser_window_page.check_new_window_message_button()
        assert len(windows) == 2, 'Alert window has not been opened'
