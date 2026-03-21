from selenium.webdriver.common.by import By

class LoginPageLocators:    
    login_email_field = [By.XPATH, '//input[@name= "name"]']
    login_password_field = [By.XPATH, '//input[@name= "Пароль"]']
    login_button = [By.XPATH, '//button[text()= "Войти"]']
    restore_password_button = [By.XPATH, '//a[text()="Восстановить пароль"]']
    restore_password_title = [By.XPATH, '//h2[text()="Восстановление пароля"]']
    restore_password_email_field = [By.XPATH, '//input[@class= "text input__textfield text_type_main-default"]']
    restore_password_accept_button = [By.XPATH, '//button[text()= "Восстановить"]']
    help_text_code_from_letter = [By.XPATH, '//label[text()= "Введите код из письма"]']
    hide_show_password_button = [By.XPATH, '//div[@class="input__icon input__icon-action"]']
    active_password_field = [By.XPATH, '//div[@class= "input pr-6 pl-6 input_type_text input_size_default input_status_active"]']
    

class LoginPageSelectors:
    active_password_field = "input pr-6 pl-6 input_type_text input_size_default input_status_active"