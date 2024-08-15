from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, '//*[@id="email"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')

    ENTER_BUTTON = (By.XPATH, '//button[text() = ""]')

    @staticmethod
    def button_by_text(var):
        return By.XPATH, f'//button[text() = "{var}"]'

    @staticmethod
    def get_question_answer(question_number):
        return By.XPATH, f'//button[text() = "{question_number}"]'
