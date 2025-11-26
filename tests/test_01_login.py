# from steps import login_steps  # This ensures pytest sees your step implementations
# from pytest_bdd import scenarios
#
# scenarios('../features/login.feature')

from pytest_bdd import scenarios
# from steps.login_steps import *  # This import is crucial for pytest-bdd to register steps
#
# scenarios('login.feature')

from pytest_bdd import scenario

@scenario('../features/login.feature', 'Successful login')
def test_successful_login():
    pass


def test_launch_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.wait_for_timeout(5000)
    page.get_by_label("Username").fill("tomsmith")
    page.wait_for_timeout(5000)
    page.get_by_label("Password").fill("SuperSecretPassword")
    page.wait_for_timeout(5000)
    page.get_by_role("button").click()
    page.wait_for_timeout(5000)

