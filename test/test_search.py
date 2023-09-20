import pytest
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage


@pytest.mark.usefixtures("setup")
class TestSearch:
    def test_search_for_a_valid_product(self):
        homePageObj = HomePage(self.driver)
        searchPageObj = homePageObj.search_for_a_product("HP")
        assert searchPageObj.validate_search()

    def test_search_for_a_invalid_product(self):
        homePageObj = HomePage(self.driver)
        searchPageObj = homePageObj.search_for_a_product("Honda")
        expectedMessage = 'There is no product that matches the search criteria.'
        assert searchPageObj.retrive_no_product_message().__eq__(expectedMessage)

    def test_search_for_a_empty_product(self):
        homePageObj = HomePage(self.driver)
        searchPageObj = homePageObj.search_for_a_product("")
        expectedMessage = 'There is no product that matches the search criteria.'
        assert searchPageObj.retrive_no_product_message().__eq__(expectedMessage)
