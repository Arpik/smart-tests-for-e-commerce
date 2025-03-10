# Helper functions to use across tests

import random


def select_random_option(page, selector):
    """Selects a random option from a dropdown by checking its available values."""
    options = page.locator(selector).evaluate(
        "el => [...el.options].map(o => o.textContent.trim())")
    random_choice = random.choice(options)  # Pick a random value
    print(f"Selecting option: {random_choice}")  # Debugging
    page.select_option(selector, label=random_choice)  # Select by label


def block_ads(route, request):
    # Define a list of ad-related domains or URL patterns to block
    ad_domains = ['ads', 'doubleclick', 'googlesyndication', 'adservice']

    # Check if the request URL contains any ad-related domain
    if any(domain in request.url for domain in ad_domains):
        route.abort()  # Block the request
    else:
        route.continue_()  # Allow the request