class LoginPage:
    # URL = "https://www.ezhire.me/erp/#/login"
    # USERNAME_FIELD = "//form[@id='my_captcha_form']//input[@id='login__username']"
    # PASSWORD_FIELD = "//form[@id='my_captcha_form']//input[@id='login__password']"
    # LOGIN_BUTTON = "//form[@id='my_captcha_form']//button[@type='submit']"

    def __init__(self, page):
        self.page = page
    URL ="https://the-internet.herokuapp.com/login"
    def go_to(self):
        self.page.goto(self.URL)
        self.page.wait_for_timeout(5000)


    def login(self, username, password):
        # self.page.locator(self.USERNAME_FIELD).fill(username)
        # self.page.locator(self.PASSWORD_FIELD).fill(password)
        # self.page.locator(self.LOGIN_BUTTON).click()

        # page = context.new_page()

        self.page.get_by_label("Username").wait_for()
        self.page.get_by_label("Username").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button").click()

            # self.page.wait_for_timeout(5000)
            # self.page.get_by_label("Username").fill(username)
            # self.page.wait_for_timeout(5000)
            # self.page.get_by_label("Password").fill(password)
            # self.page.wait_for_timeout(5000)
            # self.page.get_by_role("button").click()
            # self.page.wait_for_timeout(5000)
