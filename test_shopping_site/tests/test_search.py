import pytest
from test_shopping_site.pages.home_page import HomePage

@pytest.mark.smoke
def test_search_for_product(driver):
    homepage = HomePage(driver)

    # Arrange
    homepage.load()

    # Act
    homepage.search("dress")

    # Assert
    assert "search_query=dress" in driver.current_url