from playwright.sync_api import Page
from config.locators import *


class ProfilePage:
    def __init__(self, page:Page):
        self.page = page
        self.view_profile_button = VIEW_PROFILE
        self.profile_name = PROFILE_NAME
        self.profile_percentage_value = PROFILE_PERCENTAGE_VALUE
        self.edit_general_profile = EDIT_GENERAL_PROFILE
        self.save_general_profile_section = SAVE_GENERAL_PROFILE_SECTION
        self.last_updated_today = LAST_UPDATED_PROFILE_TODAY

    def view_profile(self):
        self.page.locator(self.view_profile_button).click()

    def get_profile_name(self):
        return self.page.locator(self.profile_name).inner_text()

    def get_profile_percentage_value(self):
        percentage_text = self.page.locator(self.profile_percentage_value).inner_text()
        percentage_value = percentage_text.replace("%", "").strip()
        return percentage_value

    def edit_general_profile_section(self):
        self.page.locator(self.edit_general_profile).click()
        self.page.locator(self.save_general_profile_section).click()
        self.page.locator(self.last_updated_today).wait_for(state="visible")
        assert self.page.locator(self.last_updated_today).is_visible()
