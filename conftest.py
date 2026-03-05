import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

VALID_USER = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    login = LoginPage(driver)
    login.open().login(VALID_USER, PASSWORD)
    return driver

@pytest.fixture
def products_page(logged_in_driver):
    return ProductsPage(logged_in_driver)
