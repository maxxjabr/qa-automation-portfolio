from test_final_project.pages.login_page import LoginPage

def test_successful_login(page):
    login = LoginPage(page)
    login.goto()
    login.login()
    assert "inventory" in page.url