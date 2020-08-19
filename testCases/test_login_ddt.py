import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from utilities import ExcelUtils
import time


class Test_TC002_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData//LoginData.xlsx"
    logger = LogGen.loggen()
    lst_status = []
    exp= None


    @pytest.mark.regression
    def test_loginPageTitle_ddt(self,setup):

        self.logger.info("******* Starting Test Login Page DDT Test **********")
        self.logger.info("******* Starting Test 002 DDT LoginPage Title Test **********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.getRowCount(self.path,'Sheet1')
        print('Number of Rows: ', self.rows)

        for r in range(2,self.rows+1):
            self.user= ExcelUtils.readData(self.path,'Sheet1',r,1)
            self.password = ExcelUtils.readData(self.path,'Sheet1',r,2)
            self.status = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            if act_title == 'Dashboard / nopCommerce administration':
                if self.status == 'Pass':
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    self.lst_status.append("Pass")
                elif self.status == 'Fail':
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    self.lst_status.append("Fail")
            elif act_title != 'Dashboard / nopCommerce administration':
                if self.status == 'Pass':
                    self.logger.info("*** Failed ***")
                    self.lst_status.append("Fail")
                elif self.status == 'Fail':
                    self.logger.info("*** Passed ***")
                    self.lst_status.append("Pass")

        if "Fail" not in self.lst_status:
            self.logger.info("***** Login DDT Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT Failed *****")
            self.driver.close()
            assert False
        self.logger.info("******* Ending Test Login Page DDT Test  **********")
        self.logger.info("******* Completed Test 002 DDT LoginPage Title Test **********")
