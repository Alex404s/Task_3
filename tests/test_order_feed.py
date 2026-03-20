from ..pages.login_page import LoginPage
from ..pages.personal_acc_page import PersonalAccPage
from ..pages.main_page import MainPage
from ..pages.order_feed import OrderFeed
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
        
        check_text = order_feed.get_text_order_details_window()
        
        assert '#0' in check_text

    # @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    # def test_same_orders(self, driver):
    #     auth_user = LoginPage(driver)
    #     auth_user.login_user("zagagulka@yandex.ru", "useruser")
    #     main_page = MainPage(driver)         
    #     main_page.wait_for_clickable_register_order_button()
    #     main_page.wait_for_invisibility_field()
    #     personal_acc = PersonalAccPage(driver)
    #     personal_acc.scenario_go_to_order_story()
    #     order_1 = personal_acc.get_order_num()       
        
    #     order_feed = OrderFeed(driver)    
    #     order_feed.order_feed_button_click()        
    #     order_feed.wait_for_load_order_feed_field()
    #     main_page.wait_for_invisibility_field()
    #     order_feed.move_to_element()
    #     order_feed.scroll_my_order()
    #     order_2 = order_feed.get_text_order_2()

    #     assert order_1 == order_2






