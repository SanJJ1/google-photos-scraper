from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import shelve
import pprint as pp
from functions import *
browser = webdriver.Firefox(executable_path=r'geckodriver.exe')

url = 'https://photos.google.com/photo/AF1QipOFKFN6sPB5lauRLyQdINkhGQQU93zpuVkVSIKw'
browser.get(url)
input('paused: ')
print("resumed: ")

# login to google
user = '21janardhansanjay@gmail.com'
browser.find_element_by_css_selector("#identifierId").send_keys(user)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()


pw = 'lisztchopinrachmaninoff'
browser.find_element_by_css_selector("#identifierId").send_keys(pw)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()



