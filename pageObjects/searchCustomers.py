from selenium.webdriver.common.by import By
import time

class SearchCustomer:
    text_searchbyEmail_xpath = "//input[@id='SearchEmail']"
    text_searchbyFirstname_xpath = "//input[@id='SearchFirstName']"
    text_searchbyLastname_xpath = "//input[@id='SearchLastName']"
    table_customerData_xpath = "//table[@id='customers-grid']"
    table_customerData_rows_xpath = "//tbody/tr"
    table_customerData_columns_xpath = "//tbody/tr/td"
    btn_searchBtn_xpath = "//button[@id='search-customers']"

    def __init__(self,driver):
        self.driver = driver

    def set_email(self,email):
        self.driver.find_element(By.XPATH,self.text_searchbyEmail_xpath).clear()
        self.driver.find_element(By.XPATH,self.text_searchbyEmail_xpath).send_keys(email)

    def set_firstName(self,Fname):
        self.driver.find_element(By.XPATH, self.text_searchbyFirstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_searchbyFirstname_xpath).send_keys(Fname)

    def set_lastName(self,Lname):
        self.driver.find_element(By.XPATH, self.text_searchbyLastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_searchbyLastname_xpath).send_keys(Lname)

    def click_search_btn(self):
        self.driver.find_element(By.XPATH, self.btn_searchBtn_xpath).click()

    def getNoOfrows(self):
        return len(self.table_customerData_rows_xpath)

    def getNoOfColumns(self):
        return len(self.table_customerData_columns_xpath)

    def searchCustomerbyEmail(self,email):
        flag = False
        for r in range(1, self.getNoOfrows() + 1):
            table = self.driver.find_element(By.XPATH,self.table_customerData_xpath)
            emailID = table.find_element(By.XPATH, "//tbody/tr["+str(r)+"]/td[2]").text
            if emailID == email:
                flag = True
                break
        return flag

    def searchCustomerbyName(self,Name):
        flag = False
        for r in range(1, self.getNoOfColumns() + 1):
            table = self.driver.find_element(By.XPATH, self.table_customerData_xpath)
            Name_search = table.find_element(By.XPATH, "//tbody/tr["+str(r)+"]/td[3]").text
            if Name == Name_search:     # or Name in Name_search
                flag = True
                break
        return flag



