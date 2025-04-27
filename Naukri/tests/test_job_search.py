import time
from pages.job_search_page import JobSearchPage
from pages.login_page import LoginPage


class TestNaukriJobSearch:

    def test_job_search_start(self, page):
        login_page = LoginPage(page)
        job_search_page = JobSearchPage(page)

        login_page.login()
        job_search_page.start_job_search()
        job_search_page.search_job()

    def test_apply_job_search_freshness_filter(self, page):
        login_page = LoginPage(page)
        job_search_page = JobSearchPage(page)

        login_page.login()
        job_search_page.start_job_search()
        job_search_page.search_job()
        job_search_page.apply_freshness_filter()
        time.sleep(5)
