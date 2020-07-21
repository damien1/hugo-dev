# test case for {{< cld-response >}} shortcode

# Import the 'modules' that are required for execution
import unittest
import pytest
import time
import datetime
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

date = datetime.date.today().strftime("%Y%m%d")

class TestShortcode(unittest.TestCase):
    # An Example test Case, to show off the set-up of a screen-shot on exception.

    def setUp(self):
        """Set up the Browser and the Tear Down."""
        self.driver = webdriver.Chrome()

        # NOTE: In addCleanup, the first in, is executed last.
        self.addCleanup(self.driver.quit)
        self.addCleanup(self.screen_shot)
        self.driver.implicitly_wait(2)

    def screen_shot(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        for method, error in self._outcome.errors:
            if error:
                self.driver.get_screenshot_as_file("tests/failure_screenshots/" + date + self.id() + ".png")

    # def test_fails(self):
    #     """A test case that fails because of missing element."""
    #     self.driver.get("http://www.google.com")
    #     self.driver.find_element_by_css_selector("div.that-does-not-exist")

    def test_internal(self):
    # A test case that passes
        self.driver.get("http://localhost:9081/")
        self.driver.delete_all_cookies()
        print(str("no cookies"))
        assert "Airspace" in self.driver.title
        self.driver.set_window_size(1000, 600)
    
    # # check custom footer content
    #     elements = self.driver.find_elements(By.CSS_SELECTOR, ".cd-headline")
    #     assert len(elements) > 0
    #     assert self.driver.find_element(By.CSS_SELECTOR, ".copy").text == "Copyright © 2004 - 2020 Damien Saunders."
    #     elements = self.driver.find_elements(By.CSS_SELECTOR, ".pages")
    #     assert len(elements) > 0

    #resize for tablet
        self.driver.set_window_size(400, 600)
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".navbar-toggle")
        assert len(elements) > 0
        self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggle").click()
        WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".About")))
        self.driver.find_element(By.XPATH, "//a[contains(@href,'about')]").click()
        print(str("resized ok"))
        self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler").click()
        WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Blog")))
        self.driver.find_element(By.CSS_SELECTOR, ".Blog").click()
        self.driver.set_window_size(1000, 600)
    
    #find pagination
        element_scroll = self.driver.find_element(By.XPATH, "//span[contains(.,\'»\')]")
        actions = ActionChains(self.driver)
        actions.move_to_element(element_scroll).perform()
        self.driver.find_element(By.XPATH, "//span[contains(.,\'»\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler").click()
        WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".About")))
        self.driver.find_element(By.CSS_SELECTOR, ".About").click()
        self.driver.save_screenshot('tests/passed/' + date + '_local_screenshot.png')
        print(str("OK"))  

    #   # check for backend
    #     self.driver.get("http://localhost:9081/backend/")
    #     print(self.driver.title)
    #     assert "Backend" in self.driver.title
    #     print(str(" ... all done ..."))  