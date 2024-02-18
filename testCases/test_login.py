import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utlitities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_homePageTitle(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        self.driver.close()

        if actual_title == "Swag Labs":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin(self)
        actual_title = self.driver.title
        self.driver.close()

        if actual_title == "Swag Labs":
            assert True
        else:
            assert False
