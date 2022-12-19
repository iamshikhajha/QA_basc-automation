from selenium.webdriver.common.by import By
from elementPackage.locators import locators


class function:

    def __init__(self,driver):
        self.l = locators()
        self.driver = driver

    def Register_part(self,firstName,LastName,Email,Password):
            self.driver.find_element(By.XPATH,self.l.myAccount).click()
            self.driver.find_element(By.XPATH, self.l.Register).click()
            self.driver.find_element(By.ID, self.l.firstName).send_keys(firstName)
            self.driver.find_element(By.ID, self.l.LastName).send_keys(LastName)
            self.driver.find_element(By.ID, self.l.Email).send_keys(Email)
            self.driver.find_element(By.ID, self.l.Password).send_keys(Password)
            #self.driver.find_element(By.XPATH, self.l.Subscribe).click()
            self.driver.find_element(By.XPATH, self.l.PrivacyPolicy).click()
            self.driver.find_element(By.XPATH, self.l.button).click()




