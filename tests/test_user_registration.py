from playwright.sync_api import sync_playwright
from utils import data_generator
from utils.helpers import select_random_option, block_ads

def test_register_user():
    with sync_playwright() as p:
        # Launch browser
        # Change headless to True for headless mode
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        test_data_generator = data_generator.TestDataGenerator()
        user_data = test_data_generator.generate_ai_user()

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
        page.fill('div.signup-form input[name="email"]', user_data["email"])

        # Click 'Signup' button
        page.click('button[data-qa="signup-button"]')

        # Verify that 'ENTER ACCOUNT INFORMATION' is visible
        # assert page.is_visible('h2:has-text("ENTER ACCOUNT INFORMATION")')

        # Fill details: Title, Name, Email, Password, Date of birth
        page.locator('input[type="radio"][id="id_gender1"]').click()
        
        page.fill('input[name="password"]', user_data["password"])
        select_random_option(page, 'select[id="days"]')
        page.on('route', block_ads)
        page.mouse.wheel(0, 500)  # Scroll down by 500 units

        select_random_option(page, 'select[id="months"]')
        select_random_option(page, 'select[id="years"]')

        # Select checkbox 'Sign up for our newsletter!'
        page.check('input[name="newsletter"]')

        # Select checkbox 'Receive special offers from our partners!'
        page.check('input[name="optin"]')

        # Fill address details
        page.fill('input[name="first_name"]', user_data["first_name"])
        page.fill('input[name="last_name"]', user_data["last_name"])
        page.fill('input[name="company"]', user_data["company"])
        page.fill('input[name="address1"]', user_data["address1"])
        page.fill('input[name="address2"]', user_data["address2"])
        select_random_option(page, 'select[id="country"]')
        page.fill('input[name="state"]', user_data["state"])
        page.fill('input[name="city"]', user_data["city"])
        page.fill('input[name="zipcode"]', user_data["zipcode"])
        page.fill('input[name="mobile_number"]', user_data["phonenumber"])

        # Click 'Create Account' button
        page.click('button[data-qa="create-account"]')

        # Verify that 'ACCOUNT CREATED!' is visible
        assert page.is_visible('b:has-text("Account Created!")')

        # Close the browser
        browser.close()

  
