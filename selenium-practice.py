from selenium import webdriver

def main():

  driver = webdriver.Firefox()
  
  driver.get('https://wikipedia.com')
  
  driver.quit()
  
if __name__ == '__main__':
  main()