# # from pages.pre_booking_page import PreBookingPage
# # from apis.booking_api import create_booking
# # from db.query_executor import fetch_booking_by_id
# # from playwright.sync_api import Page
# # def test_booking_ui_vs_api_vs_db(browser , PreBookingPage):
# #     # page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# #     page.set_viewport_size(({"width":1920, "height":1080}))
# #     page.wait_for_timeout(5000)
# #     title=page.title()
# #     print("Page of the title"+title)
# #     # assert "EZHIRE" in title
# #     # Step 1: Create booking via API
# #     # booking_data = {
# #     #     "name": "Test User",
# #     #     "date": "2025-09-10"
# #     # }
# #     # api_response = create_booking(booking_data)
# #     # booking_id = api_response["id"]
# #     #
# #     # # Step 2: Validate in DB
# #     # db_record = fetch_booking_by_id(booking_id)
# #     # assert db_record["name"] == "Test User"
# #     #
# #     # # Step 3: Validate in UI
# #     # page = browser.new_page()
# #     # booking = PreBookingPage(page)
# #     # booking.navigate()
# #     # booking.fill_form("Test User", "2025-09-10")
# #     # booking.submit()
# #     #
# #     # assert booking.is_confirmation_displayed()
#
# from pages.pre_booking_page import PreBookingPage
#
# def test_open_pre_booking_page(browser):
#     page = browser.new_page()
#     booking_page = PreBookingPage(page)
#
#     booking_page.navigate()
#
#     assert "pre_booking_generation" in page.url
#
#     page.close()  # ✅ Always close pages after the test