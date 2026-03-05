from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class TestLogin:
    def test_valid_login_redirects_to_products(self, driver):
        login = LoginPage(driver)
        login.open().login("standard_user", "secret_sauce")
        assert "/inventory" in driver.current_url

    def test_valid_login_shows_products_title(self, driver):
        login = LoginPage(driver)
        login.open().login("standard_user", "secret_sauce")
        products = ProductsPage(driver)
        assert products.get_page_title() == "Products"

    def test_invalid_password_shows_error(self, driver):
        login = LoginPage(driver)
        login.open().login("standard_user", "wrong_password")
        assert login.is_error_displayed()

    def test_locked_user_cannot_login(self, driver):
        login = LoginPage(driver)
        login.open().login("locked_out_user", "secret_sauce")
        assert login.is_error_displayed()

    def test_empty_fields_show_error(self, driver):
        login = LoginPage(driver)
        login.open().login("", "")
        assert login.is_error_displayed()
