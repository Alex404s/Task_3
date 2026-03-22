from ..pages.login_page import LoginPage
from ..pages.main_page import MainPage
from ..pages.order_feed_page import OrderFeed
from ..locators.login_page_locators import LoginPageSelectors
from ..locators.main_page_locators import MainPageSelectors
from ..locators.order_feed_locators import OrderFeedSelectors
import allure



class TestMainPage:
    @allure.title('Проверка сценария "переход по клику на «Конструктор»"')
    def test_scenario_go_to_constructor_success(self, driver):        
        main_page = MainPage(driver)
        main_page.scenario_go_to_constructor()        

        assert main_page.get_text_constructor_title() == MainPageSelectors.constructor_title_text


    @allure.title('Проверка сценария "переход по клику на «Лента заказов»"')
    def test_scenario_go_to_order_feed_success(self, driver):
        main_page = MainPage(driver)
        main_page.scenario_go_to_order_feed()
        order_feed = OrderFeed(driver)        
        order_feed.wait_for_load_order_feed_field()         

        assert order_feed.get_text_all_time_counter_title() == OrderFeedSelectors.all_time_counter_title_text


    @allure.title('Проверка сценария "если кликнуть на ингредиент, появится всплывающее окно с деталями"')
    def test_scenario_ingredient_details_window_success(self, driver):
        main_page = MainPage(driver)
        main_page.scenario_ingredient_details()         

        assert main_page.get_text_ingredient_details_title() == MainPageSelectors.ingredient_details_title_text


    @allure.title('Проверка закрытия всплывающего окна с деталями')
    def test_close_ingredient_details_window_success(self, driver):
        main_page = MainPage(driver)
        main_page.scenario_ingredient_details()
        main_page.click_close_ingredient_details_button()        
        main_page.wait_for_invisibility_field()
        main_page.click_main_login_button()
        login_page = LoginPage(driver)
        login_page.wait_for_clickable_restore_password_button()        

        assert login_page.get_text_restore_password_button() == LoginPageSelectors.restore_password_button_text    


    @allure.title('Проверка сценария "при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента"')
    def test_scenario_add_to_order_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_invisibility_field()
        main_page.scenario_add_to_order()         

        assert main_page.get_text_sauce_spicy_x_counter() == MainPageSelectors.sauce_spicy_x_counter_text


    @allure.title('Провекра, что залогиненный пользователь может оформить заказ')
    def test_auth_user_make_login_success(self, driver, new_user_with_post_delete):
        auth_user = LoginPage(driver)
        auth_user.login_user(new_user_with_post_delete[0]["user"]["email"], new_user_with_post_delete[1])
        main_page = MainPage(driver)
        main_page.wait_for_invisibility_field()
        main_page.wait_for_clickable_register_order_button()
        
        assert main_page.get_text_register_order_button() == MainPageSelectors.register_order_button_text


    


    
