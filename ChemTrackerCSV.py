# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:24:03 2021

@author: adple
"""
#Import required methods from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#Import time for wait step at end
import time

#Identify web browser driver and add directory to save in
chrome_options = Options()
prefs = {"download.default_directory" : r"C:\xx\xx\xx"}
chrome_options.add_experimental_option("prefs",prefs)
chromedriver = 'C:\xx\xx\chromedriver'

#Open browser and navigate to login
driver = webdriver.Chrome(executable_path = chromedriver, chrome_options = chrome_options)
wait = WebDriverWait(driver, 10)
driver.get('https://url')
assert "Sign On" in driver.title

#Enter username and password
username = driver.find_element_by_id("username")
username.clear()
username.send_keys("user")

password = driver.find_element_by_id("password")
password.clear()
password.send_keys("pwd")

#Navigate to download link for inventory .csv file
driver.find_element_by_class_name("ping-button.normal.allow").click()
wait.until(EC.presence_of_element_located((By.ID, "sidebar-left")))
driver.find_element_by_link_text("VINSE Cleanroom").click()
driver.find_element_by_link_text("ChemTracker").click()

#Download .csv file
wait.until(EC.presence_of_element_located((By.ID, "csv-export-link")))
driver.find_element_by_id("csv-export-link").click()

#Wait until file has downloaded then close browser window
time.sleep(5)
driver.quit()


