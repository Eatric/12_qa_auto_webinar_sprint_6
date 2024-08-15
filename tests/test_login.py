import allure

from data import AuthData, MainData, Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLogin:

    @allure.title('Проверка авторизации')
    @allure.description('Авторизуемся под тестовым пользователм и проверяем что авторизовались именно под ним')
    def test_success_authorization(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.MAIN_PAGE)

        login_page.set_email_input(AuthData.LOGIN)
        login_page.set_password_input(AuthData.PASSWORD)
        login_page.click_auth_button()

        main_page = MainPage(driver)

        assert main_page.get_current_user(MainData.USER_NAME) == MainData.USER_NAME, ('Имя пользователя не '
                                                                                      'соответствует ожидаемому')
