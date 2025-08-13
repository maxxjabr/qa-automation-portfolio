from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--incognito")  # Use incognito to avoid using cache
options.add_argument("--disable-application-cache")
options.add_argument("--disk-cache-size=0")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

def test_homepage_title():
    driver = webdriver.Chrome(options=options)
    driver.get("http://quotes.toscrape.com/")

    # Wait up to 10 seconds for the login button to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "quote"))
    )
    
    assert "Quotes to Scrape" in driver.title
    driver.quit()

def test_login_button_exists():
    driver = webdriver.Chrome(options=options)
    driver.get("http://quotes.toscrape.com/")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "quote"))
    )
    
    login_link = driver.find_element(By.LINK_TEXT, "Login")
    assert login_link.is_displayed()
    driver.quit()

def test_can_navigate_to_next_page():
    driver = webdriver.Chrome(options=options)
    driver.get("http://quotes.toscrape.com/")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "quote"))
    )
    
    next_link = driver.find_element(By.CSS_SELECTOR, ".next a")
    driver.execute_script("arguments[0].scrollIntoView();", next_link)
    next_link.click()
    
    assert "page/2" in driver.current_url
    driver.quit()
