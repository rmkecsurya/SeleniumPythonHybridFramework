from selenium.webdriver.common.by import By

class AccountPage:

    editYourInformationLinkText = 'Edit your account information'

    def __init__(self,driver):
        self.driver = driver

    def display_status_of_edit_your_info(self):
        return self.driver.find_element(By.LINK_TEXT, self.editYourInformationLinkText).is_displayed()