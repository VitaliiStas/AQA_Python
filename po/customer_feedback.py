
from selenium.webdriver import ActionChains

from po.home_page_bo import HomePage
from po.locators import locators


class FeedbackPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def _click_customer_feedback_button(self):
        self.click_on_element(locators.customer_feedback_button)
        assert "/#/contact" in self.driver.current_url, \
            "Customer Feedback page doesn't opened !!!!!!!!!"
        return self

    def _type_feedback(self, feedback):
        self.type_data(locators.comment_field_form, feedback)
        return self

    def _set_slider_rating(self):
        ActionChains(self.driver).drag_and_drop_by_offset(self.get_element_by_xpath(locators.slider), 50, 0).perform()
        return self

    def _get_captcha(self):
        return self.get_element_by_xpath(locators.captcha).text

    def _type_captcha_result(self):
        self.type_data(locators.captcha_result_form, eval(self._get_captcha()))
        return self

    def leave_feedback(self):
        self.click_navigation_button()
        self._click_customer_feedback_button()
        self._set_slider_rating()
        self._type_feedback("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

        self._type_captcha_result()
        self.click_on_element(locators.submit)
        # assert self.is_text_present(locators.thank_you_for_your_feedback) == "Thank you for your feedback", \
        #     "The feedback didn't leave !!!!!!!!!"

        assert self.get_element_by_xpath("//*[@class='mat-slider-thumb-label-text']").text != "None", \
            "The feedback didn't leave !!!!!!!!!"
        return self
