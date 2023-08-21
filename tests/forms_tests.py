import time
from pages.forms_page import PracticeFormPage


class TestPracticeFormPage:

    def test_submitting_of_form(self, driver):
        for i in range(20):
            practice_form_page = PracticeFormPage(driver)
            x = practice_form_page.choose_subjects(10)
