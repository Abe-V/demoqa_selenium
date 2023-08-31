from pages.forms_page import PracticeFormPage


class TestPracticeFormPage:

    def test_submitting_of_form(self, driver):
        practice_form_page = PracticeFormPage(driver)
        input_data = practice_form_page.fill_the_form_randomly()
        practice_form_page.click_submit()
        output_data = practice_form_page.check_the_form()
        assert input_data == output_data, 'There is discrepancy between input and output data'
