# 🌐 Web UI Automation — Selenium + Pytest

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
web-ui-automation-selenium/
├── tests/
│   ├── test_login.py       # Login tests with data-driven cases
│   └── test_products.py    # Product listing and cart tests
├── pages/
│   ├── base_page.py        # Base page with shared methods
│   ├── login_page.py       # Login page object
│   └── products_page.py    # Products page object
├── reports/                # HTML test reports
├── conftest.py             # Pytest fixtures
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

```bash
# Clone
git clone https://github.com/luiselizondotech-dotcom/web-ui-automation-selenium
cd web-ui-automation-selenium

# Install
pip install -r requirements.txt

# Run tests
pytest -v --html=reports/report.html --self-contained-html
```

## 🧩 Test Coverage

| Module | Test Cases |
|--------|-----------|
| Login | Valid login, invalid credentials, locked user, empty fields (parameterized) |
| Products | Product count, sorting, add to cart |
| Cart | Badge count validation |

## 🧠 Key Concepts

- ✅ Page Object Model (POM) design pattern
- ✅ Explicit waits (WebDriverWait)
- ✅ Data-driven testing with `@pytest.mark.parametrize`
- ✅ Fixtures with setup/teardown
- ✅ Headless Chrome execution

## 👤 Author

**Luis Elizondo** — QA Engineer  
[LinkedIn](https://www.linkedin.com/in/qa-engineer-elizondo-luis) | [GitHub](https://github.com/luiselizondotech-dotcom)
