from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart = (By.CLASS_NAME, "ajax_add_to_cart_button")
        self.cart_modal = (By.ID, "layer_cart")
        self.cart_text = (By.CLASS_NAME, "icon-ok")
    
    def add_first_item_to_cart(self):
        self.driver.find_element(*self.add_to_cart).click()
    
    def is_item_added(self):
        return self.driver.find_element(*self.cart_modal).is_displayed()