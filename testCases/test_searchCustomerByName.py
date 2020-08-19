import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomersPage import AddCustomerPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_SearchCustomerByName:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):

        self.logger.info("************* TC005 Search Customer By Name **********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        # Login
        self.login = LoginPage(self.driver)
        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        self.logger.info("************* Login Successful **********")

        self.logger.info("************* Navigating to Search Customer Page **********")
        self.cust = AddCustomerPage(self.driver)
        self.cust.clickOnCustomersMenu()
        self.cust.clickOnCustomersSubMenuItem()

        self.logger.info("************* Starting Search Customer By Name **********")
        self.search = SearchCustomerPage(self.driver)
        self.search.setFname('John')
        self.search.setLname('Smith')
        self.search.clickSearch()
        time.sleep(5)
        status = self.search.searchCustomerByName('John Smith')
        print(status)
        if status == True:
            self.logger.info("Search Customer by Name passed successfully")
            assert True == True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_search_customer_by_name_scr.png")
            self.logger.error("Search Customer by Name test case failed")
            assert True == False
        self.logger.info("************* Search Customer By Name Finished **********")
        self.logger.info("************* TC005 Search Customer By Name Completed **********")
        self.driver.close()