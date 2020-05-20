from bs4 import BeautifulSoup
import requests

def main():

  #soup = BeautifulSoup(page.content, 'html.parser')
  
  page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
  print(type(page))
  print(page.status_code)


if __name__ == '__main__':
  main()