from playwright.sync_api import Page
from config.locators_linkedin import *


class LinkedinProfilePage:
    def __init__(self, page:Page):
        self.page = page
        self.feed_page_profile_section = LinkedInProfileLocators.FEED_PAGE_PROFILE_SECTION
        self.edit_profile_section = LinkedInProfileLocators.EDIT_BUTTON
        self.save_profile_section = LinkedInProfileLocators.SAVE_PROFILE

    def view_linkedin_profile(self):
        self.page.locator(self.feed_page_profile_section).click()

    def edit_linkedin_profile(self):
        self.page.locator(self.edit_profile_section).first.click()
        self.page.locator(self.save_profile_section).click()
