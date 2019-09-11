
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
  

driver = webdriver.Firefox()
  
driver.get("https://web.whatsapp.com/") 
driver.implicitly_wait(100)
  
target = 'Notes'
string ="Sample Spam text!!"

xpath_title='//span[@title="' + target + '"]/ancestor::div[6]'
xpath_inp='//div[@dir="ltr"][@spellcheck="true"]'


title=driver.find_element_by_xpath(xpath_title)
title.click()

inp=driver.find_element_by_xpath(xpath_inp)
inp.send_keys(string + Keys.ENTER) 

	

