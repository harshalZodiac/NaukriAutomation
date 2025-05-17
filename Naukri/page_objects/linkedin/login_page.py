from config.locators_linkedin import *
from playwright.sync_api import Page
import settings


class LinkedinLoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.linkedin_username_field= LinkedInLoginLocators.USERNAME
        self.linkedin_password_field = LinkedInLoginLocators.PASSWORD
        self.linkedin_sign_in_button = LinkedInLoginLocators.SIGN_IN
        self.keep_me_signed_in = LinkedInLoginLocators.KEEP_ME_LOGGED_IN

    def login_to_linkedin_application(self):
        self.page.goto(settings.LINKEDIN_URL)
        self.page.locator(self.linkedin_username_field).fill(settings.USERNAME)
        self.page.locator(self.linkedin_password_field).fill(settings.PASSWORD)
        try:
            self.page.locator(self.keep_me_signed_in).evaluate("checkbox => checkbox.checked = false")
        except Exception as e:
            print(f"Check box not visible: {e}")
        self.page.locator(self.linkedin_sign_in_button).click()

