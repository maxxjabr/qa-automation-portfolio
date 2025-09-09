from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_item_selector = ".cart_item"
        self.item_name_selector = ".inventory_item_name"

    def get_cart_items(self):
        return self.page.query_selector_all(self.cart_item_selector)

    def get_first_item_name(self):
        return self.page.locator(self.item_name_selector).first.text_content()