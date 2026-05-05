import time

import pytest
from selenium import webdriver
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtility


from pageObjects.LoginPage import LoginPage


class Test_002_DDT_login:
    base_url = ReadConfig.getApplicationURL()
    path = ".//TestData/Demo_TestData.xlsx"
    Logger_1 = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.Logger_1.info("********* Test Case _002 DDT_Login ***************")
        self.Logger_1.info("********** Verifying Login _DDT Test Case **********")
        self.driver = setup
        self.driver.get(self.base_url)
        time.sleep(8)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)

        self.rows = ExcelUtility.getRowCount(self.path, "Sheet1")
        print("Number of row: ", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = ExcelUtility.readData(self.path, "Sheet1", r, 1)
            self.passw = ExcelUtility.readData(self.path, "Sheet1", r, 2)
            self.exp = ExcelUtility.readData(self.path, "Sheet1", r, 3)

            lp.setUserName(self.user)
            lp.setPassword(self.passw)
            lp.click_login_btn()
            time.sleep(2)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.Logger_1.info("********** Passed ********")
                    lp.click_logout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.Logger_1.info("**** Failed *****")
                    lp.click_logout()
                    lst_status.append("Failed")

            elif act_title != exp_title:
                if self.exp == "Passed":
                    self.Logger_1.info("**** Failed *****")
                    lst_status.append("Failed")
                elif self.exp == "Failed":
                    self.Logger_1.info("*** Passed ***")
                    lst_status.append("Passed")

            if "Failed" not in lst_status:
                self.Logger_1.info("*** Login_DDT Test Case is passed ***")
                assert True
            else:
                self.Logger_1.info("**** Login_DDT Test Case is failed ****")
                assert False

        self.Logger_1.info("**** End of Login_DDT Test Case ****")
        self.Logger_1.info("**** Test Case_002_DDT Completed ****")










