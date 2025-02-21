# Import the logger
from utils.log_config import logger

def test_homepage_title(page):
    logger.info("Navigating to the homepage")  # Log before action
    page.goto("https://www.automationexercise.com/")

    title = page.title()
    logger.info(f"Page title retrieved: {title}")  # Log retrieved title

    assert "Automation Exercise" in title, "Title does not match expected value"
    logger.info("Test Passed ✅")
