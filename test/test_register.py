import datetime
import pytest
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        homePageObj = HomePage(self.driver)
        registerPageObj = homePageObj.navigate_to_register_page()
        registerPageObj.enter_first_name("Surya")
        registerPageObj.enter_last_name("N")
        registerPageObj.enter_email_name(self.create_invalidEmailId())
        registerPageObj.enter_telephone("9876543210")
        registerPageObj.enterPassword("pass@123")
        registerPageObj.enterConfirmPassword("pass@123")
        registerPageObj.clickPolicyCheckBox()
        accountSuccessPage = registerPageObj.clickSubmitBtn()
        expected = "Your Account Has Been Created!"
        assert accountSuccessPage.retrive_account_creation_msg().__eq__(expected)
        self.driver.close()

    def test_register_with_all_fields(self):
        homePageObj = HomePage(self.driver)
        registerPageObj=homePageObj.navigate_to_register_page()
        registerPageObj.enter_first_name("Surya")
        registerPageObj.enter_last_name("N")
        registerPageObj.enter_email_name(self.create_invalidEmailId())
        registerPageObj.enter_telephone("9876543210")
        registerPageObj.enterPassword("pass@123")
        registerPageObj.enterConfirmPassword("pass@123")
        registerPageObj.click_subcribe_yes()
        registerPageObj.clickPolicyCheckBox()
        accountSuccessPage=registerPageObj.clickSubmitBtn()
        expected = "Your Account Has Been Created!"
        assert accountSuccessPage.retrive_account_creation_msg().__eq__(expected)
        self.driver.close()

    def test_register_with_duplicate_email(self):
        homePageObj = HomePage(self.driver)
        registerPageObj=homePageObj.navigate_to_register_page()
        registerPageObj.enter_first_name("Surya")
        registerPageObj.enter_last_name("N")
        registerPageObj.enter_email_name("gidakik715@tenjb.com")
        registerPageObj.enter_telephone("9876543210")
        registerPageObj.enterPassword("pass@123")
        registerPageObj.enterConfirmPassword("pass@123")
        registerPageObj.click_subcribe_yes()
        registerPageObj.clickPolicyCheckBox()
        registerPageObj.clickSubmitBtn()
        expectedWarning = "Warning: E-Mail Address is already registered!"
        assert registerPageObj.warningMessageText().__eq__(expectedWarning)
        self.driver.close()

    def without_anyFields(self):
        homePageObj = HomePage(self.driver)
        homePageObj.navigate_to_register_page()
        registerPageObj = RegisterPage(self.driver)
        registerPageObj.enter_first_name("")
        registerPageObj.enter_last_name("")
        registerPageObj.enter_email_name("")
        registerPageObj.enter_telephone("")
        registerPageObj.enterPassword("")
        registerPageObj.enterConfirmPassword("")
        registerPageObj.click_subcribe_yes()
        registerPageObj.clickPolicyCheckBox()
        registerPageObj.clickSubmitBtn()
        expectedWarningMessageError = 'Warning: You must agree to the Privacy Policy!'
        assert registerPageObj.warningMessageText().__eq__(expectedWarningMessageError)
        expectedFistNameMessageError = 'First Name must be between 1 and 32 characters!'
        assert registerPageObj.firstNameWarningXpath().__eq__(expectedFistNameMessageError)
        expectedLastNameMessageError = 'Last Name must be between 1 and 32 characters!'
        assert registerPageObj.lastNameWarningText().__eq__(expectedLastNameMessageError)
        expectedEmailMessageError = 'E-Mail Address does not appear to be valid!'
        assert registerPageObj.emailWarningText().__eq__(expectedEmailMessageError)
        expectedTelephoneMessageError = 'Telephone must be between 3 and 32 characters!'
        assert registerPageObj.telephoneWarningText().__eq__(expectedTelephoneMessageError)
        expectedPasswordMessageError = 'Password must be between 4 and 20 characters!'
        assert registerPageObj.passwordWarningText().__eq__(expectedPasswordMessageError)
        self.driver.close()

    def create_invalidEmailId(self):
        currentTime = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "surya" + currentTime + "@gmail.com"
