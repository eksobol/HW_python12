import os

from selene import browser, be, have

CURRENT_FILE = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(CURRENT_FILE)
FILE = os.path.join(DIRECTORY, "..", "resources")


class RegistrationStudent:

    def open(self, value):
        browser.open(value)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value).press_enter()

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value).press_enter()

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value).press_enter()

    def fill_gender(self):
        browser.element('label[for=gender-radio-2]').click()

    def fill_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value).click()

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'[value = "{month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value = "{year}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobby(self):
        browser.element('label[for=hobbies-checkbox-1]').click()
        browser.element('label[for=hobbies-checkbox-3]').click()

    def fill_image(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f"{FILE}/{value}"))

    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value).press_enter()

    def fill_state_and_city(self):
        browser.element('#state').click()
        browser.element('//*[text()="Uttar Pradesh"]').click()
        browser.element('#city').click()
        browser.element('//*[text()="Merrut"]').click()

    def fill_submit(self):
        browser.element('#submit').click()

    def shoud_have_text(self, name, email, gender, mobile, date, subject, hobbies, picture, address, state):
        browser.element('//table//td[contains(text(),"Student Name")]/../td[2]').should(have.text(name))
        browser.element('//table//td[contains(text(),"Student Email")]/../td[2]').should(have.text(email))
        browser.element('//table//td[contains(text(),"Gender")]/../td[2]').should(have.text(gender))
        browser.element('//table//td[contains(text(),"Mobile")]/../td[2]').should(have.text(mobile))
        browser.element('//table//td[contains(text(),"Date of Birth")]/../td[2]').should(have.text(date))
        browser.element('//table//td[contains(text(),"Subjects")]/../td[2]').should(have.text(subject))
        browser.element('//table//td[contains(text(),"Hobbies")]/../td[2]').should(have.text(hobbies))
        browser.element('//table//td[contains(text(),"Picture")]/../td[2]').should(have.text(picture))
        browser.element('//table//td[contains(text(),"Address")]/../td[2]').should(have.text(address))
        browser.element('//table//td[contains(text(),"State and City")]/../td[2]').should(
            have.text(state))
