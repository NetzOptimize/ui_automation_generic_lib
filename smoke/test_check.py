# imports
from FUNCTIONS.helper import Checker
import json
from utilites.logfile import Logclass
import pytest


# test case
def test_checking(browser):
    ##################
    # LOGGING ERRORS, INFO etc.
    ##################
    logger = Logclass()
    log = logger.getLogs()
    log.info("This test is now running")

    ##################
    #  PASSING URL AND WEBDRIVER
    ##################
    run = Checker("http://127.0.0.1:5500/sample.html", browser)

    ##################
    # METHODS TO DISPLAY URL
    ##################
    run.display_url()
    website_url = run.return_url()
    print(f"Website url is: {website_url}")

    ##################
    # CHECK ALL CHECKBOXES
    ##################
    run.check_all("xpath", "//input[@type='checkbox']")

    ##################
    # COUNT ALL CHECKBOXES
    ##################
    count_checkbox = run.count_all_checkboxes("xpath", "//input[@type='checkbox']")
    print(f"Total number of checkboxes: {count_checkbox}")

    ##################
    # INPUT IN FIELDS
    ##################
    run.input("input", "xpath", "//input[@id='fname']", "type", "Sample Value 1")
    run.input("input", "xpath", "//input[@id='lname']", "type", "Sample Value 2")

    ##################
    # UNCHECK A CHECKED BOX
    ##################
    run.button("checkbox", "xpath", "/html[1]/body[1]/form[2]/input[2]", "click")

    ##################
    # STATIC DROPDOWN WITH DELAY
    ##################
    run.static_dropdown("xpath", "//select[@id='options']", "index", "3")
    run.slowmo(2)
    run.static_dropdown("xpath", "//select[@id='options']", "value", "1")
    run.slowmo(2)
    run.static_dropdown("xpath", "//select[@id='options']", "visible", "Option2")