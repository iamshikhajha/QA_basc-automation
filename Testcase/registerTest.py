import time
import unittest
from elementPackage.driversonly import drivers
from Functionality.Register import function


class MyTestCase(unittest.TestCase):

    def setUp(self):
        dr = drivers()
        self.driver = dr.driver
        self.driver.maximize_window()

        self.driver.get(dr.url)
        self.driver.implicitly_wait(10)

    def test_Register(self):
        lp = function(self.driver)
        lp.Register_part("Shikha","Jha","shikha1@gmail.com","password")
        time.sleep(10)


    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()
