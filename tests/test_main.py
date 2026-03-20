from ..pages.login_page import LoginPage
from ..pages.main_page import MainPage
from ..pages.order_feed import OrderFeed
import allure



class TestMainPage:
    @allure.title('Проверка сценария "переход по клику на «Конструктор»"')
    def test_scenario_go_to_constructor_success(self, driver):        
        main_page = MainPage(driver)
        main_page.scenario_go_to_constructor()
        check_text = main_page.get_text_constructor_title()

        assert check_text == "Соберите бургер"


    @allure.title('Проверка сценария "переход по клику на «Лента заказов»"')
    def test_scenario_go_to_order_feed_success(self, driver):
        main_page = MainPage(driver)
        main_page.scenario_go_to_order_feed()
        order_feed = OrderFeed(driver)        
        order_feed.wait_for_load_order_feed_field()
        check_text = order_feed.get_text_order_feed_field()

        assert check_text == "Выполнено за все время:"


    @allure.title('Проверка сценария "если кликнуть на ингредиент, появится всплывающее окно с деталями"')
    def test_scenario_ingredient_details_success(self, driver):
        main_page = MainPage(driver)
        main_page.scenario_ingredient_details()
        check_text = main_page.get_text_ingredient_details_title()

        assert check_text == "Детали ингредиента"

        main_page.click_close_ingredient_details_button()        
        main_page.wait_for_invisibility_field()
        main_page.click_main_login_button()
        login_page = LoginPage(driver)
        login_page.wait_for_clickable_restore_password_button()
        check_text_2 = login_page.get_text_restore_password_button()

        assert check_text_2 == "Восстановить пароль"


    @allure.title('Проверка сценария "при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента"')
    def test_scenario_add_to_order_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_invisibility_field()
        main_page.scenario_add_to_order()
        check_text = main_page.get_text_sauce_spicy_x_counter()

        assert check_text == '1'


    @allure.title('Провекра, что залогиненный пользователь может оформить заказ')
    def test_auth_user_make_login_success(self, driver, new_user_with_post_delete):
        auth_user = LoginPage(driver)
        auth_user.login_user(new_user_with_post_delete[0]["user"]["email"], new_user_with_post_delete[1])
        main_page = MainPage(driver)
        main_page.wait_for_invisibility_field()
        main_page.wait_for_clickable_register_order_button()
        check_text = main_page.get_text_register_order_button()
        assert check_text == 'Оформить заказ'


    


    
