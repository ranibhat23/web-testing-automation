# Web Testing Automation Framework

A Python-based web UI automation framework built with Selenium and Pytest.

## Overview

This project automates end-to-end testing of the SauceDemo e-commerce application.

The framework uses the Page Object Model to separate test scenarios from page interactions and includes reusable WebDriver fixtures, explicit waits, failure screenshots and automated CI testing with GitHub Actions.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- GitHub Actions
- HTML Test Reports

## Test Coverage

### Authentication

- Valid login
- Invalid login
- Locked-out user

### Product & Cart

- Add product to cart
- Remove product from cart
- Verify cart contents

### Checkout

- Enter customer information
- Complete checkout
- Verify order confirmation

## Running Tests

Install dependencies:

```bash
pip install -r requirements.txt
```
