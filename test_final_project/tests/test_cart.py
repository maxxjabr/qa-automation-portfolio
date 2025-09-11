import pytest
from test_final_project.pages.login_page import LoginPage
from test_final_project.pages.inventory_page import InventoryPage
from test_final_project.pages.cart_page import CartPage

def test_add_and_remove_from_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.goto()
    login.login()
    inventory.wait_for_inventory()

    inventory.add_first_item_to_cart()
    inventory.open_cart()

    assert len(cart.get_cart_items()) > 0, "Cart should contain an item after adding"

    page.go_back()
    inventory.remove_first_item_from_cart()
    inventory.open_cart()

    assert len(cart.get_cart_items()) == 0, "Cart should be empty after removing the item"
