from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
    
    def goto(self):
        self.page.goto("https://www.saucedemo.com/")
    
    def login(self, username="standard_user", password="secret_sauce"):
        self.page.fill('input[data-test="username"]', username)
        self.page.fill('input[data-test="password"]', password)
        self.page.click('input[data-test="login-button"]')
    
    def get_error_message(self):
        return self.page.text_content('h3[data-test="error"]')
