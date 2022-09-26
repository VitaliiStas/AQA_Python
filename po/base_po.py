import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from helpers.web_drivers import get_driver
from po.xpath import locators


class BasePage:
    def wait_sec(self):
        time.sleep(1)

    BASE_URL = "http://localhost:3000/#/"

    def __init__(self, driver, BASE_URL=None):
        self.driver = driver
        self.BASE_URL = self.BASE_URL if BASE_URL is None else BASE_URL
        self.open_page(self.BASE_URL)

    def open_page(self, url):
        if not url:
            url = self.BASE_URL
        driver.get(url)
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

    def check_if_login_failed(self):
        assert self.get_element_by_xpath(locators.invalid_email_password_messsage), 'Login Not Failed'
        # assert "Invalid email or password2" in driver.page_source

    def is_element_present(self, element):
        try:
            self.get_element_by_xpath(element)
            return True
        except NoSuchElementException:
            return False


