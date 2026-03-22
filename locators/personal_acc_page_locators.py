from selenium.webdriver.common.by import By

class PersonalAccPageLocators:
    order_story_button = [By.XPATH, '//a[text()= "История заказов"]']
    order_story_number = [By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"][1]//p[@class="text text_type_digits-default"]'] 
    exit_button = [By.XPATH, '//button[text()= "Выход"]']


class PersonalAccSelectors:
    active_order_story_button = 'Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9'
    order_story_button_text = "История заказов"