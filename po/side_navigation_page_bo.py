import time

from po.home_page_bo import HomePage
from po.locators import locators


class SideNavigationPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def _click_about_us_button(self):
        self.click_on_element(locators.about_us_button)
        assert "/#/about" in self.driver.current_url, \
            "About Us page doesn't opened !!!!!!!!!"
        return self

    def _go_to_about_us_page(self):
        self.click_navigation_button()
        self._click_about_us_button()
        return self

    def _click_twitter_button(self):
        self.click_on_element(locators.twiter_button)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "twitter.com/owasp_juiceshop" in self.driver.current_url, \
            "'https://twitter.com/owasp_juiceshop' Us page doesn't opened !!!!!!!!!"

    def open_twitter(self):
        self._go_to_about_us_page() \
            ._click_twitter_button()
