import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    """Setup Playwright at the session level (runs once)."""
    with sync_playwright() as p:
        yield p  # Provide Playwright instance
        # Teardown happens automatically when exiting the context manager


@pytest.fixture(scope="session")
def browser(playwright_instance):
    """Setup browser at the session level (runs once per test session)."""
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()  # Teardown after session ends


@pytest.fixture(scope="function")
def context(browser):
    """Create a new browser context for each test (isolated session)."""
    context = browser.new_context()
    yield context
    context.close()  # Clean up after each test


@pytest.fixture(scope="function")
def page(context):
    """Create a new page for each test."""
    page = context.new_page()
    yield page
    page.close()  # Close the page after the test
