import unittest
from selenium import webdriver

class HomePageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Opera session
        cls.driver = webdriver.Opera(executable_path = '../operadriver')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()

        # navigate to the application Home page
        driver.get('http://demo-store.seleniumacademy.com')

    def test_search_text_field(self):
        # get the search textbox
        search_field = self.driver.find_element_by_id('search')

        # check maxlength attribute is set to 128
        self.assertEqual('128', search_field.get_attribute('maxlength'))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)