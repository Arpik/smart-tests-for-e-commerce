from playwright.sync_api import sync_playwright


def test_open_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://demo.opencart.com")
        assert "Your Store" in page.title()
        browser.close()
