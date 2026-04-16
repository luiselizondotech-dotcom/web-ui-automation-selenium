# Web UI Automation — SauceDemo E-commerce

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white) ![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=flat-square&logo=selenium&logoColor=white) ![Pytest](https://img.shields.io/badge/Pytest-latest-0A9EDC?style=flat-square) ![Tests](https://img.shields.io/badge/Tests-30%2B-brightgreen?style=flat-square)

End-to-end UI automation framework using **Selenium WebDriver** with **Page Object Model (POM)** design pattern on the [SauceDemo](https://www.saucedemo.com) e-commerce application.

## 🎯 What This Project Demonstrates

- **Page Object Model (POM)** architecture for maintainable test code
- **Selenium WebDriver** automation for real browser interaction
- Login flow, product navigation, cart and checkout automation
- **Pytest** fixtures and test organization
- Cross-browser ready structure

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Main language |
| Selenium | 4.x | Browser automation |
| Pytest | Latest | Test framework |
| WebDriver | Chrome/Firefox | Browser driver |

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/luiselizondotech-dotcom/web-ui-automation-selenium

# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest -v

# Run with specific browser
pytest --browser=chrome -v
```

## 📋 Test Coverage

| Module | Test Scenarios |
|--------|---------------|
| Login | Valid login, invalid credentials, locked user |
| Product Page | Sort, add to cart, product details |
| Shopping Cart | Add/remove items, cart validation |
| Checkout | Complete purchase flow, form validation |

## 📊 Results

- ✅ 30+ automated UI test cases
- ✅ Page Object Model architecture applied
- ✅ Covers full e-commerce user journey
- ✅ Reusable components for easy maintenance

## 👤 Author

**Luis Elizondo** — QA Engineer
- GitHub: [@luiselizondotech-dotcom](https://github.com/luiselizondotech-dotcom)
- LinkedIn: [qa-engineer-elizondo-luis](https://www.linkedin.com/in/qa-engineer-elizondo-luis)
- Portfolio: [luis-qa-journey.lovable.app](https://luis-qa-journey.lovable.app)# 🌐 Web UI Automation — Selenium + Pytest

Automated end-to-end UI testing framework for [SauceDemo](https://www.saucedemo.com) using **Python + Selenium WebDriver + Pytest**, following the **Page Object Model (POM)** design pattern.

## 📌 About This Project

SauceDemo is a publicly available e-commerce demo application designed for practicing test automation. This project covers login flows, product browsing, cart management, and checkout processes.

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Main language |
| Selenium WebDriver 4+ | Browser automation |
| Pytest | Test runner |
| pytest-html | HTML reports |
| webdriver-manager | Auto ChromeDriver setup |

## 📁 Project Structure

```
proyecto2-web-automation/
├── tests/
│   ├── test_login.py          # Login page tests
│   ├── test_products.py       # Product listing tests
│   └── test_checkout.py       # Cart & checkout tests
├── pages/
│   ├── base_page.py           # Base page with shared methods
│   ├── login_page.py          # Login page object
│   ├── products_page.py       # Products page object
│   └── checkout_page.py       # Checkout page object
├── utils/
│   └── driver_factory.py      # WebDriver setup/teardown
├── reports/                   # Auto-generated HTML reports
├── docs/
│   └── test-cases.md          # Manual test cases documentation
├── conftest.py                # Pytest fixtures
├── pytest.ini                 # Configuration
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/tu-usuario/web-automation-selenium.git
cd web-automation-selenium
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run all tests
```bash
pytest --html=reports/report.html --self-contained-html -v
```

### 5. Run tests in headless mode
```bash
pytest --html=reports/report.html -v -k "not slow"
```

## 🧩 Test Coverage

| Module | Test Cases | Status |
|--------|-----------|--------|
| Login | Valid login, invalid user, locked user, empty fields | ✅ |
| Products | List visible, sort by price/name, add to cart | ✅ |
| Cart | Add/remove items, badge count | ✅ |
| Checkout | Complete flow, missing fields validation | ✅ |

## 🧠 Key Concepts Demonstrated

- ✅ Page Object Model (POM) design pattern
- ✅ Explicit waits (WebDriverWait)
- ✅ CSS selectors & XPath
- ✅ Test fixtures with setup/teardown
- ✅ Parameterized tests
- ✅ Screenshot on failure
- ✅ Cross-browser ready structure

## 👤 Author

**Tu Nombre** — QA Engineer  
[LinkedIn](#) | [GitHub](#)
