import pytest
from selenium import webdriver
from utilities import ReadConfig


@pytest.fixture()
def setup(request):
    browser = ReadConfig.read_configuration("basic info", "browser")
    print(browser)
    # global driver
    driver = None
    # driver = webdriver.Chrome()
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("Provide the valid Browser Name")
    driver.maximize_window()
    url = ReadConfig.read_configuration("basic info", "url")
    # driver.get("https://tutorialsninja.com/demo/")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
