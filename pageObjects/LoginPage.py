from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    username_login_xpath = "//input[@id='user-name']"
    password_login_xpath = "//input[@id='password']"
    login_button_xpath = "//input[@id='login-button']"
    profile_xpath = "//img[@class='oxd-userdropdown-img']"
    logout_linktext = "/web/index.php/auth/logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.username_login_xpath).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_login_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_login_xpath).send_keys(password)

    def clickLogin(self, login):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def clickLogout(self, profile, logout):
        self.driver.find_element(By.XPATH, self.profile_xpath).click()
        self.driver.find_element(By.XPATH, self.logout_linktext).click()