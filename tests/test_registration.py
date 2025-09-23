import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

email = 'user.name@gmail.com'
password = 'password'
username = 'username'


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email=email, username= username, password=password)
    registration_page.click_registration_button()

    dashboard_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_page.dashboard_title_check()

