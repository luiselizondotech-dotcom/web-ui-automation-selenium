class TestProductListing:
    def test_products_page_shows_correct_count(self, products_page):
        assert products_page.get_product_count() == 6

    def test_products_page_title_is_products(self, products_page):
        assert products_page.get_page_title() == "Products"

    def test_all_products_have_names(self, products_page):
        names = products_page.get_product_names()
        assert all(len(name) > 0 for name in names)

    def test_all_products_have_positive_prices(self, products_page):
        prices = products_page.get_product_prices()
        assert all(price > 0 for price in prices)

    def test_sort_by_name_az(self, products_page):
        products_page.sort_by("az")
        names = products_page.get_product_names()
        assert names == sorted(names)

    def test_sort_by_price_low_to_high(self, products_page):
        products_page.sort_by("lohi")
        prices = products_page.get_product_prices()
        assert prices == sorted(prices)

    def test_add_item_to_cart_updates_badge(self, products_page):
        products_page.add_first_item_to_cart()
        assert products_page.get_cart_badge_count() == 1
