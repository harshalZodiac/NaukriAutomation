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
            question_answer_map = {
                "How much experience do you have in Python?": settings.YEARS_OF_EXPERIENCE_IN_CORE,
                "How many years of experience you have in Selenium?": settings.YEARS_OF_EXPERIENCE_IN_CORE,
                "How many years of experience do you have in Api Automation?": settings.YEARS_OF_EXPERIENCE_IN_CORE,
                "How many years of exp in python coding": settings.YEARS_OF_EXPERIENCE_IN_CORE,
                "How many years of experience do you have in Manual Testing?": settings.YEARS_OF_EXPERIENCE_IN_CORE,
                "How many years of experience do you have in Salesforce Testing?": settings.YEARS_OF_EXPERIENCE_IN_NON_CORE,
                "How many years of experience do you have in Selenium Automation?": settings.YEARS_OF_EXPERIENCE_IN_CORE,
                "How many years of experience do you have in Javascript?": settings.YEARS_OF_EXPERIENCE_IN_NON_CORE,
                "What is your last working day?": settings.NOTICE_PERIOD,
                "How many years of experience do you have in Python?": settings.YEARS_OF_EXPERIENCE_IN_CORE,
                "How many years of Exp in Automation Python testing?": settings.YEARS_OF_EXPERIENCE_IN_CORE,
                "How many years of total experience you have?": settings.YEARS_OF_EXPERIENCE_IN_CORE,
                "What is your expected CTC in Lakhs per annum?": settings.EXPECTED_CTC,
                "Please confirm your availability for Virtual interview on 17th May 2025?": settings.ANSWER_YES,
                "How many years of experience do you have in Application Engineering?": settings.YEARS_OF_EXPERIENCE_IN_CORE,
                "Are you open to work on contract?": settings.ANSWER_YES,
                "Do you have PF in your current company?": settings.ANSWER_YES,
                "Are you currently residing in Hyderabad or willing to relocate to Hyderabad?": settings.ANSWER_YES,
                "Are you willing to work 4 days a week from Office?": settings.ANSWER_YES,
                "Are you okay to relocate to bangalore": settings.CURRENT_LOCATION_IS_BANGALORE,
                "How Many Years of exp you have in Data Engineering?": settings.YEARS_OF_EXPERIENCE_IN_CORE,
                "Expected CTC (Numeric Input Only)": settings.EXPECTED_CTC_NUMERIC,
                "What is your expected annual CTC in INR ?": settings.EXPECTED_CTC_NUMERIC,
                "Current CTC (Numeric Input Only)": settings.CURRENT_CTC_NUMERIC,
                "What is your current annual CTC in INR ?": settings.CURRENT_CTC_NUMERIC,
                "Notice Period": settings.NOTICE_PERIOD,
                "What is your notice period?": settings.NOTICE_PERIOD,
                "First Name": settings.FIRST_NAME,
                "Date of Birth": settings.DATE_OF_BIRTH,
                "Last Name": settings.LAST_NAME,
                "Current Location": settings.CURRENT_LOCATION,
                "Preferred Location": settings.CURRENT_LOCATION,
                "How many years of Experience do you have in ETL resting?": settings.YEARS_OF_EXPERIENCE_IN_NON_CORE,
                "How many years of experience do you have in Mobile Testing?  ": settings.YEARS_OF_EXPERIENCE_IN_NON_CORE,
                "How many relevant years of experience into Python development?": settings.YEARS_OF_EXPERIENCE_IN_NON_CORE
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
