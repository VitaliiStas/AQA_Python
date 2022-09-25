from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    browser_options = Options()
    browser_options.add_argument("--window-size=1200,800")
    driver = Chrome(executable_path=ChromeDriverManager().install(), options=browser_options)
    return driver

