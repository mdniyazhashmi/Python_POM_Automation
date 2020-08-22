from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        print('Launching Chrome Browser......')
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print('Launching Firefox Browser......')
    else:
        driver = webdriver.Ie(executable_path=IEDriverManager().install())
        print('Launching IE Browser default......')
    return driver

#This will get the value from CLI/hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

#This will retun the Browser value to the set up method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##################PyTest HTML Reports#######################


#It is hook to add additional environment info in the Html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Niyaz'

#It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins', None)