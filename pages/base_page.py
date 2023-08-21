from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_element(self, element):
        self.driver.execute_script("window.scrollBy(0,200);", element)

    def action_double_click(self, element):
        action = ActionChains(driver=self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(driver=self.driver)
        action.context_click(element)
        action.perform()

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def close_current_tab(self):
        self.driver.close()

    def switch_to_first_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def set_page_zoom(self, value):
        self.driver.execute_script(f"document.body.style.zoom = '{value}%'")

    def check_current_zoom(self):
        return int(float(self.driver.execute_script("return window.getComputedStyle(document.body, null).zoom"))*100)

    def select_text(self, locator):
        self.element_is_visible(locator).send_keys(Keys.COMMAND + 'a')
