import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from po.locators import locators


class BasePage:
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

    def get_element_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 4).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))

    def get_elements_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_all_elements_located((By.XPATH, xpath)))

    def click_on_element(self, element):
        self.get_element_by_xpath(element).click()

    def type_data(self, element, text):
        self.get_element_by_xpath(element).send_keys(text)

    def open_login_form(self):
        self.click_on_element(locators.dismiss_button)
        self.click_on_element(locators.account_button)
        self.click_on_element(locators.login_button)
        return self

    def fill_confirm_login_form(self, email, password):
        self.type_data(locators.email_field, email)
        self.type_data(locators.password_field, password)
        self.click_on_element(locators.login_confirm_button)
        return self

    def is_text_present(self, element):
        try:
            return self.get_element_by_xpath(element).text
        except NoSuchElementException:
            return False

    # fix assert

    def check_if_login_successful(self):
        assert self.is_text_present(locators.your_basket_button) == "Your Basket", "login failed"

    def check_if_login_failed(self):
        assert self.is_text_present(locators.invalid_email_password_message, ) == "Invalid email or password.", \
            "'login failed' message is missing"
