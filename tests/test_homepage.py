def test_open_homepage(browser, page):
    # Navigate to the base URL
    base_url = "https://demo.opencart.com"
    page.goto(base_url)

    # Assert the page title
    assert "Your Store" in page.title()
