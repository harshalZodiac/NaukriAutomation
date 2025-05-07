from playwright.sync_api import Page
from config.locators import *
from utils.helpers import *
import settings
import time


class JobApplyPage:
    def __init__(self, page:Page):
        self.page = page
        self.job_posts = JOB_POSTS
        self.apply_on_company_site_button = APPLY_ON_COMPANY_SITE_BUTTON
        self.naukri_internal_apply = NAUKRI_INTERNAL_APPLY_BUTTON
        self.answer_placeholder = ANSWER_PLACEHOLDER
        self.job_already_applied = JOB_ALREADY_APPLIED
        self.job_apply_pagination = JOB_APPLY_PAGINATION
        self.internal_job_apply_success = JOB_APPLY_SUCCESS
        self.question_1 = QUESTION_1
        self.question_2 = QUESTION_2
        self.question_3 = QUESTION_3
        self.question_4 = QUESTION_4

    def apply_for_job(self, job_index):
        with self.page.context.expect_page() as new_tab_info:
            self.page.locator(self.job_posts).nth(job_index).click()
        new_tab = new_tab_info.value
        new_tab.wait_for_load_state("load")

        time.sleep(2)
        if new_tab.locator(self.apply_on_company_site_button).first.is_visible():
            external_url = new_tab.url
            save_external_link(external_url)
            new_tab.close()
            return
        if new_tab.locator(self.naukri_internal_apply).first.is_visible():
            new_tab.locator(self.naukri_internal_apply).first.click(force=True)
            time.sleep(2)
            if new_tab.locator(self.question_1).is_visible():
                new_tab.locator(self.answer_placeholder).fill(settings.YEARS_OF_EXPERIENCE_IN_PYTHON)
                time.sleep(1)
                new_tab.keyboard.press("Enter")
                time.sleep(2)
            if new_tab.locator(self.question_2).is_visible():
                new_tab.locator(self.answer_placeholder).fill(settings.YEARS_OF_EXPERIENCE_IN_PYTHON_AUTOMATION)
                time.sleep(1)
                new_tab.keyboard.press("Enter")
                time.sleep(2)
            if new_tab.locator(self.question_3).is_visible():
                new_tab.locator(self.answer_placeholder).fill(settings.TOTAL_YEARS_OF_EXPERIENCE)
                time.sleep(1)
                new_tab.keyboard.press("Enter")
                time.sleep(2)
            if new_tab.locator(self.question_4).is_visible():
                new_tab.locator(self.answer_placeholder).fill(settings.EXPECTED_CTC)
                time.sleep(1)
                new_tab.keyboard.press("Enter")
                time.sleep(2)
            if new_tab.locator(self.internal_job_apply_success).is_visible():
                new_tab.close()
