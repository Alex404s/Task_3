from .base_page import BasePage
from ..locators.personal_acc_page_locators import PersonalAccPageLocators
import allure



class PersonalAccPage(BasePage):
    @allure.step('Ожидание кликабельности раздела "История заказов"')
    def wait_for_clickable_order_story_button(self):
        super().wait_for_clickable_element(PersonalAccPageLocators.order_story_button)


    @allure.step('Получение текста раздела "История заказов"')
    def get_text_order_story_button(self):
        text = super().get_text_element(PersonalAccPageLocators.order_story_button)
        return text


    @allure.step('Нажатие на кнопку "История заказов"')
    def order_story_button_click(self):
        super().click_button(PersonalAccPageLocators.order_story_button)


    @allure.step('Получение значения атрибута "class" активного поля "История заказов"')
    def get_attribute_value_active_order_story_button(self):
        value = super().get_attribute_value_element(PersonalAccPageLocators.order_story_button, "class")
        return value
    

    @allure.step('Нажатие на кнопку "Выход"')
    def order_exit_button_click(self):
        super().click_button(PersonalAccPageLocators.exit_button)


    @allure.step('Получения номера заказа')
    def get_order_num(self):
        text = super().get_text_element(PersonalAccPageLocators.order_story_number)
        return text
    
    @allure.step('Сценарий "Переход по клику на «Личный кабинет»"')
    def scenario_go_to_personal_acc(self):        
        super().wait_for_clickable_personal_acc_button()         
        super().personal_acc_button_click()       
        self.wait_for_clickable_order_story_button()

    
    @allure.step('Сценарий "Переход в раздел «История заказов»"')
    def scenario_go_to_order_story(self):
        super().wait_for_clickable_personal_acc_button()
        super().personal_acc_button_click()
        self.wait_for_clickable_order_story_button()
        self.order_story_button_click()


    @allure.step('Сценарий "Выход из аккаунта"')
    def scenario_acc_exit(self):
        super().wait_for_clickable_personal_acc_button()
        super().personal_acc_button_click()
        self.wait_for_clickable_order_story_button()
        self.order_exit_button_click()
    

    
