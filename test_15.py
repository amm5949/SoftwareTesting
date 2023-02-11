import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import time


class TestCase(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(
            executable_path=r'C:\webdrivers\geckodriver.exe', options=options)

        self.driver.maximize_window()

        self.driver.delete_all_cookies()

        self.driver.get("http://localhost:3000/")
        print("we are all set!")
        time.sleep(20)

    def testCard(self):
        src1 = '/html/body/div/main/div/div[1]'
        src2 = '/html/body/div/main/div/div[2]'

        card1 = self.driver.find_element(By.XPATH, src1)
        
        card2 = self.driver.find_element(By.XPATH, src2)
        
        location2 = card2.location
        # time.sleep(20)
        action = ActionChains(self.driver)
        action.click_and_hold(card1)
        action.release(card2)
        action.perform()

        time.sleep(10)

        location1_after_movement = card1.location
        self.assertEqual(location2, location1_after_movement)

    def testList(self):
        src1 = '/html/body/div/main/div/div[1]'
        src2 = '/html/body/div/main/div/div[2]'

        list1 = self.driver.find_element(By.XPATH, src1)
        
        list2 = self.driver.find_element(By.XPATH, src2)

        location2 = list2.location
        
        action = ActionChains(self.driver)
        action.click_and_hold(list1)
        action.release(list2)
        action.perform()

        time.sleep(10)

        location1_after_movement = list1.location
        self.assertEqual(location2, location1_after_movement)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

# driver = webdriver.Firefox()

# # driver.maximize_window()

# print(driver._mobile)

# driver.get("https://www.google.com")
