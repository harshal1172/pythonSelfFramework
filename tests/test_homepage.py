import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testdata.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmit(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("entering firstname "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])

        self.dropdown(homepage.getGender(), getData["gender"])

        homepage.getSubmit().click()
        message = homepage.getSuccess().text
        assert 'Success' in message
        self.driver.refresh()

    #@pytest.fixture(params=HomePageData.test_homepage_data)
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param