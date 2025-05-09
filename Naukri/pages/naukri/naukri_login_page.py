from playwright.sync_api import Page
from config.locators import *
import settings


class NaukriLoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.login_button= LOGIN_BUTTON
        self.username_field= USERNAME_INPUT
        self.password_field = PASSWORD_INPUT
        self.submit_button = SUBMIT_BUTTON

    def login(self):
        self.page.goto(settings.NAUKRI_URL)
        self.page.locator(self.login_button).click()
        self.page.locator(self.username_field).fill(settings.USERNAME)
        self.page.locator(self.password_field).fill(settings.PASSWORD)
        self.page.locator(self.submit_button).click()

