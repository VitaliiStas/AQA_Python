import time


def test_login(login_page):
    login_page.open_login_form() \
        .fill_confirm_login_form("javatestvitalii@gmail.com", "Passw0rd") \
        .check_if_login_successful()


def test_false_login(login_page):
    login_page.open_login_form() \
        .fill_confirm_login_form("bogus_email@.com", "bogus_password") \
        .check_if_login_failed()


def test_opening_social_media(navigation_menu):
    navigation_menu.open_twitter()


def test_leave_feedback(feedback):
    feedback.leave_feedback()


def test_add_items_to_basket(home_page):
    home_page.add_item_to_basket_and_check()


def test_delete_items_to_basket(home_page):
    home_page.test_adding()


def test_buy_last_item_and_check_sold_out(home_page):
    home_page.buy_last_item_and_check_sold_out()
    time.sleep(5)
