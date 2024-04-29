from selenium.webdriver.common.by import By


class AccountRegistrationPage:
    txt_firstname_xpath = "//input[@id='input-firstname']"
    txt_lastname_xpath = "//input[@id='input-lastname']"
    txt_email_xpath = "//input[@id='input-email']"
    txt_telephone_xpath = "//input[@id='input-telephone']"
    txt_password_xpath = "//input[@id='input-password']"
    txt_confirm_password_xpath = "//input[@id='input-confirm']"
    rdo_newsletter_yes_xpath = "//label[normalize-space()='Yes']"
    rdo_newsletter_no_xpath = "//label[normalize-space()='No']"
    chk_policy_xpath = "//input[@name='agree']"
    btn_continue_xpath = "//input[@value='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setTelephone(self, phone):
        self.driver.find_element(By.XPATH, self.txt_telephone_xpath).send_keys(phone)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)

    def setConfPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_confirm_password_xpath).send_keys(pwd)

    def setNewsLetterYes(self):
        self.driver.find_element(By.XPATH, self.rdo_newsletter_yes_xpath).click()

    def setNewsLetterNo(self):
        self.driver.find_element(By.XPATH, self.rdo_newsletter_no_xpath).click()

    def setPrivacyPolicy(self):
        self.driver.find_element(By.XPATH, self.chk_policy_xpath).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()
