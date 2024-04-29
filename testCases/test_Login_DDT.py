import time
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import excelUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator
import os


class Test_Login_DDT:
    base_url = ReadConfig.getApplicationUrl()
    logger = LogGenerator.log_generator()

    path = os.path.abspath(os.curdir)+"/testData/OpenCart_login_testdata.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.rows = excelUtils.getRowCount(self.path, 'Sheet1')
        list_status = []

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.Home_Page = HomePage(self.driver)
        self.Login_Page = LoginPage(self.driver)
        self.MyAccount_Page = MyAccountPage(self.driver)

        for r in range(2, self.rows+1):
            time.sleep(2)
            self.Home_Page.clickMyAccount()
            time.sleep(2)
            self.Home_Page.clickLogin()

            self.email = excelUtils.readData(self.path, "Sheet1", r, 1)
            self.password = excelUtils.readData(self.path, "Sheet1", r, 2)
            self.expected_res = excelUtils.readData(self.path, "Sheet1", r, 3)
            # time.sleep(2)
            self.Login_Page.setEmail(self.email)
            # time.sleep(2)
            self.Login_Page.setPassword(self.password)
            # time.sleep(2)
            self.Login_Page.clickLogin()
            time.sleep(3)
            self.target_page = self.MyAccount_Page.isMyAccountPageExists()

            if self.expected_res == 'Valid':
                if self.target_page is True:
                    list_status.append('Pass')
                    self.Home_Page.clickMyAccount()
                    self.MyAccount_Page.clickLogout()
                else:
                    list_status.append('Fail')

            elif self.expected_res == 'Invalid':
                if self.target_page is True:
                    list_status.append('Fail')
                    self.Home_Page.clickMyAccount()
                    self.MyAccount_Page.clickLogout()
                else:
                    list_status.append('Pass')
        self.driver.close()

        # Final Validation

        if "Fail" not in list_status:
            assert True
        else:
            assert False
        self.logger.info('Test case "test_Login_DDT" completed testing')
