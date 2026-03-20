from .base_page import BasePage
from ..locators.personal_acc_page_locators import PersonalAccPageLocators
from ..locators.order_feed_locators import OrderFeedLocators
import allure

class OrderFeed(BasePage):
    @allure.step('Ожидание отображения страницы "Лента заказов"')
    def wait_for_load_order_feed_field(self):
        super().wait_for_load_element(OrderFeedLocators.order_feed_field)

    
    @allure.step('Получение текста заголовка "Выполнено за все время:"')
    def get_text_order_feed_field(self):
        text = super().get_text_element(OrderFeedLocators.order_feed_field)
        return text
    

    @allure.step('Нажатие по последнему заказу')
    def click_latest_order_in_list(self):
        super().click_button(OrderFeedLocators.latest_order_in_list)


    @allure.step('Ожидание отображения окна с деталями заказа')
    def wait_for_load_order_details_window(self):
        super().wait_for_load_element(OrderFeedLocators.order_details_window)

    @allure.step('Получение текста в окне с деталями заказа')
    def get_text_order_details_window(self):
        text = super().get_text_element(OrderFeedLocators.order_details_window)
        return text
    
    @allure.step('Навести мышку в ленту заказов')
    def move_to_element(self):
        super().get_move_to_element(OrderFeedLocators.latest_order_in_list)

    
    @allure.step('Прокрутка до моего заказа')
    def scroll_my_order(self):
        super().scroll_to_element(PersonalAccPageLocators.order_story_number)


    @allure.step('Получение текста в окне с деталями заказа')
    def get_text_order_2(self):
        text = super().get_text_element(OrderFeedLocators.order_details_window)
        return text
