from test_shopping_site.pages.login_page import LoginPage

def test_invalid_password_login(page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "wrong_password")
    assert login.get_error_message() is not None
