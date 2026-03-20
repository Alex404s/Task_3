from ..pages.personal_acc_page import PersonalAccPage
from ..pages.login_page import LoginPage
from ..pages.main_page import MainPage
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
        check_text = personal_acc.get_text_order_story_button()

        assert check_text == "История заказов"

    
    @allure.title('Проверка сценария "Переход в раздел «История заказов»"')
    def test_scenario_go_to_order_story_success(self, new_user_with_post_delete, driver):
        auth_user = LoginPage(driver)
        auth_user.login_user(new_user_with_post_delete[0]["user"]["email"], new_user_with_post_delete[1])
        main_page = MainPage(driver)
        main_page.wait_for_clickable_register_order_button()
        main_page.wait_for_invisibility_field()
        personal_acc = PersonalAccPage(driver)
        personal_acc.scenario_go_to_order_story()
        check_value = personal_acc.get_attribute_value_active_order_story_button()     

        assert check_value == 'Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9'
