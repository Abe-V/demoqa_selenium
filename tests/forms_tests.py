import time
from pages.forms_page import PracticeFormPage


class TestPracticeFormPage:

    def test_submitting_of_form(self, driver):
        practice_form_page = PracticeFormPage(driver)
        x = practice_form_page.click_choose_all_hobbies()
        print(x)
