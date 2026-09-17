# Web Testing Automation

Automated web UI testing project built with **Python, Selenium WebDriver and pytest**.

This project automates key user journeys on [SauceDemo](https://www.saucedemo.com/), including login validation, product interactions, shopping cart functionality and checkout.

The project follows the **Page Object Model (POM)** design pattern and includes automated HTML reporting and GitHub Actions CI.

## Tech Stack

- Python
- Selenium WebDriver
- pytest
- pytest-html
- Git & GitHub
- GitHub Actions
- Chrome WebDriver

## Automated Test Scenarios

The test suite currently contains 7 automated tests:

### Login

- Valid user login
- Invalid user login
- Locked-out user login

### Products

- Add Sauce Labs Backpack to cart
- Remove Sauce Labs Backpack from cart

### Cart

- Verify selected product is displayed in the cart

### Checkout

- Complete an end-to-end checkout successfully
- Verify the order confirmation message

## Project Structure

```text
web-testing-automation/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── reports/
│   └── screenshots/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Framework Design

The project uses the **Page Object Model** to separate test logic from page-specific locators and actions.

### Base Page

`BasePage` contains reusable Selenium functionality such as:

- Clicking elements
- Entering text
- Reading element text
- Checking element visibility
- Explicit waits

### Page Objects

Each application page has its own page object:

- `LoginPage`
- `InventoryPage`
- `CartPage`
- `CheckoutPage`

This makes the tests easier to read, maintain and extend.

## Running the Tests

### 1. Clone the repository

```bash
git clone https://github.com/ranibhat23/web-testing-automation.git
cd web-testing-automation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the tests

```bash
pytest
```

## HTML Test Report

Generate a self-contained HTML report using:

```bash
pytest --html=reports/report.html --self-contained-html
```

The report provides an overview of passed and failed tests and execution details.

## Failure Screenshots

The framework automatically captures a screenshot when a test fails.

Screenshots are stored under:

```text
reports/screenshots/
```

This helps with debugging UI failures during local execution and CI runs.

## Continuous Integration

The project uses **GitHub Actions** to automatically execute the test suite in a Linux CI environment.

The workflow:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Runs the pytest test suite
5. Reports the test results

The test suite has been verified to pass both locally and in GitHub Actions.

### Current Test Result

```text
7 passed
```

## What This Project Demonstrates

This project demonstrates practical experience with:

- UI test automation
- Selenium WebDriver
- Python and pytest
- Page Object Model
- Explicit waits and synchronization
- Functional testing
- Positive and negative test scenarios
- End-to-end testing
- Test reporting
- Failure screenshot capture
- Continuous integration with GitHub Actions
- Debugging tests across local and CI environments

## Future Improvements

Potential future enhancements include:

- Parameterised test data
- Additional product and checkout scenarios
- API testing
- Cross-browser testing
- Parallel test execution
- Allure reporting
- Expanded CI test coverage
