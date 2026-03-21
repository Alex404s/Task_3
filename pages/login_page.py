from .base_page import BasePage
from ..locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):    
    @allure.step('Ожидание кликабельности кнопки "Восстановить пароль"')
    def wait_for_clickable_restore_password_button(self):
        self.wait_for_clickable_element(LoginPageLocators.restore_password_button)


    @allure.step('Ввод почты для авторизации')
    def send_keys_to_login_email_field(self, email):
        self.send_keys_to_element(LoginPageLocators.login_email_field, email)


    @allure.step('Ввод пароля для авторизации')
    def send_keys_to_login_password_field(self, password):
        self.send_keys_to_element(LoginPageLocators.login_password_field, password)


    @allure.step('Нажатие на кнопку "Войти"')
    def login_button_click(self):
        self.click_button(LoginPageLocators.login_button)


    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def restore_password_button_click(self):
        self.click_button(LoginPageLocators.restore_password_button)

    
    @allure.step('Получение текста заголовка "Восстановить пароль"')
    def get_text_restore_password_button(self):
        text = self.get_text_element(LoginPageLocators.restore_password_button)
        return text
    
    
    @allure.step('Получение текста заголовка "Восстановление пароля"')
    def get_text_restore_password_title(self):
        text = self.get_text_element(LoginPageLocators.restore_password_title)
        return text
    
    @allure.step('Ожидание кликабельности поля ввода email')
    def wait_for_clickable_restore_password_email_field(self):
        self.wait_for_clickable_element(LoginPageLocators.restore_password_email_field)


    @allure.step('Ввод почты для восстановления пароля')
    def send_keys_to_restore_password_email_field(self, email):
        self.send_keys_to_element(LoginPageLocators.restore_password_email_field, email)

    
    @allure.step('Нажатие на кнопку "Восстановить"')
    def click_restore_password_accept_button(self):
        self.click_button(LoginPageLocators.restore_password_accept_button)


    @allure.step('Ожидание кликабельности кнопки показать/скрыть пароль')
    def wait_for_clickable_hide_show_password_button(self):
        self.wait_for_clickable_element(LoginPageLocators.hide_show_password_button)


    @allure.step('Получение текста названия поля "Введите код из письма"')
    def get_text_help_text_code_from_letter(self):
        text = self.get_text_element(LoginPageLocators.help_text_code_from_letter)
        return text
    

    @allure.step('Нажатие на кнопку показать/скрыть пароль')
    def click_hide_show_password_button(self):
        self.click_button(LoginPageLocators.hide_show_password_button)

    
    @allure.step('Ожидание отображения подсветки поля "Пароль"')
    def wait_for_load_active_password_field(self):
        self.wait_for_clickable_element(LoginPageLocators.active_password_field)

    
    @allure.step('Получение значения атрибута "class" подсветки поля "Пароль"')
    def get_attribute_value_active_password_field(self):
        value = self.get_attribute_value_element(LoginPageLocators.active_password_field, "class")
        return value
    

    @allure.step('Авторизация пользователя')
    def login_user(self, email, password):
        self.wait_for_clickable_personal_acc_button()
        self.personal_acc_button_click()
        self.wait_for_clickable_restore_password_button()
        self.send_keys_to_login_email_field(email)
        self.send_keys_to_login_password_field(password)
        self.login_button_click()   
    

    @allure.step('Сценарий "Переход на страницу восстановления пароля по кнопке «Восстановить пароль»"')
    def scenario_go_to_restore_password(self):        
        self.personal_acc_button_click()
        self.wait_for_clickable_restore_password_button()
        self.restore_password_button_click()
        self.wait_for_clickable_restore_password_email_field()
        

    @allure.step('Сценарий "Ввод почты и клик по кнопке «Восстановить»"')
    def scenario_insert_email_and_go_to_next_menu(self, email):
        self.scenario_go_to_restore_password()
        self.send_keys_to_restore_password_email_field(email)
        self.click_restore_password_accept_button()
        self.wait_for_clickable_hide_show_password_button()


    @allure.step('Сценарий "Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его"')
    def scenario_click_hide_show_password_active(self, email):
        self.scenario_insert_email_and_go_to_next_menu(email)
        self.click_hide_show_password_button()
        self.wait_for_load_active_password_field()



    

 




    