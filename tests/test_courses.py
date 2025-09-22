import pytest
from playwright.sync_api import expect, Page


COURSES_LINK = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto(COURSES_LINK)

    courses_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_header).to_be_visible()

    courses_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    courses_list_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_list_title).to_be_visible()

    courses_list_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_list_description).to_be_visible()
