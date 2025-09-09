import pytest
from test_shopping_site.pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, should_succeed", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", True),
])
def test_user_login_roles(page, username, password, should_succeed):
    login = LoginPage(page)
    login.goto()
    login.login(username, password)

    if should_succeed:
        assert "inventory" in page.url
    else:
        assert login.get_error_message() is not None
