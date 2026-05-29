import time
import pytest
import random
from selenium.common import TimeoutException
from locators.elements_page_locators import LinksPageLocators, RadioButtonPageLocators
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver)
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the full name doesn't match"
            assert email == output_email, "the email doesn't match"
            assert current_address == output_cur_addr, "the current address doesn't match"
            assert permanent_address == output_per_addr, "the permanent address doesn't match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver)
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            assert input_checkbox == output_checkbox, 'checkboxes have not been selected'

    class TestRadioButton:

        # list of 'Yes', 'Impressive' and 'No' radio buttons
        radio_buttons_locators = RadioButtonPageLocators.BUTTONS

        @pytest.mark.parametrize('locator', radio_buttons_locators)
        def test_radio_button(self, driver, locator):
            radio_button_page = RadioButtonPage(driver)
            # list of unclickable buttons
            locators_expected_to_fail = [RadioButtonPageLocators.EXPECTED_TO_FAIL]
            try:
                selected = radio_button_page.click_on_the_radio_button(locator)
                output = radio_button_page.get_output_result()
                assert output == selected, f"{selected} has not been selected"
            except TimeoutException:
                if locator in locators_expected_to_fail:
                    pytest.xfail('This button is unclickable yet')

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver)
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person == table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver)
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "The person was not found in a table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver)
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person's card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver)
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person_info()
            assert web_table_page.check_deleted_person(), "Table is not empty"

        @pytest.mark.xfail(reason="Not all row numbers available")
        def test_web_page_change_count_rows(self, driver):
            web_table_page = WebTablePage(driver)
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], \
                'The number of rows in the table has not been changed or has changed incorrectly'

    class TestButtonsPage:
        def test_double_click_button(self, driver):
            buttons_page = ButtonsPage(driver)
            click_button = buttons_page.double_click_button()
            clicked_message = buttons_page.get_clicked_buttons()
            assert click_button == clicked_message, "You have not done a double click"

        def test_right_click_button(self, driver):
            buttons_page = ButtonsPage(driver)
            click_button = buttons_page.right_click_button()
            clicked_message = buttons_page.get_clicked_buttons()
            assert click_button == clicked_message, "You have done a right click"

        def test_dynamic_button(self, driver):
            buttons_page = ButtonsPage(driver)
            click_button = buttons_page.dynamic_click_button()
            clicked_message = buttons_page.get_clicked_buttons()
            assert click_button == clicked_message, "You have done a dynamic click"

    class TestLinksPage:

        # List of locators expected to fail due to links not provided
        expected_fail_locators = LinksPageLocators.EXPECTED_FAIL_LOCATORS

        # List of all LinksPage locators for parametrize
        @pytest.mark.parametrize('locator',
                                 [attr for attr in vars(LinksPageLocators).values() if isinstance(attr, tuple)])
        def test_link(self, driver, locator):
            links_page = LinksPage(driver)
            # try/except implemented to handle tests expected to fail due to not provided links
            try:
                link_href, current_url, status_code = links_page.try_follow_the_link(locator)
                assert link_href == current_url and status_code == 200, \
                    f"This URL {link_href} is redirecting to {current_url} URL. Status code = {status_code}"
            except AssertionError as e:
                if locator in self.expected_fail_locators:
                    pytest.xfail(f"No valid href link is provided yet")
                else:
                    raise e

    class TestUploadAndDownloadPage:

        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver)
            # file_name = file name on a local machine, result = uploaded file name appeared on browser
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, 'The file has not been uploaded'

        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver)
            # check = True if file was created
            check = upload_download_page.download_file()
            assert check is True, 'The file has not been downloaded'


    class TestDynamicPropertiesPage:

        def test_text_with_random_id(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver)
            text = dynamic_properties_page.get_text()
            assert text == "This text has random Id", 'Text is not as expected'

        def test_will_enable_5_seconds_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver)
            #  checking if button is enabled
            before = dynamic_properties_page.check_will_enable_5_seconds_button_clickability()
            # 5 secs explicit wait
            time.sleep(5)
            #  checking if button is enabled
            after = dynamic_properties_page.check_will_enable_5_seconds_button_clickability()
            assert not before, 'Button has been enabled too early'
            assert after, 'Button is not enabled yet'

        def test_change_color_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver)
            # checks current color, no waits
            color_before = dynamic_properties_page.check_color_change_button_color()
            time.sleep(5)
            # checks current color, no waits
            color_after = dynamic_properties_page.check_color_change_button_color()
            assert color_before != color_after, 'Color did not changed'

        def test_visible_after_5_seconds_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver)
            # checking if button is enabled
            before = dynamic_properties_page.check_visible_after_5_seconds_button()
            # 5 sec explicit wait
            time.sleep(5)
            # checking if button is enabled
            after = dynamic_properties_page.check_visible_after_5_seconds_button()
            assert not before, 'Button has been enabled too early'
            assert after, 'Button is not enabled yet'
