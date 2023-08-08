import time
import pytest
import random
from locators.elements_page_locators import LinksPageLocators

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver)  # , 'https://demoqa.com/text-box')
            # text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the full name doesn't match"
            assert email == output_email, "the email doesn't match"
            assert current_address == output_cur_addr, "the current address doesn't match"
            assert permanent_address == output_per_addr, "the permanent address doesn't match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver)
            # check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            assert input_checkbox == output_checkbox, 'checkboxes have not been selected'

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver)  # , 'https://demoqa.com/radio-button')
            # radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impression = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' has not been selected"
            assert output_impression == 'Impressive', "'Impressive' has not been selected"
            assert output_no == 'No', "'No' has not been selected"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver)  # , 'https://demoqa.com/webtables')
            # web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver)  # , 'https://demoqa.com/webtables')
            # web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "The person was not found in a table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver)  # , 'https://demoqa.com/webtables')
            # web_table_page.open()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person's card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver)  # , 'https://demoqa.com/webtables')
            # web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person_info()
            text = web_table_page.check_deleted_person()
            assert text == "No rows found"

        def test_web_page_change_count_rows(self, driver):
            web_table_page = WebTablePage(driver)  # , 'https://demoqa.com/webtables')
            # web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], 'The number of rows in the table has not been changed or has ' \
                                                      'changed incorrectly'

    class TestButtonsPage:
        def test_double_click_button(self, driver):
            buttons_page = ButtonsPage(driver)  # , "https://demoqa.com/buttons")
            # buttons_page.open()
            click_button = buttons_page.double_click_button()
            clicked_message = buttons_page.get_clicked_buttons()
            assert click_button == clicked_message, "You have not done a double click"

        def test_right_click_button(self, driver):
            buttons_page = ButtonsPage(driver)  # , "https://demoqa.com/buttons")
            # buttons_page.open()
            click_button = buttons_page.right_click_button()
            clicked_message = buttons_page.get_clicked_buttons()
            assert click_button == clicked_message, "You have done a right click"

        def test_dynamic_button(self, driver):
            buttons_page = ButtonsPage(driver)  # , "https://demoqa.com/buttons")
            # buttons_page.open()
            click_button = buttons_page.dynamic_click_button()
            clicked_message = buttons_page.get_clicked_buttons()
            assert click_button == clicked_message, "You have done a dynamic click"

    class TestLinksPage:

        # List of locators expected to fail
        EXPECTED_FAIL_LOCATORS = [
            LinksPageLocators.CREATED_LINK,
            LinksPageLocators.NO_CONTENT_LINK,
            LinksPageLocators.MOVED_LINK,
            LinksPageLocators.BAD_REQUEST,
            LinksPageLocators.UNAUTHORIZED_LINK,
            LinksPageLocators.FORBIDDEN_LINK,
            LinksPageLocators.NOT_FOUND_LINK
        ]

        @pytest.mark.parametrize('locator',
                                 [attr for attr in vars(LinksPageLocators).values() if isinstance(attr, tuple)])
        def test_link(self, driver, locator):
            links_page = LinksPage(driver)
            try:
                link_href, current_url, status_code = links_page.try_follow_the_link(locator)
                assert link_href == current_url and status_code == 200, \
                    f"This URL {link_href} is redirecting to {current_url} URL. Status code = {status_code}"
            except Exception as e:
                if locator in self.EXPECTED_FAIL_LOCATORS:
                    pytest.xfail(f"No valid href link is provided yet")
                else:
                    raise e
