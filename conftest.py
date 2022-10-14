import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from helpers.web_drivers import get_driver
from po.base_po import BasePage
from po.home_page_bo import HomePage
from po.side_navigation_page_bo import SideNavigationPage


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
    login_page.open_login_form().fill_confirm_login_form("javatestvitalii@gmail.com", "Passw0rd")

    yield HomePage(login_page.driver)

@pytest.fixture()
def navigation_menu(home_page) -> SideNavigationPage:

    yield SideNavigationPage(home_page.driver)

