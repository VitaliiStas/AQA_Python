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


def test_add_remove_items_and_complete_purchase(purchase):
    purchase.add_items_to_basket_and_check()
    assert purchase.check_if_basket_not_empty(), "No elements in the basket.Adding elements failed"
    purchase.delete_item_from_basket().click_checkout_button()
    assert purchase.check_if_select_address_page_opened(), "Select address page doesn't opened"
    purchase.click_add_new_address_button()
    assert purchase.check_if_add_new_address_page_opened(), "Add new address page doesn't opened"
    purchase.fill_address_form().select_delivery_address()
    assert purchase.check_if_delivery_method_page_opened(), "Delivery-method page doesn't opened"
    purchase.select_delivery_speed()
    assert purchase.check_if_my_payment_option_page_opened(), "My payment option page doesn't opened"
    purchase.fill_my_payment_options_information().choose_card()
    assert purchase.check_if_order_summary_page_opened(), "Order summary page doesn't opened"
    purchase.pay()
    assert purchase.check_if_purchase_complete(),"Purchase doesn't complete!!!!!!"

def test_buy_last_item_and_check_sold_out(home_page):
    home_page.buy_last_item_and_check_sold_out()
    assert home_page.check_if_only_one_element_present(), "Error with adding last item !!!!!!!!!"
    home_page.delete_all_items_from_basket()


def test_change_user_profile_info(profile):
    profile.change_user_profile_info()
    assert profile.check_if_user_info_correct(),"Changing user profile info and photo upload failed"

# python -m pytest tests/test.py --alluredir allure
# allure serve allure
