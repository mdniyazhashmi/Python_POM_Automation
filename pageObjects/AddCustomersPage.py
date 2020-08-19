from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time


class AddCustomerPage:

    #Add Customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_submenu_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddNew_xpath = "//a[@class='btn bg-blue']"
    txtboxEmail_xpath = "//input[@id='Email']"
    txtboxPassword_id = "Password"
    txtboxFName_id = "FirstName"
    txtboxLName_id = "LastName"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtboxDOB_id = 'DateOfBirth'
    txtboxCompanyName_id = 'Company'
    chkboxtaxexempt_id = "IsTaxExempt"
    txtCustomerRoles_xpath = "//div[10]//div[2]//div[1]//div[1]//div[1]"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpdownManagerVendor_id = "VendorId"
    txtboxAdminComment_id = "AdminComment"
    btnSave_xpath = "//button[@class='btn bg-blue']"


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersSubMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_submenu_xpath).click()

    def clickonAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtboxEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.txtboxPassword_id).send_keys(password)

    def setFName(self, fname):
        self.driver.find_element_by_id(self.txtboxFName_id).send_keys(fname)

    def setLName(self, lname):
        self.driver.find_element_by_id(self.txtboxLName_id).send_keys(lname)

    def clickGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()

    def setDOB(self, dob):
        self.driver.find_element_by_id(self.txtboxDOB_id).send_keys(dob)

    def setCompanyName(self, company):
        self.driver.find_element_by_id(self.txtboxCompanyName_id).send_keys(company)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)

        if role == 'Registered':
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath("//li[@class='k-button']//span[@class='k-select']").click()
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)

        elif role == 'Forum Moderators':
            self.lstitem =self.driver.find_element_by_xpath("lstitemForumModerators_xpath")

        elif role == 'Vendors':
            self.lstitem = self.driver.find_element_by_xpath("lstitemVendors_xpath")

        else:
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.lstitem)

    def setManagerOfVendor(self,value):
        drp_ManagerOfVendor = Select(self.driver.find_element_by_id(self.drpdownManagerVendor_id))
        drp_ManagerOfVendor.select_by_visible_text(value)


    def setAdminComment(self,comment):
        self.driver.find_element_by_id(self.txtboxAdminComment_id).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()