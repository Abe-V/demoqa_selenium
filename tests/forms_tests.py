import time
from pages.forms_page import PracticeFormPage


class TestPracticeFormPage:

    def test_submitting_of_form(self, driver):
        practice_form_page = PracticeFormPage(driver)
        practice_form_page.fill_fields_to_submit()
