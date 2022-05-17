from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver



    productNames = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    productAdd = (By.XPATH, "//div[@class='card h-100']/div[2]/button")
    #self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
    checkOutButton = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    confirmbutton = (By.XPATH, "//button[@class='btn btn-success']")


    def getProductList(self):
        return self.driver.find_elements(*CheckOutPage.productNames)

    def getProductName(self):
        return self.driver.find_element(*CheckOutPage.productAdd)

    def clickcheckOut(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton)

    def confirmButton(self):
        self.driver.find_element(*CheckOutPage.confirmbutton).click()
        confirm = ConfirmPage(self.driver)
        return confirm

