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
A1_adr = []
A2_adr = []
A3_adr = []
A4_adr = []
A5_adr = []
B1_adr = []
B2_adr = []
B3_adr = []
B4_adr = []
B5_adr = []



''' loop through all matches and extract data'''

i = 1
while i <= 5:
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(/html/body/div[2]/div/div[2]/div[1]/div[2]/div[7]/div[1]/div[{0}]/div[2]/a/div/table/tbody/tr/td[1]/div/div)'.format(str(i)))))
    team_A.append(element.text)

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(/html/body/div[2]/div/div[2]/div[1]/div[2]/div[7]/div[1]/div[{0}]/div[2]/a/div/table/tbody/tr/td[3]/div/div)'.format(str(i)))))
    team_B.append(element.text)    
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="result-con "])[{0}]'.format(str(i)))))
    element.click()
    driver.back()
    i = i+1
  

''' Creating dataframe '''
df = pd.DataFrame({"Team A":team_A, "Team B":team_B})
print (df)

'''
df = pd.DataFrame({"Team A":team_A,"Team B":team_B, "Score":score, "Map":maps, "Event":event, "A1_adr":A1_adr, "A2_adr":A2_adr,"A3_adr":A3_adr,"A4_adr":A4_adr, "A5_adr":A5_adr, "B1_adr":B1_adr, "B2_adr":B2_adr, "B3_adr":B3_adr, "B4_adr":B4_adr, "B5_adr":B5_adr })
df
'''



    
    
    
