import time


def test_login(login_page):
    time.sleep(2)


def test_false_login(login_page):
    login_page.open_login_form().fill_confirm_login_form().check_if_login_failed()
    time.sleep(2)
