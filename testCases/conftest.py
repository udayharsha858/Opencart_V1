from datetime import datetime
import os.path

import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.customLogger import LogGenerator

logger = LogGenerator.log_generator()  # This statement supports to generate logs


@pytest.fixture
def setup(browser):
    # if browser == 'chrome':
    #     options = webdriver.ChromeOptions()
    #     options.add_experimental_option("detach", True)
    #     options.add_argument("--disable-notifications")
    #     driver = webdriver.Chrome(options=options)
    #     return driver
    if browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")
        driver = webdriver.Edge(options=options)
        # return driver
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-notifications")
        driver = webdriver.Firefox(options=options)
        # return driver
    else:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options)
        # return driver
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


"""
Pytest HTML Reports
"""


def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "OpenCart"
    config.stash[metadata_key]["Module Name"] = "Registration Module"
    config.stash[metadata_key]["Tester Name"] = "Uday Kumar A"


def pytest_html_report_title(report):
    report.title = "OpenCart Test"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = (os.path.abspath(os.curdir) + "/reports/" + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                              + ".html")
