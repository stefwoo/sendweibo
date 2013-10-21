#! /usr/bin/python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()
driver.get("https://www.neobux.com/m/l/")
assert u"NeoBux" in driver.title
elem1 = driver.find_element_by_id("Kf1")
elem1.send_keys("stefwoo888")
elem2 = driver.find_element_by_id("Kf2")
elem2.send_keys("Br1sjhhrhl")
elem2.send_keys(Keys.RETURN)
assert u"NeoBux" in driver.title
elem3 = driver.find_element_by_xpath('//a[@class = "bdrtton small2 purple"]')
elem3.click()
# driver.close()