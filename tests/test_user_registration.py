import pytest
from playwright.sync_api import sync_playwright
from utils import data_generator
import random


# Function to select a random option from a dropdown
def select_random_option(page, selector, min_value, max_value):
    random_value = str(random.randint(min_value, max_value))  # Generate a random number within the range
    page.select_option(selector, label=random_value)  # Select the random value

def block_ads(route, request):
    # Define a list of ad-related domains or URL patterns to block
    ad_domains = ['ads', 'doubleclick', 'googlesyndication', 'adservice']
    
    # Check if the request URL contains any ad-related domain
    if any(domain in request.url for domain in ad_domains):
        route.abort()  # Block the request
    else:
        route.continue_()  # Allow the request

def test_register_user():
    with sync_playwright() as p:
        # Launch browser
        # Change headless to True for headless mode
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        test_data_generator = data_generator.TestDataGenerator()
        user_data = test_data_generator.generate_user()

        print(user_data)

        # Navigate to the URL
        page.goto('http://automationexercise.com')

        # Verify that home page is visible successfully
        # Check if the page title is visible
        assert page.is_visible('h2.title')

        # Click on 'Signup / Login' button
        page.click('a[href="/login"]')

        # Verify 'New User Signup!' is visible
        assert page.is_visible('h2:has-text("New User Signup!")')

        # Enter name and email address
        page.fill('input[name="name"]', user_data["first_name"])
        signup_email_field = page.locator('div.signup-form input[name="email"]')
        signup_email_field.fill(user_data["email"])

        # Click 'Signup' button
        page.click('button[data-qa="signup-button"]')

        # Verify that 'ENTER ACCOUNT INFORMATION' is visible
        #assert page.is_visible('h2:has-text("ENTER ACCOUNT INFORMATION")')

        # Fill details: Title, Name, Email, Password, Date of birth
        mr_radio_button = page.locator('input[type="radio"][id="id_gender1"]').click()
        page.fill('input[name="password"]', user_data["password"])

        # page.fill('input[name="days"]', '10')
        # page.fill('input[name="months"]', 'January')
        # page.fill('input[name="years"]', '1990')
            # Select random values for day (1-31), month (1-12), and year (1990-2023)
        select_random_option(page, 'select[id="days"]', 1, 31)
        page.on('route', block_ads)
        # Listen for alerts and dismiss them automatically
        page.on('popup', lambda popup: popup.close())
        select_random_option(page, 'select[id="months"]', 1, 12)
        select_random_option(page, 'select[id="years"]', 190, 2023)
        
        # Select checkbox 'Sign up for our newsletter!'
        page.check('input[name="newsletter"]')

        # Select checkbox 'Receive special offers from our partners!'
        page.check('input[name="optin"]')

        # Fill address details
        page.fill('input[name="first_name"]', 'Test')
        page.fill('input[name="last_name"]', 'User')
        page.fill('input[name="company"]', 'Test Co.')
        page.fill('input[name="address1"]', '123 Test Street')
        page.fill('input[name="address2"]', 'Suite 200')
        page.fill('input[name="country"]', 'Canada')
        page.fill('input[name="state"]', 'Ontario')
        page.fill('input[name="city"]', 'Toronto')
        page.fill('input[name="zipcode"]', 'M5V 2N8')
        page.fill('input[name="mobile_number"]', '1234567890')

        # Click 'Create Account' button
        page.click('button[data-qa="create-account"]')

        # Verify that 'ACCOUNT CREATED!' is visible
        assert page.is_visible('b:has-text("Account Created!")')

        # Click 'Continue' button
        page.click('a[data-qa="continue-button"]')

        # Verify that 'Logged in as username' is visible
        assert page.is_visible('a[href="/profile"]')

        # Click 'Delete Account' button
        page.click('a[href="/delete_account"]')

        # Verify that 'ACCOUNT DELETED!' is visible
        assert page.is_visible('h2:has-text("Account Deleted!")')

        # Click 'Continue' button
        page.click('a[data-qa="continue-button"]')

        # Close the browser
        browser.close()
