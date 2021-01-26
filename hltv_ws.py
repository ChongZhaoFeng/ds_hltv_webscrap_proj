from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


'''landing the page'''

driver = webdriver.Chrome()
driver.get("https://hltv.org")
driver.maximize_window()        



'''allow cookies'''

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Allow all cookies")))
    element.click()
    

except:
    print ("Allow cookies fail")
    



''' search for desire team '''

try:
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@class="navsearchinput tt-input"]')))
    element.send_keys("Astralis")
    element.send_keys(Keys.ENTER)
    
except:
    print ("Input search fail")
    
    
    
''' press the first team on search result '''

try:
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Astralis")))
    element.click()
    
except:
    print ("Press search result fail")    



''' press all matches '''

try:
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@data-content-id='matchesBox']")))
    element.click()
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "See all results for Astralis")))
    element.click()
    
except:
    print ("all matches result fail")   
