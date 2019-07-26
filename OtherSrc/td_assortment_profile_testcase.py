# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from selenium import webdriver

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class td_assortment_profile_testcase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(3)
    
    def test_td_assortment_profile(self):
        success = True
        wd = self.wd
        wd.get("https://10.125.2.174/bin-java/login?f=general/login.htm")
        wd.find_element_by_id("login1").click()
        wd.find_element_by_id("login1").clear()
        wd.find_element_by_id("login1").send_keys("asliter")
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("wuhan02")
        if not wd.find_element_by_id("mapcheck").is_selected():
            wd.find_element_by_id("mapcheck").click()
        wd.find_element_by_xpath("//input[@class='sb']").click()
        try:
            wd.find_element_by_name("answeryes").click()
        except:
            pass
        wd.find_element_by_id("menuTrigger").click()
        wd.find_element_by_link_text("Assortment Profile").click()
        wd.find_element_by_link_text("Open All").click()
        wd.find_element_by_link_text("Set Assortment Permissions").click()
        wd.back()
        wd.find_element_by_link_text("Set Cluster Sequence").click()
        wd.back()
        wd.find_element_by_link_text("Store Groups").click()
        wd.back()
        wd.find_element_by_xpath("//a[@class='logout']/small").click()
        self.assertTrue(success)
        def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
