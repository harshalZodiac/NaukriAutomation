import settings
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class TestNaukriLogin:

    def test_naukri_successful_login(self, page):
        login_page = LoginPage(page)
        login_page.login()

    def test_naukri_view_profile(self, page):
        login_page = LoginPage(page)
        profile_page = ProfilePage(page)

        login_page.login()
        profile_page.view_profile()
        name = profile_page.get_profile_name()
        assert name == settings.USER_FULL_NAME

    def test_profile_percentage_value(self, page):
        login_page = LoginPage(page)
        profile_page = ProfilePage(page)

        login_page.login()
        profile_page.view_profile()
        name = profile_page.get_profile_name()
        assert name == settings.USER_FULL_NAME
        percentage_value = profile_page.get_profile_percentage_value()
        assert int(percentage_value) >= 90, f"Profile completion is only {percentage_value}%. Please update!"
