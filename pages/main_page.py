from .base_page import BasePage
from ..locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step('Ожидание кликабельности кнопки "Войти в аккаунт"')
    def wait_for_clickable_main_login_button(self):
        self.wait_for_clickable_element(MainPageLocators.main_login_button)


    @allure.step('Ожидание пропажи невидимого поля')
    def wait_for_invisibility_field(self):
        self.wait_for_visibility_element(MainPageLocators.field)


    @allure.step('Ожидание кликабельности кнопки "Оформить заказ"')
    def wait_for_clickable_register_order_button(self):
        self.wait_for_clickable_element(MainPageLocators.register_order_button)


    @allure.step('Ожидание кликабельности кнопки "Оформить заказ"')
    def wait_for_load_register_mail(self):
        self.wait_for_load_element(MainPageLocators.main_login_button)

    
    @allure.step('Ожидание отображения заголовка "Соберите бургер"')
    def wait_for_load_constructor_title(self):
        self.wait_for_load_element(MainPageLocators.constructor_title)


    @allure.step('Получение текста заголовка "Соберите бургер"')
    def get_text_constructor_title(self):
        text = self.get_text_element(MainPageLocators.constructor_title)
        return text
    

    @allure.step('Наведение на область ингредиентов')
    def move_ingredient_area(self):
        self.get_move_to_element(MainPageLocators.ingredient_area)


    @allure.step('Прокрутка ингредиентов до "Соус Spicy-X"')
    def scroll_to_sauce_spicy_x_img(self):
        self.scroll_to_element(MainPageLocators.sauce_spicy_x_img)
        

    @allure.step('Нажатие на ингредиент "Соус Spicy-X"')
    def click_sauce_spicy_x_img(self):
        self.click_button(MainPageLocators.sauce_spicy_x_img)

    
    @allure.step('Ожидание отображения заголовка "Детали ингредиента"')
    def wait_for_load_ingredient_details_title(self):
        self.wait_for_load_element(MainPageLocators.ingredient_details_title)


    @allure.step('Получение текста заголовка "Детали ингредиента"')
    def get_text_ingredient_details_title(self):
        text = self.get_text_element(MainPageLocators.ingredient_details_title)
        return text


    @allure.step('Нажатие на крестик в меню "Детали ингредиента" ингредиента "Соус Spicy-X"')
    def click_close_ingredient_details_button(self):
        self.click_button(MainPageLocators.close_ingredient_details_button)


    @allure.step('Нажатие на кнопку "Войти в аккаунт"')
    def click_main_login_button(self):
        self.click_button(MainPageLocators.main_login_button)


    @allure.step('Добавление ингредиента "Соус Spicy-X" в заказ')
    def add_to_order_sauce_spicy_x_img(self):
        self.drag_and_drop(MainPageLocators.sauce_spicy_x_img, MainPageLocators.constructor_basket_area)

    
    @allure.step('Получение каунтера ингредиента "Соус Spicy-X"')
    def get_text_sauce_spicy_x_counter(self):
        text = self.get_text_element(MainPageLocators.sauce_spicy_x_counter)
        return text
    

    @allure.step('Получение текста кнопки "Оформить заказ"')
    def get_text_register_order_button(self):
        text = self.get_text_element(MainPageLocators.register_order_button)
        return text


    @allure.step('Сценарий "переход по клику на «Конструктор»"')
    def scenario_go_to_constructor(self):
        self.wait_for_clickable_main_login_button()
        self.wait_for_invisibility_field()
        self.personal_acc_button_click()
        self.constructor_button_click()
        self.wait_for_load_constructor_title()

    
    @allure.step('Сценарий "переход по клику на «Лента заказов»"')
    def scenario_go_to_order_feed(self):
        self.wait_for_clickable_main_login_button()
        self.wait_for_invisibility_field()        
        self.order_feed_button_click()


    @allure.step('Сценарий "если кликнуть на ингредиент, появится всплывающее окно с деталями"')
    def scenario_ingredient_details(self):
        self.wait_for_clickable_main_login_button()
        self.wait_for_invisibility_field()
        self.move_ingredient_area()
        self.scroll_to_sauce_spicy_x_img()     
        self.click_sauce_spicy_x_img()

    
    @allure.step('Сценарий "при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента"')
    def scenario_add_to_order(self):
        self.wait_for_clickable_main_login_button()
        self.wait_for_invisibility_field()
        self.move_ingredient_area()
        self.scroll_to_sauce_spicy_x_img()
        self.wait_for_clickable_main_login_button()
        self.add_to_order_sauce_spicy_x_img()
        



    


    


    

    