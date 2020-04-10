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

    def test_search_text_field_by_name(self):
        # get the search textbox by attribute name
        search_field = self.driver.find_element_by_name('q')

    def test_search_text_field_by_class(self):
        # get the search textbox by class name
        search_field = self.driver.find_element_by_class_name('input-text')

    def test_search_button_enabled(self):
        # get Search button
        search_button = self.driver.find_element_by_class_name('button')

        # check Search button is enabled
        self.assertTrue(search_button.is_enabled())

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)