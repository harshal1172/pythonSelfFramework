from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopPage()
        log.info("getting product list")
        products = checkOutPage.getProductList()

        for product in products:
            name = product.text
            if name == 'iphone X':
                log.info("adding product to cart " +name)
                checkOutPage.getProductName().click()

        checkOutPage.clickcheckOut().click()

        confirm = checkOutPage.confirmButton()
        log.info("entering country name")
        confirm.countryName().send_keys('India')

        self.waitMethod("India")

        confirm.countryClick().click()
        confirm.acceptbox().click()
        confirm.submit().click()

        successText = confirm.success().text
        log.info("text received from application " +successText)

        assert "Success! Thank you!" in successText

        #self.driver.get_screenshot_as_file("screen.png")





