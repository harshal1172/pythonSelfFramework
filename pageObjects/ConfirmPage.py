from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    #self.driver.find_element_by_id('country').send_keys('India')
    countryname = (By.ID, "country")
    #self.driver.find_element_by_link_text("India").click()
    country_click = (By.LINK_TEXT, "India")
    #self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
    acceptcheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    #self.driver.find_element_by_css_selector("[type='submit']").click()
    submitbutton = (By.CSS_SELECTOR, "[type='submit']")
    #self.driver.find_element_by_class_name("alert-success").text
    successmessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def countryName(self):
        return self.driver.find_element(*ConfirmPage.countryname)

    def countryClick(self):
        return self.driver.find_element(*ConfirmPage.country_click)

    def acceptbox(self):
        return self.driver.find_element(*ConfirmPage.acceptcheckbox)

    def submit(self):
        return self.driver.find_element(*ConfirmPage.submitbutton)

    def success(self):
        return self.driver.find_element(*ConfirmPage.successmessage)