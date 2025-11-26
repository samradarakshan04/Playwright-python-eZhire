# from playwright.sync_api import Page
#
# class PreBookingPage:
#     def __init__(self, page: Page):
#         self.page = page
#         self.url = "https://www.ezhire.me/erp/#/pre_booking_generation/0"
#     #     self.name_input = page.locator("#name")
#     #     self.date_input = page.locator("#date")
#     #     self.submit_button = page.locator("#submit")
#     #     self.confirmation = page.locator(".confirmation")
#     #
#     # def navigate(self):
#     #     self.page.goto(self.url)
#     #
#     # def fill_form(self, name, date):
#     #     self.name_input.fill(name)
#     #     self.date_input.fill(date)
#     #
#     # def submit(self):
#     #     self.submit_button.click()
#     #
#     # def is_confirmation_displayed(self):
#     #     return self.confirmation.is_visible()

from playwright.sync_api import Page

class PreBookingPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.ezhire.me/erp/#/login"

    def navigate(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state('load')  # optional but useful
