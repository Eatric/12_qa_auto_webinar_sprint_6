import allure

from locators.login_page_locator import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Заполняем поле Email')
    def set_email_input(self, email):
        login_input = self.wait_and_find_element(LoginPageLocators.EMAIL_FIELD)
        login_input.send_keys(email)

    @allure.step('Заполняем поле Password')
    def set_password_input(self, password):
        password_input = self.wait_and_find_element(LoginPageLocators.PASSWORD_FIELD)
        password_input.send_keys(password)

    @allure.step('Нажимаем кнопку войти')
    def click_auth_button(self):
        button = self.wait_and_find_element(LoginPageLocators.button_by_text('Войти'))
        button.click()

    def auth(self, email, password):
        self.set_email_input(email)
        self.set_password_input(password)
        self.click_auth_button()

