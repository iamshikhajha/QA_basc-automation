from selenium.webdriver.common.by import By
from elementPackage.locators import locators

class addTo:

    def __init__(self,driver):
        self.l = locators()
        self.driver = driver

    def addtoCart(self):
        self.driver.find_element(By.XPATH, self.l.shoppingCart).click()
        self.driver.find_element(By.XPATH, self.l.continueBtn).click()

