from bs4 import BeautifulSoup
import requests

def main():

  
  # get web page
  page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
  
  print("Status code: ",page.status_code)
  
  
  # create BS object from page
  soup = BeautifulSoup(page.content, 'html.parser') 
  print(soup.prettify())
  
  body = soup.find('body')
  
  soup.find_all(class_="outer-text")
  
  soup.select("p a")
  soup.select("body p.first-item")
  
  
    
  


if __name__ == '__main__':
  main()