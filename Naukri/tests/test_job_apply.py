import time

from pages.apply_page import JobApplyPage
from pages.job_search_page import JobSearchPage
from pages.login_page import LoginPage


class TestNaukriJobApply:

    def test_apply_first_twenty_jobs(self, page):
        login_page = LoginPage(page)
        job_search_page = JobSearchPage(page)
        job_apply_page = JobApplyPage(page)

        login_page.login()
        job_search_page.start_job_search()
        job_search_page.search_job()
        job_search_page.apply_freshness_filter()
        page_number = page.locator(job_apply_page.job_apply_pagination)
        for j in range(4):
            page_number.nth(j).click()
            time.sleep(3)
            for i in range(-1, 20):
                job_apply_page.open_first_job_post(i)
                time.sleep(2)
