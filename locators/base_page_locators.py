from selenium.webdriver.common.by import By

class BasePageLocators:
    personal_acc_button = [By.XPATH, '//p[text()= "Личный Кабинет"]']
    constructor_button = [By.XPATH, '//p[text()= "Конструктор"]']
    order_feed_button = [By.XPATH, '//a[@class="AppHeader_header__link__3D_hX"]/p[text()= "Лента Заказов"]']
    field = [By.XPATH, '//div[@class="Modal_modal_overlay__x2ZCr"]']