#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from time import sleep


# driver = webdriver.Firefox()
print("Waiting for selenium docker startup...")

driver = None
remaining_attempts = 60
while (driver is None) and (remaining_attempts > 0):
	try:
		driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.FIREFOX)
	except:
		remaining_attempts -= 1
		sleep(1)
		pass

server = 'http://dvwa:80'

ready = False
remaining_attempts = 60
while (not ready) and (remaining_attempts > 0):
	try:
		driver.get(server + '/login.php')
		ready = True
	except:
		remaining_attempts -= 1
		sleep(1)
		ready = False

print('Starting selenium tests...')

driver.get(server + '/login.php')
driver.find_element_by_name('username').click()
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_name('password').send_keys(Keys.ENTER)

driver.get(server + '/vulnerabilities/exec')
driver.find_element_by_name('ip').click()
driver.find_element_by_name('ip').clear()
driver.find_element_by_name('ip').send_keys('8.8.8.8')
driver.find_element_by_name('Submit').click()

driver.get(server + '/vulnerabilities/xss_s')
driver.find_element_by_name('txtName').click()
driver.find_element_by_name('txtName').send_keys('usenmame')
driver.find_element_by_name('mtxMessage').click()
driver.find_element_by_name('mtxMessage').send_keys('comment')
driver.find_element_by_name('btnSign').click()

driver.get(server + '/vulnerabilities/fi/?page=file1.php')

driver.get(server + '/vulnerabilities/xss_r')
driver.find_element_by_name('name').click()
driver.find_element_by_name('name').send_keys('usenmame')
driver.find_element_by_xpath("//input[@value='Submit']").click()

driver.quit()

print('Selenium tests are done')
