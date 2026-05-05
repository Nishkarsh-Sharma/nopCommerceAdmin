from operator import truediv

import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomers import AddCustomer
from pageObjects.searchCustomers import SearchCustomer
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
import time

class Test_005_searchCustomer_byName:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    passw = ReadConfig.getPassword()
    Logger_5 = LogGen.loggen()

    @pytest.mark.regression
    def test_send_Name(self,setup):
        self.driver = setup
        self.Logger_5.info("**** Test case_005_ search customer by name started")
        self.driver.get(self.baseurl)
        time.sleep(10)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.passw)
        self.lp.click_login_btn()

        self.Logger_5.info("**** Login Successfull")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.clickOnCustomerMenu()
        self.add_cust.clickOnCsutomerSubmenu()

        search_ByName = SearchCustomer(self.driver)
        search_ByName.set_firstName("Victoria")
        search_ByName.set_lastName("Terces")
        search_ByName.click_search_btn()

        status = search_ByName.searchCustomerbyName("Victoria Terces")

        if status == True:
            self.Logger_5.info("***** Teats case_005_search customer by name passed ***")
            assert True
        else:
            time.sleep(5)
            self.driver.save_screenshot(r"C:\Users\nishk\PycharmProjects\nopCommerceAdmin\Screenshots\test_searchCustomerByName_src.png")
            self.Logger_5.error("***** Teats case_005_search customer by name failed ***")
            assert False

        self.Logger_5.info("***** Teats case_005_search customer by name Completed ***")
