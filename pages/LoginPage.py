from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage


class LoginPage:
    emailTextBoxXPATH = '//*[@id="input-email"]'
    passwordTxtBoxXPATH = '//*[@id="input-password"]'
    loginBtnXPATH = '//input[@class="btn btn-primary"]'
    warningXPATH = '//*[@id="account-login"]/div[1]'

    def __init__(self,driver):
        self.driver = driver

    def enter_email_text_box(self,emailId):
        self.driver.find_element(By.XPATH, self.emailTextBoxXPATH).click()
        self.driver.find_element(By.XPATH, self.emailTextBoxXPATH).clear()
        self.driver.find_element(By.XPATH, self.emailTextBoxXPATH).send_keys(emailId)

    def enter_password_text_box(self,pswd):
        self.driver.find_element(By.XPATH, self.passwordTxtBoxXPATH).click()
        self.driver.find_element(By.XPATH, self.passwordTxtBoxXPATH).clear()
        self.driver.find_element(By.XPATH, self.passwordTxtBoxXPATH).send_keys(pswd)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.loginBtnXPATH).click()
        return AccountPage(self.driver)

    def login(self,emailId,pswd):
        self.enter_email_text_box(emailId)
        self.enter_password_text_box(pswd)
        accountPageObj = self.click_login_btn()
        return accountPageObj

    def is_warning_displayed(self):
        return self.driver.find_element(By.XPATH, self.warningXPATH).text
