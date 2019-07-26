import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://10.125.2.172")

    def user_login(self, username, password):
        self.driver.find_element_by_id("login1").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        if(self.driver.find_element_by_id("mapcheck").is_selected()):
            print("checked")
        else:
            self.driver.find_element_by_id("mapcheck").click()
        self.driver.find_element_by_xpath("//input[@value='Log In']").click()

    def test_login1(self):
        '''username and password is empty'''
        self.user_login("","")

    def test_login2(self):
        '''username is corrent, but password is blank'''
        self.user_login("superivy", "")

    def test_login3(self):
        '''username is empty, password is correct'''
        self.user_login("", "123")

    def test_login4(self):
        '''username and password is correct'''
        self.user_login("superivy", "wuhan02")

if __name__ == '__main__':
    unittest.main()
