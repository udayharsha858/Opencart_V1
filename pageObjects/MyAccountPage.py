from selenium.webdriver.common.by import By


class MyAccountPage:
    msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"
    msg_myaccount_xpath = "//h2[normalize-space()='My Account']"
    btn_logout_xpath = "//li[@class='dropdown open']/ul//li/a[text()='Logout']"
    msg_Logout_conf_msg_xpath = "//h1[normalize-space()='Account Logout']"

    def __init__(self, driver):
        self.driver = driver

    def getConfirmMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_conf_xpath).text
        except:
            None

    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
        except:
            return False

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()

    def getLogoutConfirmationMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_Logout_conf_msg_xpath).text
        except:
            None
