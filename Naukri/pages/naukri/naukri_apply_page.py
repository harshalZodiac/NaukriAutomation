from playwright.sync_api import Page
from config.naukri_locators import *
from utils.helpers import *
import settings
import time


class NaukriJobApplyPage:
    def __init__(self, page:Page):
        self.page = page
        self.job_posts = JOB_POSTS
        self.apply_on_company_site_button = APPLY_ON_COMPANY_SITE_BUTTON
        self.naukri_internal_apply = NAUKRI_INTERNAL_APPLY_BUTTON
        self.answer_placeholder = ANSWER_PLACEHOLDER
        self.job_already_applied = JOB_ALREADY_APPLIED
        self.job_apply_pagination = JOB_APPLY_PAGINATION
        self.internal_job_apply_success = JOB_APPLY_SUCCESS
        self.question_placeholder = QUESTION_PLACEHOLDER
        self.i_am_interested = I_AM_INTERESTED
        # self.question_1 = QUESTION_1
        # self.question_2 = QUESTION_2
        # self.question_3 = QUESTION_3
        # self.question_4 = QUESTION_4

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
        if new_tab.locator(self.i_am_interested).first.is_visible():
            new_tab.locator(self.i_am_interested).first.click(force=True)
            time.sleep(2)
        if new_tab.locator(self.naukri_internal_apply).first.is_visible():
            new_tab.locator(self.naukri_internal_apply).first.click(force=True)
            time.sleep(2)
            question_answer_map = {
                "How much experience do you have in Python?": settings.YEARS_OF_EXPERIENCE_IN_PYTHON,
                "How many years of Exp in Automation Python testing?": settings.YEARS_OF_EXPERIENCE_IN_PYTHON_AUTOMATION,
                "How many years of total experience you have?": settings.TOTAL_YEARS_OF_EXPERIENCE,
                "What is your expected CTC in Lakhs per annum?": settings.EXPECTED_CTC,
                "Please confirm your availability for Virtual interview on 17th May 2025?": settings.ANSWER_YES,
                "How many years of experience do you have in Application Engineering?": settings.TOTAL_YEARS_OF_EXPERIENCE,
                "Are you open to work on contract?": settings.ANSWER_YES,
                "How Many Years of exp you have in Data Engineering?": settings.TOTAL_YEARS_OF_EXPERIENCE,
                "Expected CTC (Numeric Input Only)": settings.EXPECTED_CTC_NUMERIC,
                "Current CTC (Numeric Input Only)": settings.CURRENT_CTC_NUMERIC,
                "Notice Period": settings.NOTICE_PERIOD,
                "First Name": settings.FIRST_NAME,
                "Last Name": settings.LAST_NAME,
                "Current Location": settings.CURRENT_LOCATION,
                "Preferred Location": settings.CURRENT_LOCATION,
                "How many years of Experience do you have in ETL resting?  ": settings.YEARS_OF_EXPERIENCE_IN_ETL,
                "Your KCET Rank: (Mention NA if not applicable)": settings.ANSWER_NOT_APPLICABLE
            }

            while True:
                try:
                    question_locator = new_tab.locator(self.question_placeholder).last
                    answer_box = new_tab.locator(self.answer_placeholder).first

                    if not question_locator.is_visible():
                        break

                    question_text = question_locator.inner_text().strip()
                    answer = question_answer_map.get(question_text)

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
