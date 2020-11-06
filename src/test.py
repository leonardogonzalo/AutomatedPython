import unittest
import time
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PIL import Image
from Util import Util
from PageVelocity import Velocity

class TestProcesos(unittest.TestCase):

    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='F:\\learingautomatization\\utilitarios\\chromedriver.exe')
        self.driver.maximize_window()

    def test_task(self):
        try:
            #Velocity(self.driver).programar_backups()
            Velocity(self.driver).login()
        except Exception as ex:
            self.driver.quit()
            print(ex)

    def tearDown(self):
        self.driver.quit()

if __name__== "__main__":
    unittest.main(verbosity=2,testRunner= HTMLTestRunner(output="reportes",report_name="rpt_test"))