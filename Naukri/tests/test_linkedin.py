from pages.linkedin.linkedin_profile_page import LinkedinProfilePage
from pages.linkedin.linkedin_login_page import LinkedinLoginPage
import time


class TestLinkedinLogin:

    def test_linkedin_successful_login(self, page):
        linkedin_login_page = LinkedinLoginPage(page)
        linkedin_login_page.login()
        time.sleep(5)


class TestLinkedinProfile:

    def test_linkedin_profile_section_navigation(self, page):
        linkedin_login_page = LinkedinLoginPage(page)
        linkedin_profile_page = LinkedinProfilePage(page)

        linkedin_login_page.login()
        linkedin_profile_page.view_linkedin_profile()
        time.sleep(5)

    def test_linkedin_profile_random_edit(self, page):
        linkedin_login_page = LinkedinLoginPage(page)
        linkedin_profile_page = LinkedinProfilePage(page)

        linkedin_login_page.login()
        linkedin_profile_page.view_linkedin_profile()
        linkedin_profile_page.edit_linkedin_profile()
        time.sleep(5)
