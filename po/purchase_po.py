import random

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from po.home_page_bo import HomePage
from po.locators import locators


class PurchasePage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def delete_item_from_basket(self):
        list_el = self.get_elements_by_xpath(locators.delete_item_buttons)
        self.press_delete(list_el[0])
        return self

    def move_and_js_click(self, element):
        ActionChains(self.driver).move_to_element(element).perform()
        self.cursed_click(element)

    def move_and_click(self, locator):
        element = self.get_element_by_xpath(locator)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def click_checkout_button(self):
        self.move_and_js_click(self.get_element_by_xpath(locators.checkoutButton))
        return self

    def click_add_new_address_button(self):
        self.move_and_js_click(self.get_element_by_xpath(locators.add_a_new_address_button))
        return self

    def check_if_select_address_page_opened(self):
        return "#/address/select" in self.driver.current_url

    def check_if_add_new_address_page_opened(self):
        return "#/address/create" in self.driver.current_url

    def _fill_form(self, input_for_text, text):
        el = self.get_element_by_xpath(input_for_text)
        ActionChains(self.driver).move_to_element(el).perform()
        # need to clean form before typing a new data
        el.clear()
        self.type_data(input_for_text, text)
        return self

    @allure.step("Fill a new address")
    def fill_address_form(self):
        self._fill_form(locators.country_form, "COUNTRY@@@@")
        self._fill_form(locators.name_form, "NAME@@@@")
        self._fill_form(locators.number_form, 12345678)
        self._fill_form(locators.zip_code_form, 123)
        self._fill_form(locators.address_form, "address@@@")
        self._fill_form(locators.city_form, "city@@@")
        self.cursed_click(self.get_element_by_xpath(locators.submit_button))
        return self

    @allure.step("Select delivery address")
    def select_delivery_address(self):
        self.cursed_click(self.get_element_by_xpath(locators.radio_button))
        self.cursed_click(self.get_element_by_xpath(locators.continue_button))
        return self

    def check_if_delivery_method_page_opened(self):
        return "#/delivery-method" in self.driver.current_url

    @allure.step("Select delivery speed")
    def select_delivery_speed(self):
        self.cursed_click(self.get_element_by_xpath(locators.one_day_delivery_radio_button))
        self.cursed_click(self.get_element_by_xpath(locators.proceed_to_delivery_method_selection_button))
        return self

    def expand_new_car_info(self):
        self.cursed_click(self.get_element_by_xpath(locators.expand_button))
        return self

    def _select_from_drop_down(self, element):
        self.get_element_by_xpath(element).click()

    def _select_month(self):
        self._select_from_drop_down(locators.select_month)
        return self

    def _select_year(self):
        self._select_from_drop_down(locators.select_year)
        return self

    @allure.step("Fill payment info")
    def fill_my_payment_options_information(self):
        self.expand_new_car_info() \
            ._fill_form(locators.card_holder_name_form, str(random.randint(100, 999))) \
            ._fill_form(locators.card_number_form, random.randint(1111111111111111, 9111111111111111)) \
            ._select_month() \
            ._select_year() \
            .move_and_js_click(self.get_element_by_xpath(locators.submit_payment_option_button))
        return self

    def check_if_my_payment_option_page_opened(self):
        return "#/payment/shop" in self.driver.current_url

    @allure.step("Choose card for the pay")
    def choose_card(self):
        WebDriverWait(self.driver, 4) \
            .until(expected_conditions
                   .text_to_be_present_in_element_attribute
                   ((By.XPATH, locators.submit_payment_option_button), "disabled", "true"))
        self.move_and_click(locators.card_for_pay)
        self.move_and_js_click(self.get_element_by_xpath(locators.submit_info_button))
        return self

    def check_if_order_summary_page_opened(self):
        return "#/order-summary" in self.driver.current_url

    @allure.step("Confirm purchase")
    def pay(self):
        self.move_and_js_click(self.get_element_by_xpath(locators.place_your_order_and_pay_button))

    def check_if_purchase_complete(self):
        return self.get_element_by_xpath("//*[text()='Thank you for your purchase!']") \
                   .text == "Thank you for your purchase!"
