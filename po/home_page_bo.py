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

    def add_all_items_to_basket(self, click_elements_from_list):
        self.click_elements_from_list(click_elements_from_list)
        return self

    def go_to_basket(self):
        self.click_on_element(locators.basket_button)

    def press_delete(self, el):
        webdriver.ActionChains(self.driver) \
            .move_to_element(el).click(el).perform()
        return self

    # todo can't delete all elements, delete only first
    def delete_items_from_basket(self):
        try:
            for el in self.get_elements_by_xpath(locators.delete_item_buttons):
                webdriver.ActionChains(self.driver) \
                    .move_to_element(el)
                self.press_delete(el)

        except StaleElementReferenceException as Exception:
            print('AAAAAAAAAAAAAAAAAAAAAAA')

    def add_item_to_basket_and_check(self):
        self.add_all_items_to_basket(self.get_all_items_from_page())
        self.go_to_basket()

        assert self.get_elements_by_xpath(locators.delete_item_buttons) is not None, \
            "No elements in the basket.Adding elementas failed"

    def test_adding(self):
        self.add_all_items_to_basket(self.get_all_items_from_page())
        self.go_to_basket()

        self.delete_items_from_basket()

    def click_navigation_button(self):
        el = locators.side_navigation_button
        self.click_on_element(el)

        assert self.is_text_present("//*[text()='Contact']") == "Contact", \
            "Navigation page doesn't opened !!!!!!!!!"
        return self
