from page_objects.naukri.job_search_page import NaukriJobSearchPage
from page_objects.naukri.profile_page import NaukriProfilePage
from page_objects.naukri.job_apply_page import NaukriJobApplyPage
from page_objects.naukri.login_page import NaukriLoginPage
import settings
import time
import math

class TestNaukriLogin:

    def test_naukri_successful_login(self, browser_page):
        login_page = NaukriLoginPage(browser_page)
        login_page.login()

    def test_naukri_view_profile(self, browser_page):
        login_page = NaukriLoginPage(browser_page)
        profile_page = NaukriProfilePage(browser_page)

        login_page.login()
        profile_page.view_profile()
        name = profile_page.get_profile_name()
        assert name == settings.USER_FULL_NAME

    def test_profile_percentage_value(self, browser_page):
        login_page = NaukriLoginPage(browser_page)
        profile_page = NaukriProfilePage(browser_page)

        login_page.login()
        profile_page.view_profile()
        name = profile_page.get_profile_name()
        assert name == settings.USER_FULL_NAME
        percentage_value = profile_page.get_profile_percentage_value()
        assert int(percentage_value) >= 90, f"Profile completion is only {percentage_value}%. Please update!"

    def test_update_profile_general_section(self, browser_page):
        login_page = NaukriLoginPage(browser_page)
        profile_page = NaukriProfilePage(browser_page)

        login_page.login()
        profile_page.view_profile()
        profile_page.edit_general_profile_section()

class TestNaukriJobSearch:

    def test_job_search_start(self, browser_page):
        login_page = NaukriLoginPage(browser_page)
        job_search_page = NaukriJobSearchPage(browser_page)

        login_page.login()
        job_search_page.start_job_search()
        job_search_page.search_job()

    def test_apply_job_search_freshness_filter(self, browser_page):
        login_page = NaukriLoginPage(browser_page)
        job_search_page = NaukriJobSearchPage(browser_page)

        login_page.login()
        job_search_page.start_job_search()
        job_search_page.search_job()
        job_search_page.apply_freshness_filter()
        time.sleep(5)

class TestNaukriJobApply:

    def test_naukri_apply(self, browser_page):
        login_page = NaukriLoginPage(browser_page)
        job_search_page = NaukriJobSearchPage(browser_page)
        job_apply_page = NaukriJobApplyPage(browser_page)

        login_page.login()
        job_search_page.start_job_search()
        job_search_page.search_job()
        job_search_page.apply_freshness_filter()
        job_search_page.apply_education_filter()
        job_search_page.apply_role_category_filter()
        total_jobs = job_search_page.get_total_number_of_jobs()
        total_pages = math.ceil(total_jobs/20)
        second_last_page = total_pages - 1
        last_page_jobs = (total_jobs - (second_last_page * 20))

        page_number = browser_page.locator(job_apply_page.job_apply_pagination)
        for page_no in range((second_last_page + 1)):
            page_number.nth(page_no).click()
            time.sleep(3)
            if page_no == second_last_page:
                jobs_per_page = last_page_jobs
            else:
                jobs_per_page = 20
            for i in range(jobs_per_page):
                job_apply_page.apply_for_job(i)
                time.sleep(2)