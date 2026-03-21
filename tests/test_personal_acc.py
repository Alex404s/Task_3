from ..pages.personal_acc_page import PersonalAccPage
from ..pages.login_page import LoginPage
from ..pages.main_page import MainPage
from ..locators.personal_acc_page_locators import PersonalAccSelectors
import allure


class TestPersonalAcc:
    @allure.title('Проверка сценария "Переход по клику на «Личный кабинет»"')
    def test_scenario_go_to_personal_acc_success(self, new_user_with_post_delete, driver):
        auth_user = LoginPage(driver)
        auth_user.login_user(new_user_with_post_delete[0]["user"]["email"], new_user_with_post_delete[1])
        main_page = MainPage(driver)
        main_page.wait_for_clickable_register_order_button()
        main_page.wait_for_invisibility_field()
        personal_acc = PersonalAccPage(driver)
        personal_acc.scenario_go_to_personal_acc()        

        assert personal_acc.get_text_order_story_button() == "История заказов"

    
    @allure.title('Проверка сценария "Переход в раздел «История заказов»"')
    def test_scenario_go_to_order_story_success(self, new_user_with_post_delete, driver):
        auth_user = LoginPage(driver)
        auth_user.login_user(new_user_with_post_delete[0]["user"]["email"], new_user_with_post_delete[1])
        main_page = MainPage(driver)
        main_page.wait_for_clickable_register_order_button()
        main_page.wait_for_invisibility_field()
        personal_acc = PersonalAccPage(driver)
        personal_acc.scenario_go_to_order_story()        

        assert personal_acc.get_attribute_value_active_order_story_button() == PersonalAccSelectors.active_order_story_button

    
    @allure.title('Проверка сценария "Выход из аккаунта"')
    def test_scenario_acc_exit_success(self, new_user_with_post_delete, driver):
        auth_user = LoginPage(driver)
        auth_user.login_user(new_user_with_post_delete[0]["user"]["email"], new_user_with_post_delete[1])
        main_page = MainPage(driver)
        main_page.wait_for_clickable_register_order_button()
        main_page.wait_for_invisibility_field()
        personal_acc = PersonalAccPage(driver)
        personal_acc.scenario_acc_exit()
        login = LoginPage(driver)
        login.wait_for_clickable_restore_password_button()
        login.wait_for_invisibility_field()                

        assert login.get_text_restore_password_button() == 'Восстановить пароль'