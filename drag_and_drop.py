from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import unittest

class TestAddition(unittest.TestCase):
    driver = None

    def setup(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(r"C:\Users\koga\Documents\chromedriver_win32\chromedriver.exe")
        url = 'http://pythonscraping.com/pages/javascript/draggableDemo.html'
        self.driver.get(url)
    
    def tear_down(self):
        self.driver.close()
    
    def test_drag(self):
        element = self.driver.find_element_by_id("draggable")
        target = self.driver.find_element_by_id("div2")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element, target).perform()
        self.assertEqual("You are definitely not a bot!", self.driver.find_element_by_id("message").text)

if __name__ == "__main__":
    test = TestAddition()
    test.setup()
    test.test_drag()
    test.tear_down()