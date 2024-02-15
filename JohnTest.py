from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import unittest

class TestCustomer(unittest.TestCase):

    def test_input1(self):
        driver = None
        driver_path = "D:\SeleniumChromeDriver\chromedriver-win64\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get("http://127.0.0.1/customer/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("canonc")
        age.send_keys("2")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        time.sleep(1)
        
        result = driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjohn", result)
        
        driver.close()

if __name__ == "__main__":
    unittest.main()