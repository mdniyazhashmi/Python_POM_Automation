from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time


class SearchCustomerPage:

    txtboxsearchEmail_id = "SearchEmail"
    txtboxsearchFname_id = "SearchFirstName"
    txtboxsearchLname_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblsearchResults_xpath = "//table[@role='grid']"
    tbl_xpath = "//table[@id='customers-grid']"
    tblrows_xpath = "//table[@id='customers-grid']/tbody/tr"
    tblcols_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtboxsearchEmail_id).clear()
        self.driver.find_element_by_id(self.txtboxsearchEmail_id).send_keys(email)

    def setFname(self,fname):
        self.driver.find_element_by_id(self.txtboxsearchFname_id).clear()
        self.driver.find_element_by_id(self.txtboxsearchFname_id).send_keys(fname)

    def setLname(self,lname):
        self.driver.find_element_by_id(self.txtboxsearchLname_id).clear()
        self.driver.find_element_by_id(self.txtboxsearchLname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getRowsNum(self):
        return len(self.driver.find_elements_by_xpath(self.tblrows_xpath))

    def getColsNum(self):
        return len(self.driver.find_elements_by_xpath(self.tblcols_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for i in range(1,self.getRowsNum()+1):
            table = self.driver.find_element_by_xpath(self.tbl_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(i)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag = False
        for i in range(1,self.getRowsNum()+1):
            table = self.driver.find_element_by_xpath(self.tbl_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(i)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag