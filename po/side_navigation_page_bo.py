import logging
import allure

from po.home_page_bo import HomePage
from po.locators import locators


class SideNavigationPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def _click_about_us_button(self):
        self.click_on_element(locators.about_us_button)
        if "/#/about" in self.driver.current_url:
            logging.info("About Us page  opened")
        else:
            logging.warning("About Us page doesn't opened !!!!!!!!!")
        return self

    @allure.step("Go to about us page")
    def _go_to_about_us_page(self):
        self.click_navigation_button()
        self._click_about_us_button()
        return self

    @allure.step("Click Twitter")
    def _click_twitter_button(self):
        self.click_on_element(locators.twiter_button)
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Check if Twitter opened")
    def is_twitter_opened(self):
        return "twitter.com/owasp_juiceshop" in self.driver.current_url

    @allure.step("Open Twitter")
    def open_twitter(self):
        self._go_to_about_us_page() \
            ._click_twitter_button()
