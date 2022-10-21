import logging
import time

import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from po.locators import locators


class BasePage:
    logging.basicConfig(filename="../logs.log", level=logging.INFO)

    def wait_sec(self):
        time.sleep(1)

    url = "http://localhost:3000/#/"

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = self.url if url is None else url
        self.open_page(self.url)

    def open_page(self, url=None):
        if not url:
            url = self.url
        self.driver.get(url)
        return self

    # todo add default time
    def get_element_by_xpath(self, xpath, time=4):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath)))

    def get_elements_by_xpath(self, xpath, time=4):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_all_elements_located((By.XPATH, xpath)))

    def click_on_element(self, element):
        self.get_element_by_xpath(element).click()

    def type_data(self, element, text):
        self.get_element_by_xpath(element).send_keys(text)

    @allure.step("Open login page")
    def open_login_form(self):
        self.click_on_element(locators.dismiss_button)
        self.click_on_element(locators.account_button)
        self.click_on_element(locators.login_button)
        return self

    @allure.step("Login")
    def login(self, email, password, element, time=4):
        self.type_data(locators.email_field, email)
        self.type_data(locators.password_field, password)
        self.click_on_element(locators.login_confirm_button)
        try:
            WebDriverWait(self.driver, time).until(
                expected_conditions.visibility_of_element_located((By.XPATH, element)))
        except NoSuchElementException:
            return print("NoSuchElementException, element isn't present on the page")
        return self

    def _get_text_from_element(self, element, time=4):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located((By.XPATH, element))).text

    def get_attribute_value(self, xpath, attribute_name):
        return self.get_element_by_xpath(xpath).get_attribute(attribute_name)

    @allure.step("Check if login successful")
    def check_if_login_successful(self):
        return self._get_text_from_element(locators.your_basket_button) == "Your Basket"

    @allure.step("Check if login failed")
    def check_if_login_failed(self):
        return self._get_text_from_element(locators.invalid_email_password_message, ) == "Invalid email or password."
