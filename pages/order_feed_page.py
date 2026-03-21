from .base_page import BasePage
from ..locators.order_feed_locators import OrderFeedLocators
import allure

class OrderFeed(BasePage):
    @allure.step('Ожидание отображения страницы "Лента заказов"')
    def wait_for_load_order_feed_field(self):
        self.wait_for_load_element(OrderFeedLocators.order_feed_field)         
    
    
    @allure.step('Получение текста заголовка "Выполнено за все время:"')
    def get_text_all_time_counter_title(self):
        text = self.get_text_element(OrderFeedLocators.order_feed_field)
        return text
    

    @allure.step('Получение значения "Выполнено за все время:"')
    def get_text_all_time_counter(self):
        text = self.get_text_element(OrderFeedLocators.counter_pass_all_time)
        return text
    

    @allure.step('Получение значения "Выполнено за сегодня:"')
    def get_text_today_counter(self):
        text = self.get_text_element(OrderFeedLocators.counter_pass_today)
        return text
    

    @allure.step('Ожидание появления номера заказа в работе после его создания')
    def wait_for_load_order_number_in_work(self):
        self.wait_for_load_element(OrderFeedLocators.number_order_in_work)


    @allure.step('Получение номера заказа в работе')
    def get_text_order_in_work(self):
        text = self.get_text_element(OrderFeedLocators.number_order_in_work)
        return text
    

    @allure.step('Нажатие по последнему заказу')
    def click_latest_order_in_list(self):
        self.click_button(OrderFeedLocators.latest_order_in_list)


    @allure.step('Получение номера последнего заказа')
    def get_text_latest_order_in_list(self):
        text = self.get_text_element(OrderFeedLocators.latest_order_in_list)
        return text
    

    @allure.step('Ожидание отображения окна с деталями заказа')
    def wait_for_load_order_details_window(self):
        self.wait_for_load_element(OrderFeedLocators.order_details_window)


    @allure.step('Получение текста в окне с деталями заказа')
    def get_text_order_details_window(self):
        text = self.get_text_element(OrderFeedLocators.order_details_window)
        return text
    

