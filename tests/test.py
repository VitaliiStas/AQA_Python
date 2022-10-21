import time

from po.locators import locators


def test_login(login_page):
    login_page.open_login_form() \
        .login("javatestvitalii@gmail.com", "Passw0rd", locators.your_basket_button)

    assert login_page.check_if_login_successful(), \
        "login failed"


def test_false_login(login_page):
    login_page.open_login_form() \
        .login("bogus_email@.com", "bogus_password", locators.invalid_email_password_message)
    assert login_page.check_if_login_failed(), \
        "'login failed' message is missing"


def test_opening_social_media(navigation_menu):
    navigation_menu.open_twitter()

    assert navigation_menu.is_twitter_opened(), \
        "'https://twitter.com/owasp_juiceshop' Us page doesn't opened !!!!!!!!!"


def test_leave_feedback(feedback):
    feedback.leave_feedback()
    assert feedback.check_if_feedback_successful(), "The feedback didn't leave !!!!!!!!!"


def test_add_items_to_basket(home_page):
    home_page.add_items_to_basket_and_check()
    assert home_page.check_if_basket_not_empty(), "No elements in the basket.Adding elements failed"
    home_page.delete_all_items_from_basket()


def add_remove_items_and_complete_purchase(purchase):
    purchase.add_items_to_basket_and_check()
    assert purchase.check_if_basket_not_empty(), "No elements in the basket.Adding elements failed"
    purchase.delete_items_from_basket()


def test_buy_last_item_and_check_sold_out(home_page):
    home_page.buy_last_item_and_check_sold_out()
    assert home_page.check_if_only_one_element_present(), "Error with adding last item !!!!!!!!!"
    home_page.delete_all_items_from_basket()


# todo fixture don't work properly
def test_change_user_profile_info(profile):
    profile.change_user_profile_info()
    assert profile.check_if_user_info_correct(),"Changing user profile info and photo upload failed"
    time.sleep(5)

# python -m pytest tests/test.py --alluredir allure
# allure serve allure
