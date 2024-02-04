from selene import browser, by, command, have

from data.user_data import User
from picture import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_form(self, user: User):
        browser.element('#firstName').type(user.name)
        browser.element('#lastName').type(user.lastname)
        browser.element('#userEmail').type(user.email)
        browser.element('.custom-control').click()
        browser.element('#userNumber').type(user.phone)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(by.text(user.birthday_year)).click()
        browser.element('.react-datepicker__month-select').click().element(by.text(user.birthday_month)).click()
        browser.element(f'.react-datepicker__day--0{user.birthday_day}').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#uploadPicture').send_keys(resource.path('rus.jpg'))
        browser.element('#currentAddress').type(user.address)
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.element('#react-select-3-option-0').click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-1').click()
        browser.element('#submit').perform(command.js.click)

    def should_registered(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.name} {user.lastname}',
            user.email,
            user.gender,
            user.phone,
            f'{user.birthday_day} {user.birthday_month},{user.birthday_year}',
            user.subject,
            user.hobby,
            user.picture,
            user.address,
            f'{user.state} {user.city}'
        ))