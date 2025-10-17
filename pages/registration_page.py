from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from elements.text import Text


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page, 'registration-page-registration-button', "Registration")
        self.login_link = Link(page, 'registration-page-login-link', "Login")
        self.wrong_user_already_exists_alert = Text(page, 'registration-page-user-already-exists-alert', "Wrong User")

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()

    def check_visible_wrong_user_already_exists_alert(self):
        self.wrong_user_already_exists_alert.check_visible()
        self.wrong_user_already_exists_alert.check_have_text("User already exists")
