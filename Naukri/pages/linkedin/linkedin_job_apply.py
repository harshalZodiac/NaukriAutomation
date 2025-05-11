from playwright.sync_api import Page
from config.linkedin_locators import *
import settings
import time


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
        self.review_button = REVIEW_BUTTON
        self.mandatory_not_filled_error = MANDATORY_NOT_FILLED_ERROR
        self.submit_application_button = LINKEDIN_SUBMIT_APPLICATION
        self.close_application_process = CLOSE_APPLICATION

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

        linkedin_question_answer_map = {
            "How many years of work experience do you have with Embedded Systems?": settings.YEARS_OF_EXPERIENCE_IN_NON_CORE,
            "How many years of work experience do you have with Python (Programming Language)?": settings.YEARS_OF_EXPERIENCE_IN_CORE
        }

        while True:
            try:
                if self.page.locator(self.review_button).is_visible():
                    self.page.locator(self.review_button).click()
                    time.sleep(2)
                if self.page.locator(self.submit_application_button).is_visible():
                    self.page.locator(self.submit_application_button).click()
                    time.sleep(2)
                elif self.page.locator(self.next_button).count() > 0:
                    next_btn = self.page.locator(self.next_button).first
                    next_btn.wait_for(state="visible")
                    if next_btn.is_enabled():
                        next_btn.click()
                        print("[Info] Clicked 'Next' button.")
                        time.sleep(1.5)
                    else:
                        print("[Warning] 'Next' button found but not enabled.")
                else:
                    print("[Info] No navigation button found. Exiting.")
                    break

                error_icons = self.page.locator(self.mandatory_not_filled_error)
                for i in range(error_icons.count()):
                    icon = error_icons.nth(i)
                    container = icon.locator("xpath=ancestor::div[contains(@class, 'fb-dash-form-element')]")

                    label = container.locator("label").first
                    input_field = container.locator("input, textarea").first

                    if not label.is_visible() or not input_field.is_visible():
                        continue

                    question = label.inner_text().strip()
                    answer = linkedin_question_answer_map.get(question)

                    if answer:
                        input_field.fill(answer)
                        print(f"[Info] Filled answer for: {question}")
                    else:
                        print(f"[Unmapped Question] '{question}' - Skipping this job.")
                        self.page.locator(self.close_application_process).click()
                        time.sleep(1)
                        return
                time.sleep(1.5)

            except Exception as e:
                print(f"[Error] Exception during application process: {e}")
                break
