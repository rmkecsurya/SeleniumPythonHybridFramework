from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage


class RegisterPage:
    firstNameId = 'input-firstname'
    lastNameId = 'input-lastname'
    emailId = 'input-email'
    telephoneId = 'input-telephone'
    passwordId = 'input-password'
    confirmPasswordId = 'input-confirm'
    subcribeYesXPath = '//*[@id="content"]/form/fieldset[3]/div/div/label[1]/input'
    policyXPath = '//*[@id="content"]/form/div/div/input[1]'
    submitBtnXPath = '//*[@id="content"]/form/div/div/input[2]'
    warningMsgXPath = '//*[@id="account-register"]/div[1]'
    firstNameWarningXpath = '//*[@id="account"]/div[2]/div/div'
    lastNameWarningXpath = '//*[@id="account"]/div[3]/div/div'
    emailWarningXPath = '//*[@id="account"]/div[4]/div/div'
    telephoneWarningXPath = '//*[@id="account"]/div[5]/div/div'
    passwordWarningXPath = '//*[@id="content"]/form/fieldset[2]/div[1]/div/div'

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, firstName):
        self.driver.find_element(By.ID, self.firstNameId).click()
        self.driver.find_element(By.ID, self.firstNameId).clear()
        self.driver.find_element(By.ID, self.firstNameId).send_keys(firstName)

    def enter_last_name(self, lastName):
        self.driver.find_element(By.ID, self.lastNameId).click()
        self.driver.find_element(By.ID, self.lastNameId).clear()
        self.driver.find_element(By.ID, self.lastNameId).send_keys(lastName)

    def enter_email_name(self, emailId):
        self.driver.find_element(By.ID, self.emailId).click()
        self.driver.find_element(By.ID, self.emailId).clear()
        self.driver.find_element(By.ID, self.emailId).send_keys(emailId)

    def enter_telephone(self, telephone):
        self.driver.find_element(By.ID, self.telephoneId).click()
        self.driver.find_element(By.ID, self.telephoneId).clear()
        self.driver.find_element(By.ID, self.telephoneId).send_keys(telephone)

    def enterPassword(self, password):
        self.driver.find_element(By.ID, self.passwordId).click()
        self.driver.find_element(By.ID, self.passwordId).clear()
        self.driver.find_element(By.ID, self.passwordId).send_keys(password)

    def enterConfirmPassword(self, password):
        self.driver.find_element(By.ID, self.confirmPasswordId).click()
        self.driver.find_element(By.ID, self.confirmPasswordId).clear()
        self.driver.find_element(By.ID, self.confirmPasswordId).send_keys(password)

    def click_subcribe_yes(self):
        self.driver.find_element(By.XPATH, self.subcribeYesXPath).click()

    def clickPolicyCheckBox(self):
        self.driver.find_element(By.XPATH, self.policyXPath).click()

    def clickSubmitBtn(self):
        self.driver.find_element(By.XPATH, self.submitBtnXPath).click()
        return AccountSuccessPage(self.driver)

    def warningMessageText(self):
        return self.driver.find_element(By.XPATH, self.warningMsgXPath).text

    def firstNameWarningText(self):
        return self.driver.find_element(By.XPATH, self.firstNameWarningXpath).text

    def lastNameWarningText(self):
        return self.driver.find_element(By.XPATH, self.lastNameWarningXpath).text

    def emailWarningText(self):
        return self.driver.find_element(By.XPATH, self.emailWarningXPath).text

    def telephoneWarningText(self):
        return self.driver.find_element(By.XPATH, self.telephoneWarningXPath).text

    def passwordWarningText(self):
        return self.driver.find_element(By.XPATH, self.passwordWarningXPath).text
