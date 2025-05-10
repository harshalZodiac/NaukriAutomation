import time

from playwright.sync_api import Page
from config.linkedin_locators import *
import settings


class LinkedinJobApplyPage:
    def __init__(self, page:Page):
        self.page = page
        self.job_apply_section = LINKEDIN_JOB_SECTION
        self.job_search_input = LINKEDIN_JOB_TITLE
        self.job_section_side_bar = LINKEDIN_JOB_SECTION_SIDE_BAR
        self.date_posted_filter = DATE_POSTED_FILTER_OPTIONS
        self.date_posted_last_one_day = DATE_POSTED_LAST_ONE_DAY
        self.easy_apply_filter = EASY_APPLY_FILTER
        self.apply_date_filter = APPLY_DATE_POSTED_FILTER
        self.linkedin_job_post = LINKEDIN_JOB_POST
        self.linkedin_job_apply = LINKEDIN_APPLY_BUTTON
        self.next_button = NEXT_BUTTON

    def navigate_to_job_section(self):
        self.page.locator(self.job_apply_section).click()

    def provide_job_search_input(self):
        self.page.locator(self.job_section_side_bar).first.wait_for(state="visible")
        self.page.locator(self.job_search_input).first.fill(settings.LINKEDIN_JOB_SEARCH_TITLES)
        self.page.locator(self.job_search_input).last.fill(settings.LINKEDIN_JOB_SEARCH_LOCATIONS)
        time.sleep(2)
        self.page.keyboard.press("Enter")

    def apply_filter_date_posted(self):
        self.page.locator(self.date_posted_filter).wait_for(state="visible")
        self.page.locator(self.date_posted_filter).click()
        self.page.locator(self.date_posted_last_one_day).click()
        self.page.locator(self.apply_date_filter).first.click()

    def apply_filter_easy_apply(self):
        self.page.locator(self.easy_apply_filter).wait_for(state="visible")
        self.page.locator(self.easy_apply_filter).click()

    def apply_linkedin_jobs(self, job_post):
        self.page.locator(self.linkedin_job_post).nth(job_post).wait_for(state="visible")
        self.page.locator(self.linkedin_job_post).nth(job_post).click()
        time.sleep(2)
        self.page.locator(self.linkedin_job_apply).first.wait_for(state="visible")
        self.page.locator(self.linkedin_job_apply).first.click()
        self.page.locator(self.next_button).wait_for(state="visible")
        self.page.locator(self.next_button).click()
