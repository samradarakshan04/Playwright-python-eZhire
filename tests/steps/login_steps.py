from pytest_bdd import scenarios, given, when, then
from pages.login_02_page import LoginPage

scenarios('../features/login.feature')

# scenarios('../../features/login.feature')

@given("the user is on the login page")
def go_to_login(page):
    login_page = LoginPage(page)
    login_page.go_to()

@when('the user logs in with "{username}" and "{password}"')
def login(page, username, password):
    login_page = LoginPage(page)
    login_page.login(username, password)

# @then("the user should see the dashboard")
# def verify_dashboard(page):
#     # Replace this with a reliable selector visible after successful login
#     assert page.locator("//div[contains(text(), 'Dashboard')]").is_visible()


@then("the user should see the dashboard")
def verify_dashboard(page):
    # ✅ This is where your line goes
    assert page.locator("//h1[text()='Dashboard']").is_visible()
