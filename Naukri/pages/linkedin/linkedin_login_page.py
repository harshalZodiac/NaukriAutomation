from config.linkedin_locators import *
from playwright.sync_api import Page
import settings


class LinkedinLoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.linkedin_username_field= LINKEDIN_USERNAME
        self.linkedin_password_field = LINKEDIN_PASSWORD
        self.linkedin_sign_in_button = LINKEDIN_SIGN_IN
        self.keep_me_signed_in = LINKEDIN_KEEP_ME_LOGGED_IN

    def login(self):
        self.page.goto(settings.LINKEDIN_URL)
        self.page.locator(self.linkedin_username_field).fill(settings.USERNAME)
        self.page.locator(self.linkedin_password_field).fill(settings.PASSWORD)
        self.page.locator(self.keep_me_signed_in).evaluate("checkbox => checkbox.checked = false")
        self.page.locator(self.linkedin_sign_in_button).click()

