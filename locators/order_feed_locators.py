from selenium.webdriver.common.by import By

class OrderFeedLocators:
    order_feed_field = [By.XPATH, '//p[text()= "Выполнено за все время:"]']
    latest_order_in_list = [By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"][1]//p[@class="text text_type_digits-default"]']
    order_details_window = [By.XPATH, '//p[@class="text text_type_digits-default mb-10 mt-5"]']
    counter_pass_all_time = [By.XPATH, '//p[text()= "Выполнено за все время:"]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
    counter_pass_today = [By.XPATH, '//p[text()= "Выполнено за сегодня:"]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
    number_order_in_work = [By.XPATH, '//ul[@class= "OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]']
    
    
class OrderFeedSelectors:
    all_time_counter_title_text = "Выполнено за все время:"


