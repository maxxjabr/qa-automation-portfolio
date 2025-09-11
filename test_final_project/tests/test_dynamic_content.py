from test_final_project.pages.login_page import LoginPage
from test_final_project.pages.inventory_page import InventoryPage

def test_dynamic_render(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.goto()
    login.login()
    inventory.wait_for_inventory()

    assert not inventory.page.is_visible(".shopping_cart_badge")

    inventory.add_first_item_to_cart()
    inventory.page.wait_for_selector(".shopping_cart_badge")
    
    badge_count = inventory.page.text_content(".shopping_cart_badge")
    assert badge_count == "1", f"Expected cart badge to show '1', got '{badge_count}'"