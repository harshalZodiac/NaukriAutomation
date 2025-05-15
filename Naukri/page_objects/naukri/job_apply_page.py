from playwright.sync_api import Page
from config.locators_naukri import *
from utils.helpers import *
import settings
import time


class NaukriJobApplyPage:
    def __init__(self, page:Page):
        self.page = page
        self.job_posts = NaukriJobApplicationLocators.JOB_POSTS
        self.apply_on_company_site_button = NaukriJobApplicationLocators.APPLY_ON_COMPANY_SITE_BUTTON
        self.naukri_internal_apply = NaukriJobApplicationLocators.NAUKRI_INTERNAL_APPLY_BUTTON
        self.answer_placeholder = NaukriJobApplicationLocators.ANSWER_PLACEHOLDER
        self.job_already_applied = NaukriJobApplicationLocators.JOB_ALREADY_APPLIED
        self.job_apply_pagination = NaukriJobApplicationLocators.JOB_APPLY_PAGINATION
        self.internal_job_apply_success = NaukriJobApplicationLocators.JOB_APPLY_SUCCESS
        self.question_placeholder = NaukriJobApplicationLocators.QUESTION_PLACEHOLDER
        self.i_am_interested = NaukriJobApplicationLocators.I_AM_INTERESTED

    def apply_for_job(self, job_index):
        with self.page.context.expect_page() as new_tab_info:
            self.page.locator(self.job_posts).nth(job_index).wait_for(state="visible", timeout=10000)
            self.page.locator(self.job_posts).nth(job_index).click()
        new_tab = new_tab_info.value
        new_tab.wait_for_load_state("load")

        time.sleep(2)
        if new_tab.locator(self.apply_on_company_site_button).first.is_visible():
            external_url = new_tab.url
            save_external_link(external_url)
            new_tab.close()
            return
        if new_tab.locator(self.i_am_interested).first.is_visible():
            new_tab.locator(self.i_am_interested).first.click(force=True)
            time.sleep(2)
        if new_tab.locator(self.naukri_internal_apply).first.is_visible():
            new_tab.locator(self.naukri_internal_apply).first.click(force=True)
            time.sleep(2)

            while True:
                try:
                    question_locator = new_tab.locator(self.question_placeholder).last
                    answer_box = new_tab.locator(self.answer_placeholder).first

                    if not question_locator.is_visible():
                        break

                    question_text = question_locator.inner_text().strip()
                    answer = settings.question_answer_map.get(question_text)

                    if question_text == "Thank you for your responses.":
                        print("[Info] End of section detected.")
                        break

                    if answer:
                        answer_box.fill(answer)
                        time.sleep(0.5)
                        new_tab.keyboard.press("Enter")
                        time.sleep(1.5)
                    else:
                        print(f"[Warning] Unmapped question: {question_text}")
                        break

                except Exception as e:
                    print(f"Error while handling dynamic questions: {e}")
                    break
            if new_tab.locator(self.internal_job_apply_success).is_visible():
                new_tab.close()
