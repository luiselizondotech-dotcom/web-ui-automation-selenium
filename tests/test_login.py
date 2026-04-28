import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class TestLogin:
    def test_valid_login_redirects_to_products(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        assert "/inventory" in driver.current_url

    def test_valid_login_shows_products_title(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        products = ProductsPage(driver)
        assert products.get_page_title() == "Products"

@pytest.mark.parametrize("username,password,expected_error", [
    ("standard_user", "wrong_password", "do not match"),
    ("locked_out_user", "secret_sauce", "locked out"),
    ("", "secret_sauce", ""),
])
def test_login_invalid_cases(driver, username, password, expected_error):
    login = LoginPage(driver)
    login.open()
    login.login(username, password)

    error = login.get_error().lower()
    assert expected_error in error or "Epic sadface" in error
