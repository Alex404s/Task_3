from ..pages.login_page import LoginPage
from ..pages.main_page import MainPage
from ..locators.login_page_locators import LoginPageSelectors
import allure


class TestRestorePassword:
    @allure.title('Проверка сценария "Переход на страницу восстановления пароля по кнопке «Восстановить пароль»"')
    def test_scenario_go_to_restore_password_succes(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_clickable_main_login_button()
        main_page.wait_for_invisibility_field()
        restore_pass = LoginPage(driver)
        restore_pass.scenario_go_to_restore_password()
               
        assert restore_pass.get_text_restore_password_title() == "Восстановление пароля"


    @allure.title('Проверка сценария "Ввод почты и клик по кнопке «Восстановить»"')
    def test_scenario_insert_email_and_go_to_next_menu_success(self, new_user_with_post_delete, driver):
        main_page = MainPage(driver)
        main_page.wait_for_clickable_main_login_button()        
        restore_pass = LoginPage(driver)
        restore_pass.scenario_insert_email_and_go_to_next_menu(new_user_with_post_delete[0]["user"]["email"])
               
        assert restore_pass.get_text_help_text_code_from_letter() == "Введите код из письма"

    
    @allure.title('Проверка сценария "Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его"')
    def test_scenario_click_hide_show_password_active_success(self, new_user_with_post_delete, driver):
        main_page = MainPage(driver)
        main_page.wait_for_clickable_main_login_button()
        main_page.wait_for_invisibility_field()
        restore_pass = LoginPage(driver)
        restore_pass.scenario_click_hide_show_password_active(new_user_with_post_delete[0]["user"]["email"])
                
        assert restore_pass.get_attribute_value_active_password_field() == LoginPageSelectors.active_password_field
        