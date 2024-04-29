import pytest

from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from utilities import randomString
from pageObjects.MyAccountPage import MyAccountPage
import os

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator


class Test_AccountReg:
    base_url = ReadConfig.getApplicationUrl()  # This is to get the base_url
    logger = LogGenerator.log_generator()  # This statement supports to generate logs

    @pytest.mark.regression
    def test_account_reg(self, setup):

        """Driver initiation and passing url"""
        self.logger.info("*** test_AccountRegistration started ***")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("Application launched in maximised window")

        """Creating objects for PageObject classes"""

        self.Home_Page = HomePage(self.driver)
        self.Reg_Page = AccountRegistrationPage(self.driver)
        self.MyAccount_Page = MyAccountPage(self.driver)

        """Redirecting to registration page from home page"""

        self.Home_Page.clickMyAccount()
        self.Home_Page.clickRegister()
        self.logger.info("application redirected to Registration Page")

        """Registering a new account in Registration page"""

        self.Reg_Page.setFirstName("John")
        self.Reg_Page.setLastName("Canedy")
        self.email = randomString.random_string_generator() + '@gmail.com'
        self.Reg_Page.setEmail(self.email)
        self.Reg_Page.setTelephone("9876543210")
        self.Reg_Page.setPassword("abc12xyz")
        self.Reg_Page.setConfPassword("abc12xyz")
        self.Reg_Page.setPrivacyPolicy()
        self.logger.info("Provided all the information to start registration")
        self.Reg_Page.clickContinue()
        self.confMsg = self.MyAccount_Page.getConfirmMsg()
        self.logger.info("Application redirected to registration confirmation page after clicking on continue")

        """Comparing a Confirmation message"""

        if self.confMsg == 'Your Account Has Been Created!':
            self.logger.info("Account registration is passed")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "/screenshots/" + "test_account_reg.png")
            self.logger.error("Account registration is failed")
            self.driver.close()
            assert False

        self.logger.info("*** test_AccountRegistration completed ***")
