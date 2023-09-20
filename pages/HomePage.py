from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage:
    searchBoxXPath =  '//*[@id="search"]/input'
    searchBtnXPath = '//*[@id="search"]/span/button'
    accountMenuXpath = '//*[@id="top-links"]/ul/li[2]/a/span[1]'
    loginBtnXpath = '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a'
    registerBtnXpath = '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a'

    def __init__(self, driver):
        self.driver = driver

    def enter_product_into_search_box(self, productName):
        self.driver.find_element(By.XPATH,self.searchBoxXPath).click()
        self.driver.find_element(By.XPATH,self.searchBoxXPath).clear()
        self.driver.find_element(By.XPATH,self.searchBoxXPath).send_keys(productName)

    def click_search_btn(self):
        self.driver.find_element(By.XPATH,self.searchBtnXPath).click()
        return SearchPage(self.driver)

    def navigate_to_login_page(self):
        self.driver.find_element(By.XPATH,self.accountMenuXpath).click()
        self.driver.find_element(By.XPATH,self.loginBtnXpath).click()
        return LoginPage(self.driver)

    def navigate_to_register_page(self):
        self.driver.find_element(By.XPATH,self.accountMenuXpath).click()
        self.driver.find_element(By.XPATH,self.registerBtnXpath).click()
        return RegisterPage(self.driver)

    def search_for_a_product(self,productName):
        self.enter_product_into_search_box(productName)
        searchPageObj = self.click_search_btn()
        return searchPageObj
