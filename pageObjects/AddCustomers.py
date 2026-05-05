from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


class AddCustomer:
    customers_menu_xpath = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    customer_submenu_xpath = "//a[@href='/Admin/Customer/List']"
    btn_add_new_xpath = "//a[normalize-space()='Add new']"
    text_Email_id = "Email"
    text_Password_id = "Password"
    # txt_customerRoles_xpath = "//ul[@class='select2-selection__rendered']"
    # lstItems_administrator_xpath = "//li[@title='Administrators']"
    # lstItems_forumModerator_xpath = "//li[@title='Forum Moderators']"
    # lstItems_registered_xpath = "//li[@title='Registered']"
    # lstItems_guest_xpath = "//li[contains(text(), 'Guests')]"
    # lstItems_vendor_xpath = "//li[@title='Vendors']"
    dropdown_managerofVendor_xpath = "//select[@id='VendorId']"
    rd_male_id = "Gender_Male"
    rd_female_id = "Gender_Female"
    text_firstName_xpath = "//input[@id='FirstName']"
    text_lastname_xpath = "//input[@id='LastName']"
    text_company_name_xpath = "//input[@id='Company']"
    text_adminComment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"
    dropdown_Customer_roles_xpath = "//select[@id='SelectedCustomerRoleIds']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.customers_menu_xpath).click()

    def clickOnCsutomerSubmenu(self):
        self.driver.find_element(By.XPATH,self.customer_submenu_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.btn_add_new_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.text_Email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.text_Password_id).send_keys(password)

    # def setCustomerRoles(self,role):
    #     #self.driver.find_element(By.XPATH, "//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']").click()
    #     #time.sleep(2)
    #     self.driver.find_element(By.XPATH,self.txt_customerRoles_xpath).click()
    #     time.sleep(3)
    #     if role == "Registered":
    #         self.listItem = self.driver.find_element(By.XPATH,self.lstItems_registered_xpath)
    #     elif role == "Administrators":
    #         self.listItem = self.driver.find_element(By.XPATH,self.lstItems_administrator_xpath)
    #     elif role == "Forum Moderators":
    #         self.listItem = self.driver.find_element(By.XPATH,self.lstItems_forumModerator_xpath)
    #     elif role == "Vendors":
    #         self.listItem = self.driver.find_element(By.XPATH,self.lstItems_vendor_xpath)
    #     elif role == "Guests":
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH,"//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']").click()
    #         self.driver.find_element(By.XPATH, self.txt_customerRoles_xpath).click()
    #         self.listItem = self.driver.find_element(By.XPATH,self.lstItems_guest_xpath)
    #     #else:
    #        self.listItem = self.driver.find_element(By.XPATH,self.lstItems_guest_xpath)
    #     #time.sleep(3)
    #
    #     #self.driver.execute_script("arguments[0].click();",self.listItem)

    def setCustomerRoless(self,value):
        drp_cus = Select(self.driver.find_element(By.XPATH,self.dropdown_Customer_roles_xpath))
        if value == "Guests":
            self.driver.find_element(By.XPATH,"//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']").click()
            time.sleep(2)
            drp_cus.select_by_visible_text(value)
        else:
            drp_cus.select_by_visible_text(value)
            time.sleep(2)

    def setManagerofVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.dropdown_managerofVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.rd_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID,self.rd_female_id).click()
        else:
            self.driver.find_element(By.ID,self.rd_male_id).click()

    def setFirstname(self,fname):
        self.driver.find_element(By.XPATH,self.text_firstName_xpath).send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element(By.XPATH,self.text_lastname_xpath).send_keys(lname)

    def setAdminComment(self,comment_content):
        self.driver.find_element(By.XPATH,self.text_adminComment_xpath).send_keys(comment_content)

    def setCompanyName(self,company_name):
        self.driver.find_element(By.XPATH,self.text_company_name_xpath).send_keys(company_name)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()









