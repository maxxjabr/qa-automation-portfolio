# QA Automation Portfolio

This repository showcases a 4-week QA automation portfolio project using modern Python testing frameworks. The goal is to demonstrate competency with **test planning**, **test structure**, **Selenium**, **Playwright**, and the **Page Object Model (POM)** while simulating a real-world QA workflow.

---

## Weekly Breakdown

| Week | Focus | Tech |
|------|-------|------|
| Week 1 | Test automation on static site | Selenium + Pytest |
| Week 2 | Page Object Model, login + inventory tests | Playwright + Pytest |
| Week 3 | Cart flow, user roles, error handling | Playwright + Pytest |
Week 4 | Realistic final project with dynamic content | Playwright + Pytest |

---

## Tools Used

- Python 3.x
- Selenium
- Playwright
- Pytest
- Page Object Model (POM)
- GitHub

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/maxxjabr/qa-automation-portfolio.git
cd qa-automation-portfolio
```

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
playwright install              # For Playwright tests
```

## Running Tests

### Week 1: Quotes to Scrape (Selenium)
```bash
pytest test_quotes_site/
```

### Weeks 2 & 3: Shopping Site (Playwright)
```bash
pytest test_shopping_site/
```
Set ```headless=False``` in ```conftest.py``` if you want to see the browser during testing.

### Week 4: Final Project (Playwright)
```bash
pytest test_final_project/
```

## Week-by-Week Details

### Week 1: Quotes to Scrape
Automated basic UI tests on https://quotes.toscrape.com using Selenium + Pytest.
#### Tests Included:
- Title presence
- Login visibility
- Pagination functionality

### Week 2: Shopping Site (SauceDemo)
Automated login and inventory page validations on https://saucedemo.com using Playwright + Pytest + POM.
#### Tests Included:
- Valid user login
- Product visibility
- Inventory page assertions

### Week 3: Reporting & GitHub Polish
- Integrated `pytest-html` for automatic HTML reports
- Configured `conftest.py` to capture screenshots on test failures
- Added one flaky test to demonstrate failure reporting
- Configured Playwright screenshots on failure
- Added `pytest.ini` and cleaned up repo structure

### Week 4: Final Project - SauceDemo Test Suite
Built a comprehensive end-to-end test suite on https://saucedemo.com using Playwright, covering realistic e-commerce behaviors. Emphasized code clarity, maintainability, and meaningful automation use cases.
#### Tests Included:
- `test_successful_login`: Verifies valid login credentials and correct redirect behavior
- `test_add_and_remove_from_cart`: Adds and removes an item from the cart and validates item count
- `test_sort_by_price_low_to_high`: Selects "Price (low to high)" from sort dropdown and validates sort behavior
- `test_dynamic_render`: Confirms cart badge dynamically updates after adding item (JS-rendered behavior)
#### Features:
- Page Object Model across all flows (Login, Inventory, Cart)
- Clear test suite organization under `test_final_project/`
- Failure screenshots and HTML report generation (`report.html`)

## Contact
Created by [Mahmoud Jabir](https://github.com/maxxjabr)
Connect with me on [LinkedIn](https://www.linkedin.com/in/max-jabir/)
