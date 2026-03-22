from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.base_page_locators import BasePageLocators
from selenium.webdriver import ActionChains
import allure
from seletools.actions import drag_and_drop


class BasePage:

    @allure.step('Инициализация переменной')
    def __init__(self, driver):
        self.driver = driver 


    @allure.step('Ожидание отображения элемента на странице')
    def wait_for_load_element(self, element_locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(element_locator))


    @allure.step('Ожидание кликабельности элемента')
    def wait_for_clickable_element(self, element_locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(element_locator)) 


    @allure.step('Ожидание пропажи отображения элемента')
    def wait_for_visibility_element(self, element_locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element_located(element_locator))      


    @allure.step('Клик по элементу')
    def click_button(self, button_locator):
        self.driver.find_element(*button_locator).click()


    @allure.step('Получение текста элемента')
    def get_text_element(self, element_locator):
        element_text = self.driver.find_element(*element_locator).text
        return element_text
    
    
    @allure.step('Прокрутка страницы до элемента')
    def scroll_to_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step('Ввод значения')
    def send_keys_to_element(self, element_locator, data):
        self.driver.find_element(*element_locator).send_keys(data)


    @allure.step('Получение URL текущей страницы')
    def get_url(self):
        current_url = self.driver.current_url
        return current_url
    
    
    @allure.step('Переключение на последнюю открытую страницу в браузере')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])    

    
    @allure.step('Получение значения атрибута элемента')
    def get_attribute_value_element(self, element_locator, element_attribute):
        element = self.driver.find_element(*element_locator)
        attribute_value = element.get_attribute(element_attribute)
        return attribute_value
    

    @allure.step('Наведение на определенную область')
    def get_move_to_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()


    @allure.step('Перенос элемента')
    def drag_and_drop_element(self, element_locator, target_element_locator):
        element = self.driver.find_element(*element_locator)
        target_element = self.driver.find_element(*target_element_locator)       
        drag_and_drop(self.driver, element, target_element)

       
    @allure.step('Ожидание кликабельности кнопки "Личный кабинет"')
    def wait_for_clickable_personal_acc_button(self):
        self.wait_for_clickable_element(BasePageLocators.personal_acc_button)    


    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def personal_acc_button_click(self):
        self.click_button(BasePageLocators.personal_acc_button)


    @allure.step('Ожидание кликабельности кнопки "Конструктор"')
    def wait_for_clickable_constructor_button(self):
        self.wait_for_clickable_element(BasePageLocators.constructor_button)    


    @allure.step('Нажатие на кнопку "Конструктор"')
    def constructor_button_click(self):
        self.click_button(BasePageLocators.constructor_button)


    @allure.step('Ожидание кликабельности кнопки "Лента заказов"')
    def wait_for_clickable_order_feed_button(self):
        self.wait_for_clickable_element(BasePageLocators.order_feed_button)    


    @allure.step('Нажатие на кнопку "Лента заказов"')
    def order_feed_button_click(self):
        self.click_button(BasePageLocators.order_feed_button)


    @allure.step('Ожидание пропажи невидимого поля')
    def wait_for_invisibility_field(self):
        self.wait_for_visibility_element(BasePageLocators.field)




