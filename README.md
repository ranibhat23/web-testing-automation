# Web Testing Automation

Automated UI tests for the SauceDemo e-commerce application using Python, Selenium and Pytest.

## Project Overview

This project demonstrates basic web UI automation and testing using the Page Object Model (POM).

The tests cover login functionality and product interactions.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- Git & GitHub

## Test Scenarios

### Login

- Verify successful login with valid credentials
- Verify error message for invalid login credentials

### Products

- Verify a product can be added to the shopping cart
- Verify the cart count is updated correctly

## Project Structure

```text
web-testing-automation/
│
├── pages/
│   ├── login_page.py
│   └── inventory_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_products.py
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## How to Run

Clone the repository:

```bash
git clone <your-repository-url>
```

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
pytest
```

## Future Improvements

- Add checkout test scenarios
- Add test reporting
- Add screenshots for failed tests
- Add test data using Pytest fixtures
- Add CI/CD using GitHub Actions
