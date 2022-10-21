from po.home_page_bo import HomePage
from po.locators import locators


class PurchasePage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def delete_items_from_basket(self):
       list_el = self.get_elements_by_xpath(locators.delete_item_buttons)
       self.press_delete(list_el[0])