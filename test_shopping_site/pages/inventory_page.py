class InventoryPage:
    def __init__(self, page):
        self.page = page

    def wait_for_inventory(self):
        self.page.wait_for_selector('.inventory_item')

    def product_names(self):
        return self.page.query_selector_all('.inventory_item_name')
