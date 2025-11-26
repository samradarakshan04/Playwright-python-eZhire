# # conftest.py
#
# import pytest
# from playwright.sync_api import sync_playwright
#
# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()
#
# @pytest.fixture(scope="function")
# def page(browser):
#     page = browser.new_page()
#     yield page
#     page.close()

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         yield page
#         browser.close()

def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()