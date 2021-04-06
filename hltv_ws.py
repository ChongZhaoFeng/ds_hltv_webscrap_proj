import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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



''' Defining columns '''
team_A = []
team_B = []
score = []
maps = []
event = []




''' loop through all matches and extract data'''


i = 1
while i <= 20:

    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(/html/body/div[2]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[{0}]/div[2]/a/div/table/tbody/tr/td[2])'.format(str(i)))))
    score.append(element.text)
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(/html/body/div[2]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[{0}]/div[2]/a/div)'.format(str(i)))))
    element.click()
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="teamName"][1]')))
    team_A.append(element.text)
        
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="teamName"])[2]')))
    team_B.append(element.text)
        
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/a)')))
    event.append(element.text)
    
    
    driver.back()
    i+=1
    



    

''' Creating dataframe '''
df = pd.DataFrame({"Team A":team_A, "Score":score, "Team B":team_B, "Event":event})
print (df)




    
    
