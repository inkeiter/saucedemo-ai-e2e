import re

from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"

# Public demo credentials, listed on the login page itself.
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_successful_login(page: Page) -> None:
    page.goto(BASE_URL)

    # data-test attributes are intended for testing and are more stable than CSS classes.
    page.locator('[data-test="username"]').fill(USERNAME)
    page.locator('[data-test="password"]').fill(PASSWORD)
    page.locator('[data-test="login-button"]').click()

    # expect() auto-retries until the condition is met or the timeout expires.
    expect(page).to_have_url(re.compile(r"/inventory\.html$"))
    expect(page.locator(".title")).to_have_text("Products")
