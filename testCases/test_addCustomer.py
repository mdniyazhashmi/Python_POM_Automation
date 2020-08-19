import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomersPage import AddCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.sanity
    def test_addCustomer(self,setup):

        self.logger.info("************* Test 003 Add Customer **********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        #Login
        self.login = LoginPage(self.driver)
        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        self.logger.info("************* Login Successful **********")

        self.logger.info("************* Starting Add New Customer **********")
        self.cust = AddCustomerPage(self.driver)
        self.cust.clickOnCustomersMenu()
        self.cust.clickOnCustomersSubMenuItem()
        self.cust.clickonAddNew()

        self.logger.info("************* Providing Customer Info **********")
        self.email = random_generator()+"@gmail.com"
        print(self.email)
        self.cust.setEmail(self.email)
        self.cust.setPassword("test123")
        self.cust.setFName("niyaz")
        self.cust.setLName("hashmi")
        self.cust.clickGender("Male")
        self.cust.setDOB("8/15/2005")
        self.cust.setCompanyName("SDET")
        time.sleep(5)
        self.cust.setCustomerRoles("Guests")
        self.cust.setManagerOfVendor("Vendor 1")
        self.cust.setAdminComment("testing")
        self.cust.clickOnSave()
        self.logger.info("************* Saving Customer Info **********")

        self.logger.info("************* Add Customer Validation Started **********")

        msg = self.driver.find_element_by_tag_name("body").text

        print(msg)

        if "The new customer has been added successfully." in msg:
            self.logger.info("Add Customer Test case passed")
            assert True == True
        else:

            self.driver.save_screenshot(".\\screenshots\\"+"test_add_customer_scr.png")
            self.logger.error("Add Customer Test case failed")
            assert True == False
        self.driver.close()
        self.logger.info("Add Customer Test case completed")

def random_generator(size=8, chars = string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))