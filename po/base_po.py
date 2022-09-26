import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

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
        return self.driver.find_element(By.XPATH, xpath)

    def click_on_element(self, element):
        self.get_element_by_xpath(element).click()

    def type_data(self, element, text):
        self.get_element_by_xpath(element).send_keys(text)

    def open_login_form(self):
        self.click_on_element(locators.dismiss_button)
        self.click_on_element(locators.account_button)
        self.click_on_element(locators.login_button)
        return self

    def fill_confirm_login_form(self):
        self.type_data(locators.email_field, "bogus@email.com")
        self.type_data(locators.password_field, "bogus_password")
        self.click_on_element(locators.login_confirm_button)
        return self

    def is_element_present(self, element):
        try:
            self.get_element_by_xpath(element)
            return True
        except NoSuchElementException:
            return False

    def check_if_login_failed(self):
        assert self.is_element_present(locators.invalid_email_password_messsage), "'login failed' message is missing"

