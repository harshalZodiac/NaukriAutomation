from playwright.sync_api import Page
from config.locators import *


class JobSearchPage:
    def __init__(self, page:Page):
        self.page = page
        self.job_search_start = JOB_SEARCH_START
        self.job_search_keyword = JOB_SEARCH_KEYWORD
        self.job_search_location = JOB_SEARCH_LOCATION
        self.search_button = SEARCH_BUTTON
        self.freshness_filter = FILTER_FRESHNESS
        self.freshness_filter_last_single_day = FILTER_FRESHNESS_LAST_1_DAY
        self.filters_applied = APPLIED_FILTERS

    def start_job_search(self):
        self.page.locator(self.job_search_start).click()

    def search_job(self):
        self.page.locator(self.job_search_keyword).fill("Python Test Automation")
        self.page.locator(self.job_search_location).fill("Bengaluru")
        self.page.locator(self.search_button).click()

    def apply_freshness_filter(self):
        self.page.locator(self.freshness_filter).click()
        self.page.locator(self.freshness_filter_last_single_day).click()
        self.page.locator(self.filters_applied).wait_for(state="visible")
        assert self.page.locator(self.filters_applied).is_visible()
