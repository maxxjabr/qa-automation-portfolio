from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "search_query_top")
        self.search_button = (By.NAME, "submit_search")

    def load(self):
        self.driver.get("http://automationpractice.pl/index.php")
    
    def search(self, query):
        self.driver.find_element(*self.search_box).send_keys(query)
        self.driver.find_element(*self.search_button).click()