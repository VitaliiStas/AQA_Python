import logging
import allure
from po.home_page_bo import HomePage
from po.locators import locators


class UserProfilePage(HomePage):
    image_url = "https://www.pinterest.com/pin/573153490062754309/"
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def _click_user_profile_button(self):
        self.click_on_element(locators.go_to_user_profile)

        if "/profile" in self.driver.current_url:
            logging.info("Profile page opened")
        else:
            logging.warning("Profile page doesn't opened !!!!!!!!!")
        return self

    def fill_confirm(self,input_for_text,button_for_click,text):
        # need to clean form before typing a new data
        self.get_element_by_xpath(input_for_text).clear()
        self.type_data(input_for_text, text)
        self.click_on_element(button_for_click)

    @allure.step("Type user name")
    def _set_username(self,username="Random Text"):
        self.fill_confirm(locators.user_name_input,locators.set_username_button,username)

    @allure.step("upload img")
    def upload_img(self,path_to_img):
        self.get_element_by_xpath(locators.input_for_selecting_the_profile_picture).send_keys(path_to_img)
        self.click_on_element(locators.button_to_upload_the_profile_picture)

    def check_if_user_info_correct(self):
        return self.get_attribute_value(locators.user_name_input,"value") == "Random Text"

    # Change user profile info and photo upload
    def change_user_profile_info(self):
        self.click_on_element(locators.account_button)
        self._click_user_profile_button()
        self._set_username()
        self.upload_img("C:/Users/vitalii.stasiv/Desktop/AQA_mentorship/AQA_Python/img.jpg")