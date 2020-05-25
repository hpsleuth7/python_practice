# A practice scraper on the NOAA website
# Usage: prints information on 7-day forecast in San Francisco

from bs4 import BeautifulSoup
import requests

def main():

  page = request("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XswPwsYpAUs")
  
  soup=BeautifulSoup(page.content,'html.parser')
  
  


if __name__ == '__main__':
  main()