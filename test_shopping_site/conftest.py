import pytest
from playwright.sync_api import sync_playwright, Page
from datetime import datetime
import os

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        print(f"[DEBUG] funcargs: {item.funcargs}")
        page = item.funcargs.get("page", None)
        if page:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            ss_dir = "test_shopping_site/screenshots"
            os.makedirs(ss_dir, exist_ok=True)
            screenshot_name = os.path.join(ss_dir, f"{item.name}_{timestamp}.png")
            page.screenshot(path=screenshot_name)
            print(f"Saving screenshot to {screenshot_name}")
        else:
            print("jk lmao fu")