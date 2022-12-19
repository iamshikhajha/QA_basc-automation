import time
import unittest
from elementPackage.driversonly import drivers
from Functionality.login import functions


class myTestCase(unittest.TestCase):

    def setUp(self):
        dr = drivers()
        self.driver = dr.driver
        self.driver.maximize_window()
        self.driver.get(dr.url)
        self.driver.implicitly_wait(10)

    def test_login(self):
        lp = functions(self.driver)
        lp.login_part("shikha1@gmail.com", "password")
        time.sleep(10)

    def test_continue(self):
        lp = functions(self.driver)
        lp.login_check("sandarva", "shakya", "sandarva1@gmail.com", "password")
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
