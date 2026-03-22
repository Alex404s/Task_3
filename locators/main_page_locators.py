from selenium.webdriver.common.by import By

class MainPageLocators:    
    main_login_button = [By.XPATH, '//button[text()= "Войти в аккаунт"]']    
    constructor_title = [By.XPATH, '//h1[text()= "Соберите бургер"]']
    ingredient_area = [By.XPATH, '//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]']
    sauce_spicy_x_img = [By.XPATH, '//img[@alt= "Соус Spicy-X"]']
    ingredient_details_title = [By.XPATH, '//h2[text()= "Детали ингредиента"]']
    close_ingredient_details_button = [By.XPATH, '//div[@class= "Modal_modal__contentBox__sCy8X pt-10 pb-15"]/following-sibling::button']    
    constructor_basket_area = [By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]']
    sauce_spicy_x_counter = [By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]//p[@class="counter_counter__num__3nue1"]']
    register_order_button = [By.XPATH, '//button[text()= "Оформить заказ"]']
    


class MainPageSelectors:
    register_order_button_text = 'Оформить заказ'
    sauce_spicy_x_counter_text = '1'
    ingredient_details_title_text = "Детали ингредиента"
    constructor_title_text = "Соберите бургер"