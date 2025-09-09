class InventoryPage:
    def __init__(self, page):
        self.page = page

    def wait_for_inventory(self):
        self.page.wait_for_selector('.inventory_item')

    def product_names(self):
        return self.page.query_selector_all('.inventory_item_name')
    
    def add_first_item_to_cart(self):
        self.page.locator(".inventory_item button").first.click()
    
    def remove_first_item_from_cart(self):
        self.page.locator(".inventory_item button").first.click()  # Same button toggles to "Remove"
    
    def open_cart(self):
        self.page.click("#shopping_cart_container")
