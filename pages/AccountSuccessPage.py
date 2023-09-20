from selenium.webdriver.common.by import By


class AccountSuccessPage:

    accountCreationXpath = '//*[@id="content"]/h1'
    def __init__(self, driver):
        self.driver = driver

    def retrive_account_creation_msg(self):
        return self.driver.find_element(By.XPATH, self.accountCreationXpath).text
