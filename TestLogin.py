from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

envtype = sys.argv[1]
if envtype == 'mac':
    driver = webdriver.Chrome('./macdriver/chromedriver')
if envtype == 'linux':
    driver = webdriver.Chrome('./linuxdriver/chromedriver')

driver.get("https://www.python.org")
driver.quit()