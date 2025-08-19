import pytest
from test_shopping_site.pages.home_page import HomePage
from test_shopping_site.pages.product_page import ProductPage
import time

@pytest.mark.regression
def test_add_item_to_cart(driver):
    homepage = HomePage(driver)
    product_page = ProductPage(driver)

    homepage.load()
    homepage.search("dress")
    time.sleep(2)  # Give time for products to load

    product_page.add_first_item_to_cart()
    time.sleep(3)  # Wait for cart modal to appear

    assert product_page.is_item_added()