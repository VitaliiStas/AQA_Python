import os

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from allure_commons._allure import attach,test
from helpers.web_drivers import get_driver
from po.base_po import BasePage
from po.customer_feedback import FeedbackPage
from po.home_page_bo import HomePage
from po.locators import locators
from po.purchase_po import PurchasePage
from po.side_navigation_page_bo import SideNavigationPage
from po.user_profile_po import UserProfilePage

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'driver' in item.fixturenames:
                    web_driver = item.funcargs['driver']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot' + test.__name__,
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture()
def driver(request) -> WebDriver:
    drv = get_driver()

    yield drv  # this code run after ending previous
    drv.quit()


@pytest.fixture()
def login_page(driver) -> BasePage:
    yield BasePage(driver)


@pytest.fixture()
def home_page(login_page) -> HomePage:
    login_page.open_login_form().login("javatestvitalii@gmail.com", "Passw0rd",locators.basket_button)

    yield HomePage(login_page.driver)


@pytest.fixture()
def navigation_menu(home_page) -> SideNavigationPage:
    yield SideNavigationPage(home_page.driver)


@pytest.fixture()
def feedback(home_page) -> FeedbackPage:
    yield FeedbackPage(home_page.driver)


@pytest.fixture()
def profile(home_page) -> UserProfilePage:
    # time.sleep(10)
    yield UserProfilePage(home_page.driver)

@pytest.fixture()
def purchase (home_page) -> PurchasePage:
    # time.sleep(10)
    yield PurchasePage(home_page.driver)
