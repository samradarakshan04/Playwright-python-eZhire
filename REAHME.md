Playwright + Pytest + Pytest-BDD + POM (Page Object Model)

project_root/
├── features/                   # All Gherkin feature files (plain English specs)
│   ├── login.feature
│   ├── dashboard.feature
│   └── booking.feature
│
├── steps/                      # Step definition files (Python glue code for features)
│   ├── login_steps.py
│   ├── dashboard_steps.py
│   └── booking_steps.py
│
├── pages/                      # Page Object Model classes (UI abstraction per page)
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── booking_page.py
│
├── tests/                      # (Optional) other pytest tests unrelated to BDD
│
├── conftest.py                 # Pytest fixtures & Playwright setup
├── requirements.txt            # Python dependencies
└── pytest.ini                  # Pytest configuration (optional)


