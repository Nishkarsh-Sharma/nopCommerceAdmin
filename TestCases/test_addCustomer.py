import string
import time
import random

from selenium.webdriver.common.by import By

from Utilities.readProperties import ReadConfig
from pageObjects.AddCustomers import AddCustomer
from Utilities.customLogger import LogGen
import pytest

from pageObjects.LoginPage import LoginPage


class Test_003_addCustomer:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    passw = ReadConfig.getPassword()
    Logger_3 = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.Logger_3.info("***** Test Case_003_AddCustomer ****")
        self.driver = setup
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.passw)
        self.lp.click_login_btn()
        self.Logger_3.info("**** Login Successful******")

        self.Logger_3.info("**** Starting Add Customer Test ****")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.clickOnCustomerMenu()
        self.add_cust.clickOnCsutomerSubmenu()
        self.add_cust.clickOnAddnew()

        self.Logger_3.info("**** Providing new Customer info")

        self.email = random_generator() + "@gmail.com"
        self.add_cust.setEmail(self.email)
        self.add_cust.setPassword("test123")
        self.add_cust.setFirstname("Rahul")
        self.add_cust.setLastname("Shetty")
        self.add_cust.setGender("Male")
        self.add_cust.setCompanyName("Testers around")
        self.add_cust.setCustomerRoless("Vendors")
        self.add_cust.setManagerofVendor("Vendor 2")
        self.add_cust.setAdminComment("This is for testing.... ")
        self.add_cust.clickOnSave()

        self.Logger_3.info("**** Saving customer info *****")
        self.Logger_3.info("***** Add customer validation started *****")

        self.save_msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.save_msg)


        if "The new customer has been added successfully." in self.save_msg:
            assert True
            self.Logger_3.info("**** Add Customer Test Case PAssed ***** ")
        else:
            self.driver.save_screenshot(r"C:\Users\nishk\PycharmProjects\nopCommerceAdmin\Screenshots\test_add_customer_scr.png")
            self.Logger_3.error("**** Add customer Test Case failed **** ")
            assert False

        self.Logger_3.info("**** Ending Test_003_Add Customer ****")

def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))



