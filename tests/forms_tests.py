import time
from pages.forms_page import PracticeFormPage


class TestPracticeFormPage:

    def test_submitting_of_form(self, driver):
        for _ in range(10):
            practice_form_page = PracticeFormPage(driver)
            input_data = practice_form_page.fill_the_form()
            # bd = practice_form_page
            practice_form_page.click_submit()
            output_data = practice_form_page.check_the_form()
            # time.sleep(2)
            print('\n')
            print(input_data)
            print(output_data)
