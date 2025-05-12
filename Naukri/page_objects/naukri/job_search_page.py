from playwright.sync_api import Page
from config.locators_naukri import *
import settings
import time
import re

class NaukriJobSearchPage:
    def __init__(self, page:Page):
        self.page = page
        self.job_search_start = NaukriJobSearchLocators.JOB_SEARCH_START
        self.job_search_keyword = NaukriJobSearchLocators.JOB_SEARCH_KEYWORD
        self.job_search_location = NaukriJobSearchLocators.JOB_SEARCH_LOCATION
        self.job_search_experience = NaukriJobSearchLocators.JOB_SEARCH_EXPERIENCE
        self.role_category_filter = NaukriJobSearchLocators.ROLE_CATEGORY
        self.b_tech_education = NaukriJobSearchLocators.B_TECH_EDUCATION
        self.any_graduation_education = NaukriJobSearchLocators.ANY_GRADUATION_EDUCATION
        self.search_button = NaukriJobSearchLocators.SEARCH_BUTTON
        self.years_of_experience = NaukriJobSearchLocators.YEARS_OF_EXPERIENCE
        self.freshness_filter = NaukriJobSearchLocators.FILTER_FRESHNESS
        self.freshness_filter_last_single_day = NaukriJobSearchLocators.FILTER_FRESHNESS_LAST_1_DAY
        self.filters_applied = NaukriJobSearchLocators.APPLIED_FILTERS
        self.total_number_of_jobs_title = NaukriJobSearchLocators.NO_OF_JOBS

    def start_job_search(self):
        self.page.locator(self.job_search_start).click()

    def search_job(self):
        self.page.locator(self.job_search_keyword).fill(settings.JOB_SEARCH_TITLES)
        self.page.locator(self.job_search_location).fill(settings.JOB_SEARCH_LOCATIONS)
        self.page.locator(self.job_search_experience).click()
        self.page.locator(self.years_of_experience.format(
            total_years_of_experience=settings.YEARS_OF_EXPERIENCE_IN_CORE)).click()
        self.page.locator(self.search_button).click()

    def apply_freshness_filter(self):
        self.page.locator(self.freshness_filter).click()
        self.page.locator(self.freshness_filter_last_single_day).click()
        self.validate_number_of_filters_applied('2')

    def apply_role_category_filter(self):
        self.page.wait_for_selector(self.role_category_filter, state="visible")
        self.page.locator(self.role_category_filter).click(force=True)
        self.validate_number_of_filters_applied('5')

    def apply_education_filter(self):
        self.page.wait_for_selector(self.b_tech_education, state="visible")
        self.page.locator(self.b_tech_education).click(force=True)
        self.validate_number_of_filters_applied('3')
        self.page.wait_for_selector(self.any_graduation_education, state="visible")
        self.page.locator(self.any_graduation_education).click(force=True)
        self.validate_number_of_filters_applied('4')

    def validate_number_of_filters_applied(self, no_of_filters_applied):
        self.page.locator(self.filters_applied.format(number_of_filters_applied=no_of_filters_applied)).wait_for(state="visible")
        assert self.page.locator(self.filters_applied.format(number_of_filters_applied=no_of_filters_applied)).is_visible()

    def get_total_number_of_jobs(self):
        self.page.locator(self.total_number_of_jobs_title).wait_for(state="visible")
        time.sleep(2)
        job_count_text= self.page.locator(self.total_number_of_jobs_title).text_content()
        match = re.search(r'of\s+(\d+)', job_count_text)
        total_jobs = int(match.group(1))

        return total_jobs
