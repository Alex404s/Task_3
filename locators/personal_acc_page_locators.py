from selenium.webdriver.common.by import By

class PersonalAccPageLocators:
    order_story_button = [By.XPATH, '//a[text()= "История заказов"]']
    order_story_number = [By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]//p[@class="text text_type_digits-default"]'] 
    exit_button = [By.XPATH, '//button[text()= "Выход"]']