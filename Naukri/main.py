import time
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page()

    login = LoginPage(page)
    login.login()
    time.sleep(5)
    browser.close()
