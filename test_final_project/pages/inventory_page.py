from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
    
    def wait_for_inventory(self):
        self.page.wait_for_selector('.inventory_item')

    def product_names(self):
        return self.page.query_selector_all('.inventory_item_name')

    def add_first_item_to_cart(self):
        self.page.locator(".inventory_item button").first.click()
    
    def remove_first_item_from_cart(self):
        self.page.locator('button:has-text("Remove")').first.click()

    def open_cart(self):
        self.page.click("#shopping_cart_container")
    
    def sort_by(self, sort_option):
        self.page.wait_for_selector('select[data-test="product-sort-container"]', timeout=5000)
        self.page.select_option('select[data-test="product-sort-container"]', sort_option)
    
    def get_all_prices(self):
        price_elements = self.page.locator(".inventory_item_price").all()
        return [float(elem.inner_text().replace("$", "")) for elem in price_elements]