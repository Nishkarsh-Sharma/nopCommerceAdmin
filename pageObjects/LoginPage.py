from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_id = "Password"
    btn_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_LinkText = "Logout"

    def __init__(self,driver):
        self.driver = driver


    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_LinkText).click()






