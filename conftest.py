import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from helpers.web_drivers import get_driver
from po.base_po import BasePage


@pytest.fixture()
def driver(request) -> WebDriver:
    drv = get_driver()
    yield drv  # this code run after ending previous
    drv.quit()


@pytest.fixture()
def login_page(driver) -> BasePage:
    yield BasePage(driver)
