import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from .data import URL
from .helpers import *


class BrowserFactory:
    @staticmethod
    def get_driver(browser_name, headless: bool = False):
        if browser_name.lower() == "chrome":
            options = ChromeOptions()            
            return webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")            
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Browser {browser_name} is not supported.")
        

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = BrowserFactory.get_driver(request.param, headless=True)
    driver.maximize_window()
    driver.get(URL.url_stellarburgers)
    yield driver
    driver.quit()
    

@pytest.fixture()
def new_user_with_post_delete():
    login_pass = new_user()        
    yield login_pass    
    delete_user(login_pass[0]["accessToken"])

# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(URL.url_stellarburgers)
#     yield driver
#     driver.quit()


