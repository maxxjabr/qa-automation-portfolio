# Shopping Site Test Suite (Week 2)

This suite uses Playwright and Pytest to automate tests on [https://www.saucedemo.com/](https://www.saucedemo.com/).

## What We're Testing
- Successful login with valid credentials
- Product visibility on inventory page
- Placeholder for future: search functionality

## Project Structure
- `tests/`: Pytest test files
- `pages/`: Page Object Model components
- `conftest.py`: Shared test fixtures

## Running the Tests

1. Install dependencies:
```bash
pip install -r requirements.txt
playwright install
```
2. Run tests:
```bash
PYTHONPATH=. pytest test_shopping_site
```

## Notes
- Using Playwright with sync API
- Headless mode is enabled by default but can be disabled for visibility (see 'headless=True' in 'conftest.py')