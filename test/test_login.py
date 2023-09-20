import datetime
import time

import pytest
from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_search_for_a_valid_product(self):
        homePageObj = HomePage(self.driver)
        loginPageObj = homePageObj.navigate_to_login_page()
        accountPageObj = loginPageObj.login('gidakik715@tenjb.com','pass@123')
        assert accountPageObj.display_status_of_edit_your_info()

    def test_login_with_invalidEmail_validPassword(self):
        homePageObj = HomePage(self.driver)
        loginPageObj = homePageObj.navigate_to_login_page()
        loginPageObj.login(self.create_invalidEmailId(),'pass@123')
        loginPageObj.click_login_btn()
        expectedWarning = 'Warning: No match for E-Mail Address and/or Password.'
        assert loginPageObj.is_warning_displayed().__eq__(expectedWarning)

    def test_login_with_validEmail_invalidPassword(self):
        homePageObj = HomePage(self.driver)
        loginPageObj = homePageObj.navigate_to_login_page()
        loginPageObj.login('gidakik715@tenjb.com','pass123')
        loginPageObj.click_login_btn()
        expectedWarning = 'Warning: No match for E-Mail Address and/or Password.'
        assert loginPageObj.is_warning_displayed().__eq__(expectedWarning)

    def test_login_without_credentials(self):
        homePageObj = HomePage(self.driver)
        loginPageObj = homePageObj.navigate_to_login_page()
        loginPageObj.click_login_btn()
        expectedWarning = 'Warning: No match for E-Mail Address and/or Password.'
        assert loginPageObj.is_warning_displayed().__eq__(expectedWarning)

    def create_invalidEmailId(self):
        currentTime = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "surya" + currentTime + "@gmail.com"
