# browser_options.py
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_chrome_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disk-cache-size=0")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    # Use a temp profile to avoid caching issues
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    return webdriver.Chrome(options=options)
