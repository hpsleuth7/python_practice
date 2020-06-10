from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def main():

  driver = webdriver.Firefox()
  
  driver.get('https://wikipedia.com')
 
  # pull out 'select language' element  
  search_language = driver.find_element_by_id('searchLanguage') 
  
  # command driver to select Latin 
  Select(search_language).select_by_visible_text('Latina')
  
  # pull out input element for search 
  search_input = driver.find_element_by_id('searchInput')
  
  # command driver to input 'Marcus Aurelius' into search element 
  search_input.send_keys('Marcus Aurelius')
  
  # pull out search button
  search_button = driver.find_element_by_xpath('/html/body/div[2]/form/fieldset/button/i')
  
  search_button.click()
  
  driver.quit()
  
if __name__ == '__main__':
  main()