#This program uses Selenium Webdriver and Pytest to run a parameterized test of the 
#Google homepage using Firefox then Chrome. It launches the browser, gets the Google
#page, uses a lambda function to await the search text box to be enabled by its name 
#selector, it sends keys into the search text box by its name selector, it clicks the 
#search button by its CSS selector, and tests with an assersion that the search string
#exists in the browser's title.  

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest):
    if request.param == "firefox":
        browser = webdriver.Firefox()
    elif request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        raise ValueError("Invalid browser type")
    request.addfinalizer(browser.quit)
    return browser

@pytest.mark.parametrize("browser", ["firefox", "chrome"], indirect=True)
def test_google_search(browser):
    print("Running test_google_search...")
    browser.get("https://www.google.com")

    # Wait for search entry field to be enabled
    element = WebDriverWait(browser, 10).until(
    lambda browser: browser.find_element(By.NAME, "q").is_enabled()
    )
    print(f'element {element}is enabled')
    browser.find_element(By.NAME, "q").send_keys("pytest selenium")
    browser.find_element(By.CSS_SELECTOR, "center:nth-child(1) > .gNO89b").click()
    assert "pytest selenium" in browser.title
    print("Test outcome: Passed" if "pytest selenium" in browser.title else "Test outcome: Failed")
    input("Press Enter to continue...")