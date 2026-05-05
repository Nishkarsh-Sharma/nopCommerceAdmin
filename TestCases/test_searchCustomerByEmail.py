import time

import pytest
from Utilities.customLogger import LogGen
from pageObjects.searchCustomers import SearchCustomer
from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomers import AddCustomer

class Test_004_searchCustomer_email:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    passw = ReadConfig.getPassword()
    Logger_4 = LogGen.loggen()

    @pytest.mark.regression
    def test_send_email(self,setup):
        self.Logger_4.info("**** Starting Test_004_search Customer by Email ****")
        self.driver = setup
        self.driver.get(self.baseurl)
        time.sleep(10)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.passw)
        self.lp.click_login_btn()
        self.Logger_4.info("***** Login Successful")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.clickOnCustomerMenu()
        self.add_cust.clickOnCsutomerSubmenu()

        self.Logger_4.info("**** Starting search By Email *****")

        send_Email_forSearch = SearchCustomer(self.driver)
        send_Email_forSearch.set_email("victoria_victoria@nopCommerce.com")
        send_Email_forSearch.click_search_btn()

        time.sleep(3)

        status = send_Email_forSearch.searchCustomerbyEmail("victoria_victoria@nopCommerce.com")
        if status == True:
            self.Logger_4.info("**** Test case_004_ Search customer by Email passed ****")
            assert True
        else:
            self.driver.save_Screenshot(".\\Screenshots\\" + "test_searchCustomerbyemail_src.png" )
            self.Logger_4.error("**** Test case_004_ Search customer by Email failed ***")
            assert False

        self.Logger_4.info("*** Test_004_search customer by Email Completed *** ")





