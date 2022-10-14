import time


def test_login(login_page):
    login_page.open_login_form() \
        .fill_confirm_login_form("javatestvitalii@gmail.com", "Passw0rd") \
        .check_if_login_successful()

def test_false_login(login_page):
    login_page.open_login_form()\
        .fill_confirm_login_form("bogus_email@.com", "bogus_password")\
        .check_if_login_failed()

