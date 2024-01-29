from data.user_data import user
from page.registration_page_high import RegistrationPage


def test_registration_demo_qa():
    registration = RegistrationPage()
    registration.open()
    registration.fill_form(user)
    registration.should_registered(user)


