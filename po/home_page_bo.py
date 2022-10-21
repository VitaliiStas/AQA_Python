import logging
import time

import allure
from selenium import webdriver
from selenium.common import StaleElementReferenceException

from po.base_po import BasePage
from po.locators import locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_all_items_from_page(self):
        return self.get_elements_by_xpath(locators.items_on_page)

    def add_item_to_basket(self, element):
        self.click_on_element(element)

    def click_elements_from_list(self, list_of_elements):
        for el in list_of_elements:
            webdriver.ActionChains(self.driver) \
                .move_to_element(el).click(el).perform()

    @allure.step("Add all items to the basket")
    def add_all_items_to_basket(self, click_elements_from_list):
        self.click_elements_from_list(click_elements_from_list)
        return self

    @allure.step("Go to the basket")
    def go_to_basket(self):
        self.click_on_element(locators.basket_button)
        return self

    def press_delete(self, el):
        # webdriver.ActionChains(self.driver) \
        #     .move_to_element(el).click(el).perform()
        self.driver.execute_script("arguments[0].click();", el)
        return self

    @allure.step("Delete all items from the basket")
    def delete_all_items_from_basket(self):
        try:
            for el in self.get_elements_by_xpath(locators.delete_item_buttons):
                webdriver.ActionChains(self.driver) \
                    .move_to_element(el)
                self.press_delete(el)

        except StaleElementReferenceException as Exception:
            print('AAAAAAAAAAAAAAAAAAAAAAA')

    def check_if_basket_not_empty(self):
        return self.get_elements_by_xpath(locators.delete_item_buttons) is not None

    def add_items_to_basket_and_check(self):
        self.add_all_items_to_basket(self.get_all_items_from_page())
        self.go_to_basket()


    def click_navigation_button(self):
        el = locators.side_navigation_button
        self.click_on_element(el)
        # time.sleep(1)
        if self._get_text_from_element("//*[text()='Contact']") == "Contact":
            logging.info("Navigation page opened")
        else:
            logging.warning("Navigation page doesn't opened !!!!!!!!!")
        return self


    def _click_on_last_item(self):
        # for x in range(4):
        for x in range(8):
            self.driver.execute_script("arguments[0].click();", self.get_element_by_xpath(locators.only_one_item_element))
        return self

    @allure.step("Choose the sold out item ")
    # Buying last items and checking if items are marked as sold-out
    def buy_last_item_and_check_sold_out(self):
        self._click_on_last_item()

    @allure.step("Check if element sold out")
    def check_if_only_one_element_present(self):
        self.go_to_basket()
        # this check if sold item is only one in the basked
        return self.get_element_by_xpath(locators.element_for_check).text == "Best Juice Shop Salesman Artwork"


