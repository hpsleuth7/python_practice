from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def main():

  driver = webdriver.Firefox()
  
  driver.get('https://connectnetwork.com')
 
  sign_in = driver.find_element_by_link_text('SIGN IN')
  
  sign_in.click()
  
  # try to make this into a conditional -- check whether driver is in this state
  
  bday_field = driver.find_element_by_name('birthdate')
  bday_field.send_keys("1993-04-20")  #need to randomize birthdate for security 
  
  confirm_date = driver.find_element_by_class_name('pum-age-button-enter')
  confirm_date.click()
  
  driver.quit()
 
  
if __name__ == '__main__':
  main()