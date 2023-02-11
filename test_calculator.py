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

        self.driver.get("http://localhost:3001/")
        print("we are all set!")
        time.sleep(20)
        zero = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[5]/div[1]/button')
        one = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[4]/div[1]/button')
        two = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[4]/div[2]/button')
        three = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[4]/div[3]/button')
        four = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[3]/div[1]/button')
        five = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[3]/div[2]/button')
        six = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[3]/div[3]/button')
        seven = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/button')
        eight = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/button')
        nine = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/button')

        self.result = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[1]/div')

        self.negative_sign = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[1]/div[2]/button')

        self.subtraction_sign = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[3]/div[4]/button')

        self.plus_sign = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[4]/div[4]/button')
        self.equal_sign = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[5]/div[3]/button')
        self.testArr = [zero, one, two, three, four, five, six, seven, eight, nine]
        # print("Hi")

    def testAdd(self):
        for i in range(10):
            for j in range(10):
                number1 = i
                number2 = j
                expected_value = number1 + number2

                self.testArr[i].click()
                self.plus_sign.click()
                self.testArr[j].click()
                self.equal_sign.click()
                result_1 = int(self.result.text)
                self.assertEqual(result_1, expected_value)

    def test_negative_number_in_add(self):
        for i in range(10):
            for j in range(10):
                number1 = -(i)
                number2 = j
                expected_value = number1 + number2

                self.testArr[i].click()
                self.negative_sign.click()
                self.plus_sign.click()
                self.testArr[j].click()
                self.equal_sign.click()
                result_1 = int(self.result.text)
                self.assertEqual(result_1, expected_value)

    def test_subtraction(self):
        for i in range(10):
            for j in range(10):
                number1 = i
                number2 = j
                expected_value = number1 - number2

                self.testArr[i].click()
                self.subtraction_sign.click()
                self.testArr[j].click()
                self.equal_sign.click()
                result_1 = int(self.result.text)

                self.assertEqual(result_1, expected_value)

    def test_subtraction_with_negative_number_in_first_place(self):
        for i in range(10):
            for j in range(10):
                number1 = -(i)
                number2 = j
                expected_value = number1 - number2

                self.testArr[i].click()
                self.negative_sign.click()
                self.subtraction_sign.click()
                self.testArr[j].click()
                self.equal_sign.click()
                result_1 = int(self.result.text)
                # print(f'result_1 = {result_1}')
                self.assertEqual(result_1, expected_value)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
