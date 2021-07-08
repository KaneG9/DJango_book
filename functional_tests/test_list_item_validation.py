from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

  def test_cannot_add_empty_list_items(self):
    self.browser.get(self.live_server_url)

    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('')
    inputbox.send_keys(Keys.ENTER)   

    self.fail('write me') 