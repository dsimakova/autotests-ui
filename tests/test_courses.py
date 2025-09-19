from playwright.sync_api import sync_playwright, expect


REGISTRATION_LINK = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
COURSES_LINK = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(REGISTRATION_LINK)

        registration_button = page.get_by_test_id('registration-page-registration-button')
        expect(registration_button).to_be_disabled()

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')


    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto(COURSES_LINK)

        courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_header).to_be_visible()

        courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_icon).to_be_visible()

        courses_list_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_list_title).to_be_visible()

        courses_list_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_list_description).to_be_visible()