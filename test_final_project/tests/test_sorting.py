from test_final_project.pages.login_page import LoginPage
from test_final_project.pages.inventory_page import InventoryPage

def test_sort_by_price_low_to_high(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.goto()
    login.login()
    inventory.wait_for_inventory()

    inventory.sort_by("lohi")
    prices = inventory.get_all_prices()
    assert prices == sorted(prices), f"Prices not sorted low to high: {prices}"