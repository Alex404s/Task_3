from ..pages.login_page import LoginPage
from ..pages.personal_acc_page import PersonalAccPage
from ..pages.main_page import MainPage
from ..pages.order_feed_page import OrderFeed
from ..helpers import *
import allure


class TestOrderFeed:
    @allure.title('Провеврка сценария "если кликнуть на заказ, откроется всплывающее окно с деталями"')
    def test_get_text_latest_order_in_list_success(self, driver):
        main_page = MainPage(driver)         
        main_page.wait_for_clickable_main_login_button()
        main_page.wait_for_invisibility_field()        
        order_feed = OrderFeed(driver)        
        order_feed.order_feed_button_click()        
        order_feed.wait_for_load_order_feed_field()
        main_page.wait_for_invisibility_field()        
        order_feed.click_latest_order_in_list()
        main_page.wait_for_invisibility_field()
        order_feed.wait_for_load_order_details_window()         
        
        assert '#0' in order_feed.get_text_order_details_window()
        

    @allure.title('Проверка сценария "заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_history_orders_in_order_feed_success(self, driver, new_user_with_post_delete):        
        auth_user = LoginPage(driver)
        auth_user.login_user(new_user_with_post_delete[0]["user"]["email"], new_user_with_post_delete[1])
        main_page = MainPage(driver)         
        main_page.wait_for_clickable_register_order_button()
        main_page.wait_for_invisibility_field()
        create_order(new_user_with_post_delete[0]['accessToken'])
        personal_acc = PersonalAccPage(driver)
        personal_acc.scenario_go_to_order_story()
        personal_acc.wait_for_load_story_order()                       
        personal_acc.order_feed_button_click()        
        order_feed = OrderFeed(driver)                       
        order_feed.wait_for_load_order_feed_field()
        order_feed.wait_for_invisibility_field()
        
        assert personal_acc.get_order_num() == order_feed.get_text_latest_order_in_list()


    @allure.title('Проверка сценария "при создании нового заказа счётчик Выполнено за всё время увеличивается"')
    def test_all_time_counter_up_success(self, driver, new_user_with_post_delete):
        order_feed = OrderFeed(driver)
        order_feed.wait_for_clickable_order_feed_button()
        order_feed.wait_for_invisibility_field()
        order_feed.order_feed_button_click()
        order_feed.wait_for_load_order_feed_field()
        order_feed.wait_for_invisibility_field()
        all_time_counter_before = int(order_feed.get_text_all_time_counter())
        create_order(new_user_with_post_delete[0]['accessToken'])
        all_time_counter_after = int(order_feed.get_text_all_time_counter())
        
        assert all_time_counter_after == all_time_counter_before +1


    @allure.title('Проверка сценария "при создании нового заказа счётчик Выполнено за сегодня увеличивается"')
    def test_today_counter_up_success(self, driver, new_user_with_post_delete):
        order_feed = OrderFeed(driver)
        order_feed.wait_for_clickable_order_feed_button()
        order_feed.wait_for_invisibility_field()
        order_feed.order_feed_button_click()
        order_feed.wait_for_load_order_feed_field()
        order_feed.wait_for_invisibility_field()
        all_time_counter_before = int(order_feed.get_text_today_counter())
        create_order(new_user_with_post_delete[0]['accessToken'])
        all_time_counter_after = int(order_feed.get_text_today_counter())
        
        assert all_time_counter_after == all_time_counter_before +1


    @allure.title('Проверка сценария "после оформления заказа его номер появляется в разделе В работе"')
    def test_order_in_progress(self, driver, new_user_with_post_delete):
        auth_user = LoginPage(driver)
        auth_user.login_user(new_user_with_post_delete[0]["user"]["email"], new_user_with_post_delete[1])
        main_page = MainPage(driver)         
        main_page.wait_for_clickable_register_order_button()
        main_page.wait_for_invisibility_field()
        create_order(new_user_with_post_delete[0]['accessToken'])
        personal_acc = PersonalAccPage(driver)
        personal_acc.scenario_go_to_order_story()
        personal_acc.wait_for_load_story_order()                      
        personal_acc.order_feed_button_click()
        order_feed = OrderFeed(driver)                       
        order_feed.wait_for_invisibility_field()
        order_feed.wait_for_load_order_number_in_work()        

        assert order_feed.get_text_order_in_work() in personal_acc.get_order_num() 


        
        






