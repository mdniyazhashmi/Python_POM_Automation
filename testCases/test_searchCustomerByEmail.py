import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomersPage import AddCustomerPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Test_004_SearchCustomerByEmail:


    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_SearchCustomerByEmail(self,setup):

        self.logger.info("************* TC004 Search Customer By Email Starting **********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        #Login
        self.login = LoginPage(self.driver)
        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        self.logger.info("************* Login Successful **********")

        self.logger.info("************* Navigating to Search Customer Page **********")
        self.cust = AddCustomerPage(self.driver)
        self.cust.clickOnCustomersMenu()
        self.cust.clickOnCustomersSubMenuItem()

        self.logger.info("************* Search Customer By Email Starting **********")
        self.search = SearchCustomerPage(self.driver)
        self.search.setEmail('james_pan@nopCommerce.com')
        self.search.clickSearch()
        time.sleep(5)
        status = self.search.searchCustomerByEmail('james_pan@nopCommerce.com')
        print(status)
        if status == True:
          self.logger.info("Search Customer by Email passed successfully")
          assert True == True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_search_customer_by_email_scr.png")
            self.logger.error("Search Customer by Email test case failed")
            assert True == False
        self.logger.info("************* Search Customer By Email Finished **********")
        self.logger.info("************* TC004 Search Customer By Email Completed **********")
        self.driver.close()

