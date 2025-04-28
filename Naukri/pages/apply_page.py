import time
from playwright.sync_api import Page
from config.locators import *
from config import settings

class JobApplyPage:
    def __init__(self, page:Page):
        self.page = page
        self.job_posts = JOB_POSTS
        self.apply_on_company_site_button = APPLY_ON_COMPANY_SITE_BUTTON
        self.naukri_internal_apply = NAUKRI_INTERNAL_APPLY_BUTTON
        self.question_1 = QUESTION_1
        self.question_2 = QUESTION_2
        self.question_3 = QUESTION_3
        self.question_4 = QUESTION_4
        self.answer_placeholder = ANSWER_PLACEHOLDER
        self.job_already_applied = JOB_ALREADY_APPLIED
        self.job_apply_pagination = JOB_APPLY_PAGINATION

    def open_first_job_post(self, job_index):
        self.page.locator(self.job_posts).nth(job_index).click()

        new_tab = self.page.context.wait_for_event("page")
        new_tab.wait_for_load_state("load")

        time.sleep(2)
        if new_tab.locator(self.apply_on_company_site_button).first.is_visible():
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
        if new_tab.locator(self.job_already_applied).first.is_visible():
            new_tab.close()
