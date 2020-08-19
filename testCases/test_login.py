import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage


class Test_TC001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_loginPageTitle(self,setup):
        self.logger.info("************* Test_001_Login **********")
        self.logger.info("******* Starting LoginPage Title Test **********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        if self.driver.title == "Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("LoginPage Title Test Passed")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_LoginPageTitle_scr.png")  # Screenshot
            self.driver.close()
            self.logger.error("LoginPageTitle Test Failed")
            assert False
        self.logger.info("******* Ending LoginPage Title Test **********")


    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("******* Starting HomePage Title Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        if self.driver.title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            self.logger.info("HomePage Title Test Passed")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_HomepageTitle_scr.png")  # Screenshot
            self.driver.close()
            self.logger.error("HomePage Title Test Failed")
            assert False
        self.logger.info("******* Ending HomePage Title Test **********")