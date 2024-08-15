from locators.main_page_locator import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def get_current_user(self, user_name):
        current_user = self.wait_text_and_find_element(MainPageLocators.USER_NAME, user_name)

        return current_user.text
