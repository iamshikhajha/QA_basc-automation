from elementPackage.locators import locators
from selenium.webdriver.common.by import By

class checkFunction:

    def __init__(self,driver):
        self.l = locators()
        self.driver = driver


    def checkOut(self):
        self.driver.find_element(By.XPATH, self.l.Checkout).click()




