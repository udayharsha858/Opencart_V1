from selenium.webdriver.common.by import By


class LoginPage:
    txt_email_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    btn_fgtPassword_xpath = "//div[@class='form-group']/a"
    btn_login_xpath = "//input[@value='Login']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)

    def clickForgetPassword(self):
        self.driver.find_element(By.XPATH, self.btn_fgtPassword_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
