from test_shopping_site.pages.login_page import LoginPage
from test_shopping_site.pages.inventory_page import InventoryPage

def test_product_names_are_visible(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.goto()
    login.login()
    inventory.wait_for_inventory()
    assert len(inventory.product_names()) > 0
