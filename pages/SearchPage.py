from selenium.webdriver.common.by import By

class SearchPage:
    search_by_link_text = 'HP LP3065'
    noProductMessageXpath = '//input[@id="button-search"]/following-sibling::p'

    def __init__(self,driver):
        self.driver = driver

    def validate_search(self):
        return self.driver.find_element(By.LINK_TEXT,self.search_by_link_text).is_displayed()

    def retrive_no_product_message(self):
        return self.driver.find_element(By.XPATH, self.noProductMessageXpath).text


