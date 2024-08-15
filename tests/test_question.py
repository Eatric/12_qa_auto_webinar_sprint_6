import pytest

from data import QuestionData
from locators.login_page_locator import LoginPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestQuestion:

    @pytest.mark.parametrize(QuestionData.param, QuestionData.value)
    def test_question(self, driver, number, expected_answer):
        driver = None
        print(LoginPageLocators.get_question_answer(number))

        #main_page = LoginPage(driver)

        #element = main_page.wait_and_find_element()

        #assert element.text == expected_answer
