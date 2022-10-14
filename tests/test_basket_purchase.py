# Add/remove items to the basket and complete purchase flow
import time


def test_add_items_to_basket(home_page):
    home_page.add_item_to_basket_and_check()


def test_delete_items_to_basket(home_page):
    home_page.test_adding()
    time.sleep(5)

