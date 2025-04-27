import time

from playwright.sync_api import Page
from config.locators import *


class JobApplyPage:
    def __init__(self, page:Page):
        self.page = page
        self.job_posts = JOB_POSTS
        self.apply_on_company_site_button = APPLY_ON_COMPANY_SITE_BUTTON

    def open_first_job_post(self, job_index):
        self.page.locator(self.job_posts).nth(job_index).click()

        # new_tab = self.page.context.pages[-1]
        new_tab = self.page.context.wait_for_event("page")
        new_tab.wait_for_load_state("load")

        time.sleep(5)
        if new_tab.locator(self.apply_on_company_site_button).first.is_visible():
            print("Apply on Company Site button found.")
            new_tab.close()

    # def check_if_external_apply_is_there(self):
    #     if self.page.locator(self.apply_on_company_site_button).is_visible():
    #         print("Found 'Apply on Company Site' button.")
