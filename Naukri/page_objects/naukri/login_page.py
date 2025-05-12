from playwright.sync_api import Page
from config.locators_naukri import *
import settings


class NaukriLoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.login_button= NaukriLoginLocators.LOGIN_BUTTON
        self.username_field= NaukriLoginLocators.USERNAME_INPUT
        self.password_field = NaukriLoginLocators.PASSWORD_INPUT
        self.submit_button = NaukriLoginLocators.SUBMIT_BUTTON

    def login(self):
        self.page.goto(settings.NAUKRI_URL)
        self.page.locator(self.login_button).click()
        self.page.locator(self.username_field).fill(settings.USERNAME)
        self.page.locator(self.password_field).fill(settings.PASSWORD)
        self.page.locator(self.submit_button).click()

