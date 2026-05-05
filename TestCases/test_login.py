import time

import pytest
from selenium import webdriver
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

#from TestCases.conftest import setup
from pageObjects.LoginPage import LoginPage


class Test_001_login:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    Logger_1 = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.Logger_1.info("********** Test_001_login **********")
        self.Logger_1.info("********** Verifying homePage Title **********")
        self.driver = setup
        self.driver.get(self.base_url)
        time.sleep(10)
        self.driver.maximize_window()
        actual_title = self.driver.title

        if actual_title == "nopCommerce demo store. Login":
            assert True
            self.Logger_1.info("********** Homepage Title Test Case Passed **********")
        else:
            self.driver.save_screenshot(r"C:\Users\nishk\PycharmProjects\nopCommerceAdmin\Screenshots\test_homePageTitle.png")
            self.Logger_1.error("********** Homepage Title Test Case Failed **********")
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.Logger_1.info("********** Verifying Login Test Case **********")
        self.driver = setup
        self.driver.get(self.base_url)
        time.sleep(8)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.click_login_btn()
        time.sleep(2)
        new_title = self.driver.title

        if new_title == "Dashboard / nopCommerce administration":
            assert True
            self.Logger_1.info("********** Login Test CAse is passed **********")
        else:
            self.driver.save_screenshot(r"C:\Users\nishk\PycharmProjects\nopCommerceAdmin\Screenshots\test_Login.png")
            self.Logger_1.error("********** Login Test Case is Failed **********")
            assert False

