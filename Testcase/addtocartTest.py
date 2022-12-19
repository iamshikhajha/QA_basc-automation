import time
import unittest
from elementPackage.driversonly import drivers
from Functionality.addtocart import addTo


class MyTestCase(unittest.TestCase):
    def setUp(self):
        dr = drivers()
        self.driver = dr.driver
        self.driver.maximize_window()
        self.driver.get(dr.url)
        self.driver.implicitly_wait(10)

    def test_addtocartt(self):
        lp = addTo(self.driver)
        lp.addtoCart()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()
