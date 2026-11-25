![Tests](https://github.com/inkeiter/saucedemo-ai-e2e/actions/workflows/tests.yml/badge.svg)
# saucedemo-ai-e2e

> 🇷🇺 Русская версия: [README.ru.md](README.ru.md)

A small set of E2E tests for the [Sauce Demo](https://www.saucedemo.com/) practice site, written with Python, Playwright, and pytest. The project also demonstrates using AI as an assistant when creating and reviewing automated tests.

## Test goals

**Test 1 (`test_successful_login`).** Verify that a user can log in with valid credentials and reach the products page:

1. Open the login page.
2. Enter the username `standard_user`.
3. Enter the password `secret_sauce`.
4. Click the **Login** button.
5. Check that the products page opens and its title is `Products`.

**Test 2 (`test_login_with_wrong_password_shows_error`)** is a negative scenario. Verify that a user with a wrong password does not log in and sees an error message:

1. Open the login page.
2. Enter the username `standard_user` and a wrong password.
3. Click the **Login** button.
4. Check the error text and that the user stays on the login page.

## Tech stack

- Python 3
- [Playwright for Python](https://playwright.dev/python/)
- [pytest](https://docs.pytest.org/) with the `pytest-playwright` plugin (provides the `page` fixture)
- GitHub Actions for CI

## Environment requirements

- macOS
- Python 3.9 or newer (`python3 --version`)
- Internet access (the tests run against the public Sauce Demo site)

## Setup (macOS)

```bash
# 1. Create a virtual environment
python3 -m venv .venv

# 2. Activate it
source .venv/bin/activate

# 3. Install dependencies
python -m pip install -r requirements.txt

# 4. Install the Chromium browser for Playwright
python -m playwright install chromium
```

## Running the tests

```bash
# Run the tests (headless Chromium)
python -m pytest

# Verbose output
python -m pytest -v

# Run with a visible browser
python -m pytest --headed --slowmo 500
```

## Example of expected output

A successful run looks roughly like this (versions, paths, and timing will differ):

```text
tests/test_login.py::test_successful_login PASSED                        [ 50%]
tests/test_login.py::test_login_with_wrong_password_shows_error PASSED   [100%]

============================== 2 passed in X.XXs ===============================
```

## Project structure

```text
saucedemo-ai-e2e/
├── tests/
│   └── test_login.py        # two E2E tests: successful login and login with a wrong password
├── .github/workflows/
│   └── tests.yml            # CI: runs pytest on push and pull request
├── requirements.txt         # Python dependencies
├── .gitignore
├── README.md                # this file (English)
└── README.ru.md             # Russian version
```

A Page Object layer, `conftest.py`, and configuration files are deliberately not used here: for such a small number of scenarios they would add code without practical benefit.

## What the assertions check

- `expect(page).to_have_url(...)` — the browser navigated to `/inventory.html`, so the login was accepted.
- `expect(page.locator(".title")).to_have_text("Products")` — the page is actually the products page, not just a similar-looking URL.

For the negative test:

- `expect(page.locator('[data-test="error"]')).to_have_text(...)` — the site showed the expected error message.
- `expect(page).to_have_url(BASE_URL)` — the user stayed on the login page.

All checks use Playwright's auto-waiting `expect`, so no `sleep` is needed.

## Limitations

- Only a successful login and a login with a wrong password are covered. Empty fields, a locked-out user, and other scenarios are not checked.
- The error text is checked exactly, so the test will fail if the site changes the wording.
- The tests run against a third-party public site. If the site is unavailable or its markup changes, a test may fail for reasons unrelated to your code.
- Only Chromium is used.
- Dependencies are specified with minimum versions and are not pinned exactly.

## AI-assisted development

AI (Claude) was used to prepare the tests, `requirements.txt`, the GitHub Actions workflow, and this README. The locators were taken from publicly available examples for Sauce Demo. AI is only a development aid here: there is no AI model in the test runtime, and a human must review and run all the code before trusting it.
