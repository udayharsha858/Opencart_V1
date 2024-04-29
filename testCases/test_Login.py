import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from pageObjects.MyAccountPage import MyAccountPage
import os

from utilities.customLogger import LogGenerator
from utilities.readProperties import ReadConfig


class Test_Login:
    base_url = ReadConfig.getApplicationUrl()  # This is to get the base_url
    logger = LogGenerator.log_generator()  # This statement supports to generate logs

    user = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self, setup):

        """Driver initiation and passing url"""
        self.logger.info("*** test_AccountRegistration started ***")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("Application launched in maximised window")

        """Creating objects for PageObject classes"""

        self.Home_Page = HomePage(self.driver)
        self.Login_Page = LoginPage(self.driver)
        self.MyAccount_Page = MyAccountPage(self.driver)

        """Redirecting to registration page from home page"""

        self.Home_Page.clickMyAccount()
        self.Home_Page.clickLogin()
        self.logger.info("application redirected to Registration Page")

        """Login to your account in by providing credentials"""
        self.logger.info("Login to application with provided data")
        self.Login_Page.setEmail(self.user)
        time.sleep(2)
        self.Login_Page.setPassword(self.password)
        time.sleep(2)
        self.Login_Page.clickLogin()
        time.sleep(2)

        """Validating the page redirection"""
        self.text_myaccount = self.MyAccount_Page.isMyAccountPageExists()
        if self.text_myaccount==True:
            self.logger.info("Account Login is passed is passed")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "/screenshots/" + "test_login.png")
            self.logger.error("Account login is failed")
            self.driver.close()
            assert False

        self.logger.info("*** test_login completed ***")
